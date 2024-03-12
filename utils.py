import json
from boto3.session import Session
from botocore.exceptions import ClientError
from typing import List
from pydantic import BaseModel, validator

class AwsConfig:
    def __init__(self) -> None:
        self.session: Session = Session(region_name="us-east-1")

    def get_secret_aws(self, secret_name: str) -> List[str]:

        try:
            response = self.session(service_name="secretmanager").get_secret_value(
                SecretId=secret_name
            )   

        except ClientError as error:
            raise (error)

        response = json.loads(response["SecretString"])

        return response
        


class City(BaseModel):
    city: str


    @validator('city')
    def capitalize_city(cls, value: str):
       
        new_value = value.capitalize()

        return new_value
        

class CityInfo(BaseModel):
    lat: str
    lng: str


class Config:
    AWS_CONFIG = AwsConfig()
   
