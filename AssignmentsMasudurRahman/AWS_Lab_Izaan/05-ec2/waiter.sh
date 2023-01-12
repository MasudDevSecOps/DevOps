#!/bin/bash

aws cloudformation create-stack --stack-name ec2lab5 --template-body file://ec2Lab.yaml

aws cloudformation wait stack-create-complete --stack-name ec2lab5

aws cloudformation describe-stack-resources --stack-name ec2lab5


aws cloudformation update-stack --stack-name ec2lab5 --template-body file://update-ec2lab5.yaml --parameters file://updateec2parameter.json

aws cloudformation validate-template --template-body file://update-ec2lab5.yaml