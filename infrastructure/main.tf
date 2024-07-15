provider "aws" {
    region                  = "us-east-1"
    access_key              = "test"
    secret_key              = "test"
    skip_credentials_validation = true
    skip_metadata_api_check     = true
    skip_requesting_account_id  = true
    endpoints {
        apigateway = "http://localstack:4566"
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
