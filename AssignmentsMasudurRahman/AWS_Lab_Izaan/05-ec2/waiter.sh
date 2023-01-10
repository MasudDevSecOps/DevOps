#!/bin/bash

aws cloudformation create-stack --stack-name ec2lab5 --template-body file://ec2Lab.yaml

aws cloudformation wait stack-create-complete --stack-name ec2lab5

aws cloudformation describe-stack-resources --stack-name ec2lab5