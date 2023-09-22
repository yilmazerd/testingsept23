import boto3

def create_aurora_postgres_cluster(client, cluster_id, master_username, master_password):
    try:
        response = client.create_db_cluster(
            DBClusterIdentifier=cluster_id,
            Engine='aurora-postgresql',
            MasterUsername=master_username,
            MasterUserPassword=master_password,
            PubliclyAccessible=True
        )
        print("Cluster created successfully:", response)
    except Exception as e:
        print("Error creating cluster:", e)

def create_db_instance(client, instance_id, cluster_id):
    try:
        response = client.create_db_instance(
            DBInstanceIdentifier=instance_id,
            DBClusterIdentifier=cluster_id,
            Engine='aurora-postgresql',
            DBInstanceClass='db.r5.large',
            PubliclyAccessible=True
        )
        print("DB instance created successfully:", response)
    except Exception as e:
        print("Error creating DB instance:", e)

def main():
    client = boto3.client('rds', region_name='your-region')  # e.g., 'us-west-1'
    
    cluster_identifier = "your-cluster-identifier"
    master_username = "masteruser"
    master_password = "masteruserpassword"
    
    instance_identifier = "your-instance-identifier"
    
    create_aurora_postgres_cluster(client, cluster_identifier, master_username, master_password)
    create_db_instance(client, instance_identifier, cluster_identifier)

if __name__ == "__main__":
    main()
