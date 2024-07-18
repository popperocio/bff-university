provider "aws" {
    region                  = "us-east-1"
    access_key              = "test"
    secret_key              = "test"
    skip_credentials_validation = true
    skip_metadata_api_check     = true
    skip_requesting_account_id  = true
    endpoints {
        apigateway = "http://localstack:4566"
        s3 = "http://localhost:4566"
    }
}

resource "aws_api_gateway_rest_api" "example" {
  name = "example"
  # CORS configuration
  policy = <<EOF
  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Action": "execute-api:Invoke",
        "Resource": "arn:aws:execute-api:*:*:*/*/*/*",
        "Principal": "*",
        "Condition": {
          "StringEquals": {
            "aws:SourceVpc": "vpc-12345678"  # Optional: restrict by VPC if needed
          }
        }
      }
    ]
  }
  EOF
}

resource "aws_s3_bucket" "test-bucket" {
  bucket = "my-bucket"
}

resource "aws_iam_role" "invocation_role" {
  name = "api_gateway_auth_invocation"
  path = "/"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": {
    "Effect": "Allow",
    "Action": "s3:ListBucket",
    "Resource": "arn:aws:s3:::test-bucket"
  }
}
EOF
}