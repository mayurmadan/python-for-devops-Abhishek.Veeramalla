import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    # Get all EBS snapshots
    response = ec2.describe_snapshots(OwnerIds=['self'])

    # Get all active EC2 instance IDs
    instances_response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    active_instance_ids = set()

#This accesses the list of reservations returned in the instances_response object. Each reservation represents a group of instances launched together.
    #This iterates over each reservation in the list.
    for reservation in instances_response['Reservations']:
        #This accesses the list of instances within the current reservation.
        # iterates over each instance in the list of instances within the current reservation.
        for instance in reservation['Instances']:
            # This accesses the ID of the current instance.
            # This adds the instance ID to the active_instance_ids set. Sets are used here to ensure that each instance ID is unique, avoiding duplicates.
            active_instance_ids.add(instance['InstanceId'])

    # Iterate through each snapshot and delete if it's not attached to any volume or the volume is not attached to a running instance
            # This iterates over each snapshot in the list of snapshots returned in the response object.
    for snapshot in response['Snapshots']:
        #This retrieves the ID of the current snapshot.
        snapshot_id = snapshot['SnapshotId']
        #: This retrieves the ID of the volume associated with the current snapshot. The get method is used to safely retrieve the value of the VolumeId key from the snapshot. If the key doesn't exist (i.e., the snapshot is not attached to any volume), volume_id will be None
        volume_id = snapshot.get('VolumeId')
        
        #This condition checks if volume_id is None, indicating that the snapshot is not attached to any volume.
        if not volume_id:
            # Delete the snapshot if it's not attached to any volume
            ec2.delete_snapshot(SnapshotId=snapshot_id)
            print(f"Deleted EBS snapshot {snapshot_id} as it was not attached to any volume.")
        #If the snapshot is attached to a volume, this block of code executes.    
        else:
            # Check if the volume still exists
            #This block of code attempts to describe the volume associated with the snapshot.
            try:
                #retrieves the list of attachments for the first volume in the volume_response object.
                volume_response = ec2.describe_volumes(VolumeIds=[volume_id])
                if not volume_response['Volumes'][0]['Attachments']:
                    ec2.delete_snapshot(SnapshotId=snapshot_id)
                    print(f"Deleted EBS snapshot {snapshot_id} as it was taken from a volume not attached to any running instance.")
            except ec2.exceptions.ClientError as e:
                if e.response['Error']['Code'] == 'InvalidVolume.NotFound':
                    # The volume associated with the snapshot is not found (it might have been deleted)
                    ec2.delete_snapshot(SnapshotId=snapshot_id)
                    print(f"Deleted EBS snapshot {snapshot_id} as its associated volume was not found.")
