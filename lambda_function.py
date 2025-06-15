import os
import boto3

ENV = os.environ.get("ENV", "dev")

region_name = "us-west-2"  # update with actual region name throughout repo

this_project = "project_name"  # update with actual project_name throughout repo

cluster = "cluster_name"  # update with cluster name to use on AWS

subnets = ["subnet-1", "subnet-2", "subnet-3"]  # update with subnet ids to use on AWS

security_groups = ["sg-1"]  # update with security group ids to use on AWS

ecs = boto3.client("ecs", region_name=region_name)

latest_version = (
    ecs.describe_task_definition(taskDefinition=this_project)
    .get("taskDefinition")
    .get("revision")
)


def trigger_fargate_task():

    response = ecs.run_task(
        taskDefinition=f"{this_project}:{latest_version}",
        cluster=cluster,
        launchType="FARGATE",
        count=1,
        platformVersion="LATEST",
        enableECSManagedTags=False,
        networkConfiguration={
            "awsvpcConfiguration": {
                "subnets": subnets,
                "securityGroups": security_groups,
                "assignPublicIp": "ENABLED",
            }
        },
    )

    task_id = response.get("tasks")[0].get("taskArn").split("/")[-1]
    print(
        f"Task ID: {task_id}. Task link: https://console.aws.amazon.com/ecs/home?region={region_name}#/clusters/{cluster}/tasks/{task_id}/details"
    )


def lambda_handler(event, context):
    trigger_fargate_task()


if __name__ == "__main__":
    lambda_handler()
