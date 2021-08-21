# ad-app
Test application

To launch the app, please run:
docker-compose up -d --build

If you are running it for the first time, please create a database using the following command:
docker-compose exec web python src/manage.py create_db


The application has three endpoints:


GET /api/ad/get 
Required args:
user_name (String) - Name of the user who gets an ad
sdk_version (String) - Version of the SDK user is using

saves data about the ad request in the database
returns an xml taken from the external API


GET /api/impression
Required args:
user_name (String) - Name of the user who gets an ad
sdk_version (String) - Version of the SDK user is using

saves data about the impression in the database
returns 200 HTML status


GET /api/stats/get
Required args:
filter_type (user or sdk_version. Other types would raise an error) - The statistics returned will depend on the filter you provide

receives data about ad requests and impressions from the database
calculates values
returns statistics in json format in the following format:
{
    "ad_requests_per_{filter_type}": <float>,
    "impressions_per_{filter_type}": <float>,
    "fill_rate": <float>
}
