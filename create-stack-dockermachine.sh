
VPC_ID=`aws ec2 describe-vpcs --filter Name=tag:Name,Values=Default --query Vpcs[].VpcId --output text`

SUBNET_ID=`aws ec2 describe-subnets --filters "Name=vpc-id,Values=vpc-07e679b7de3c03503" --filters "Name=tag:Name,Values=Default" --query Subnets[].SubnetId --output text`

echo 'VPC ID is = '$VPC_ID
echo 'Subnet ID is = '$SUBNET_ID
aws cloudformation create-stack --stack-name docker-machine \
  --template-body file://cf-slave.yaml --parameters ParameterKey=Key,ParameterValue=vcjain-aws ParameterKey=Subnet,ParameterValue=$SUBNET_ID ParameterKey=VPC,ParameterValue=$VPC_ID
