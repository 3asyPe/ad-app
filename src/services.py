import requests 

from app import db
from models import User, SDK


def get_xml():
    response = requests.get("https://6u3td6zfza.execute-api.us-east-2.amazonaws.com/prod/ad/vast")
    xml = response.content
    return xml


def get_or_create_user_by_name(name) -> User:
    user = User.query.filter_by(name=name).first()
    if user is None:
        user = User(name=name)
        db.session.add(user)
        db.session.commit()
    return user


def get_or_create_sdk_by_version(version) -> SDK:
    sdk = SDK.query.filter_by(version=version).first()
    if sdk is None:
        sdk = SDK(version=version)
        db.session.add(sdk)
        db.session.commit()
    return sdk


def create_ad_request(user_name: str, sdk_version: str):
    user = get_or_create_user_by_name(name=user_name)
    sdk = get_or_create_sdk_by_version(version=sdk_version)

    user.ad_requests += 1
    sdk.ad_requests += 1
    db.session.commit()


def create_impression(user_name: str, sdk_version: str):
    user = get_or_create_user_by_name(name=user_name)
    sdk = get_or_create_sdk_by_version(version=sdk_version)

    user.impressions += 1
    sdk.impressions += 1
    db.session.commit()


def get_stats(filter_type: str) -> dict:
    if filter_type == "user":
        objects = User.query.all()
    elif filter_type == "sdk_version":
        objects = SDK.query.all()
    else:
        raise ValueError()
    
    ad_requests = 0
    impressions = 0

    for obj in objects:
        ad_requests += obj.ad_requests
        impressions += obj.impressions

    divider = len(objects)

    if divider == 0:
        ad_requests_stats = 0
        impressions_stats = 0
        fill_rate_stats = 0
    else:
        ad_requests_stats = ad_requests / divider
        impressions_stats = impressions / divider
        fill_rate_stats = impressions / divider if ad_requests == 0 else impressions / ad_requests/ divider

    return {
        f"ad_requests_per_{filter_type}": ad_requests_stats,
        f"impressions_per_{filter_type}": impressions_stats,
        "fill_rate": fill_rate_stats,
    }
