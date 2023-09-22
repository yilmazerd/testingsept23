import subprocess

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error: {e}")

def create_aurora_postgres_cluster(cluster_id, master_username, master_password):
    command = f"""aws rds create-db-cluster \
                  --db-cluster-identifier {cluster_id} \
                  --engine aurora-postgresql \
                  --master-username {master_username} \
                  --master-user-password {master_password} \
                  --publicly-accessible"""
    run_command(command)

def create_db_instance(instance_id, cluster_id):
    command = f"""aws rds create-db-instance \
                  --db-instance-identifier {instance_id} \
                  --db-cluster-identifier {cluster_id} \
                  --engine aurora-postgresql \
                  --db-instance-class db.r5.large \
                  --publicly-accessible"""
    run_command(command)

def main():
    cluster_identifier = "your-cluster-identifier"
    master_username = "masteruser"
    master_password = "masteruserpassword"
    
    instance_identifier = "your-instance-identifier"
    
    create_aurora_postgres_cluster(cluster_identifier, master_username, master_password)
    create_db_instance(instance_identifier, cluster_identifier)

if __name__ == "__main__":
    main()
