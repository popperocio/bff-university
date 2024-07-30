import json
from http import HTTPStatus
from unittest.mock import AsyncMock, MagicMock

import pytest

from adapters.src.repositories import RapidApiRepository
from core.src.utils.status_codes import HttpStatus


@pytest.fixture
def set_up_rapid_api_instance():
    mock_client = AsyncMock()
    mock_response = MagicMock()
    mock_response.status_code = HttpStatus.OK
    mock_response.text = json.dumps(
        {
            "getSharedBOF2.Downloads.Hotel.Hotels": {
                "results": {
                    "status": "Success",
                    "status_code": 100,
                    "resume_key": "_CItR_Y_ZEPRoNSfx5-a3k9Qy8-P1q72n8NebxZFRaREpTzh0zP-ESnpOSdnhKVNKz1cTrLftmFu-YmXzK4Z1qQUAixXFAmHclw_81aS5yNo",  # noqa: E501
                    "hotels": {
                        "hotel_0": {
                            "hotelid_ppn": "700000000",
                            "hotelid_a": None,
                            "hotelid_b": "10003",
                            "hotelid_t": "4125705",
                            "hotel_type": "Hotel",
                            "property_type_id": "14",
                            "hotel_name": "Hotel Asterisk a family run hotel",
                            "hotel_address": "Den Texstraat 16",
                            "city": "Amsterdam",
                            "property_description": "L’Hotel Asterisk a family run hotel...",
                            "cityid_ppn": "800020723",
                            "state": None,
                            "state_code": None,
                            "country": "Netherlands",
                            "country_code": "NL",
                            "latitude": "52.358798980713",
                            "longitude": "4.8934597969055",
                            "area_id": "8282",
                            "postal_code": "1017 ZA",
                            "star_rating": "3.5",
                            "low_rate": "0",
                            "currency_code": "EUR",
                            "review_rating": 8.7,
                            "review_count": 210,
                            "rank_score_ppn": None,
                            "chain_id_ppn": "274",
                            "thumbnail": "//mobileimg.priceline.com/htlimg/41/4125705/thumbnail-150-square.jpg",  # noqa: E501
                            "has_photos": "1",
                            "room_count": "40",
                            "check_in": "15:00",
                            "check_out": "11:00",
                            "amenity_codes": "17^27^51^113^138^148^154^198^510^1062^1530^1763^1974^2449^2452^2472^2562^2602^2622^2662^2732^3622^4172^5641^5911^5941^6211^6221^9481^9491",  # noqa: E501
                            "hotel_sort_score_ppn": "0.616715",
                            "creation_date_time": "2012-01-23 00:00:00",
                            "last_changed_date": "2024-06-07",
                            "standard_check_in": "1",
                            "active": "1",
                            "agd_flag": "0",
                            "bkg_flag": "1",
                            "mer_flag": "1",
                            "smop_flag": "1",
                        },
                        "hotel_1": {
                            "hotelid_ppn": "700000001",
                            "hotelid_a": None,
                            "hotelid_b": "10004",
                            "hotelid_t": "529803",
                            "hotel_type": "Hotel",
                            "property_type_id": "14",
                            "hotel_name": "The Pavilions Amsterdam The Toren",
                            "hotel_address": "Keizersgracht 164",
                            "city": "Amsterdam",
                            "property_description": "L’élégant hôtel The Pavilions Amsterdam The Toren vous accueille le long du célèbre canal Keizersgracht...",  # noqa: E501
                            "cityid_ppn": "800020723",
                            "state": None,
                            "state_code": None,
                            "country": "Netherlands",
                            "country_code": "NL",
                            "latitude": "52.375801086426",
                            "longitude": "4.8858327865601",
                            "area_id": "8297",
                            "postal_code": "1015 CZ",
                            "star_rating": "4",
                            "low_rate": "0",
                            "currency_code": "EUR",
                            "review_rating": 8.9,
                            "review_count": 214,
                            "rank_score_ppn": None,
                            "chain_id_ppn": "417",
                            "thumbnail": "//mobileimg.priceline.com/htlimg/52/529803/thumbnail-150-square.jpg",  # noqa: E501
                            "has_photos": "1",
                            "room_count": "40",
                            "check_in": "15:00",
                            "check_out": "12:00",
                            "amenity_codes": "17^26^27^38^39^40^47^51^111^113^114^130^220^480^510^654^1062^1530^1961^1974^1976^1992^2437^2449^2452^2472^2562^2602^2622^2662^2712^2732^2752^3082^3642^4172^4511^5031^5631^5641^5681^5821^5831^5841^5911^5941^5971^6121^6211^6221^9231^9471^9481^9511",  # noqa: E501
                            "hotel_sort_score_ppn": "0.621758",
                            "creation_date_time": "2012-01-23 00:00:00",
                            "last_changed_date": "2024-06-07",
                            "standard_check_in": "1",
                            "active": "1",
                            "agd_flag": "0",
                            "bkg_flag": "1",
                            "mer_flag": "0",
                            "smop_flag": "0",
                        },
                    },
                    "csv": 'hotelid_ppn,hotelid_a,hotelid_b,hotelid_t,hotel_type,property_type_id,hotel_name,hotel_address,city,property_description,cityid_ppn,state,state_code,country,country_code,latitude,longitude,area_id,postal_code,star_rating,low_rate,currency_code,review_rating,review_count,rank_score_ppn,chain_id_ppn,thumbnail,has_photos,room_count,check_in,check_out,amenity_codes,hotel_sort_score_ppn,creation_date_time,last_changed_date,standard_check_in,active,agd_flag,bkg_flag,mer_flag,smop_flag\n700000000,,10003,4125705,Hotel,14,"Hotel Asterisk a family run hotel","Den Texstraat 16",Amsterdam,"L’Hotel Asterisk a family run hotel occupe 2 bâtiments restaurés datant du XIXe siècle...",800020723,,,Netherlands,NL,52.358798980713,4.8934597969055,8282,"1017 ZA",3.5,0,EUR,8.7,210,,274,//mobileimg.priceline.com/htlimg/41/4125705/thumbnail-150-square.jpg,1,40,15:00,11:00,17^27^51^113^138^148^154^198^510^1062^1530^1763^1974^2449^2452^2472^2562^2602^2622^2662^2732^3622^4172^5641^5911^5941^6211^6221^9481^9491,0.616715,"2012-01-23 00:00:00",2024-06-07,1,1,0,1,1,1\n700000001,,10004,529803,Hotel,14,"The Pavilions Amsterdam The Toren","Keizersgracht 164",Amsterdam,"L’élégant hôtel The Pavilions Amsterdam The Toren vous accueille le long du célèbre canal Keizersgracht...",800020723,,,Netherlands,NL,52.375801086426,4.8858327865601,8297,"1015 CZ",4,0,EUR,8.9,214,,417,//mobileimg.priceline.com/htlimg/52/529803/thumbnail-150-square.jpg,1,40,15:00,12:00,17^26^27^38^39^40^47^51^111^113^114^130^220^480^510^654^1062^1530^1961^1974^1976^1992^2437^2449^2452^2472^2562^2602^2622^2662^2712^2732^2752^3082^3642^4172^4511^5031^5631^5641^5681^5821^5831^5841^5911^5941^5971^6121^6211^6221^9231^9471^9481^9511,0.621758,"2012-01-23 00:00:00",2024-06-07,1,1,0,0,0,0',  # noqa: E501
                }
            }
        }
    )
    mock_client.get = AsyncMock(return_value=mock_response)
    rapid_api_repository = RapidApiRepository(
        client=lambda base_url, default_headers: mock_client,
        rapid_api_url="http://mockapi.com",
        rapid_api_key="mockkey",
        rapid_api_host="mockhost",
    )

    return rapid_api_repository


@pytest.fixture
def set_up_rapid_api_instance_server_error():
    mock_client = AsyncMock()

    mock_response = MagicMock()
    mock_response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
    mock_response.text = "Internal Server Error"
    mock_client.get = AsyncMock(return_value=mock_response)

    rapid_api_repository = RapidApiRepository(
        client=lambda base_url, default_headers: mock_client,
        rapid_api_url="http://mockapi.com",
        rapid_api_key="mockkey",
        rapid_api_host="mockhost",
    )

    return rapid_api_repository


@pytest.fixture
def set_up_rapid_api_instance_400():
    mock_client = AsyncMock()

    mock_response = MagicMock()
    mock_response.status_code = HTTPStatus.BAD_REQUEST
    mock_response.text = "Bad Request"
    mock_client.get = AsyncMock(return_value=mock_response)

    rapid_api_repository = RapidApiRepository(
        client=lambda base_url, default_headers: mock_client,
        rapid_api_url="http://mockapi.com",
        rapid_api_key="mockkey",
        rapid_api_host="mockhost",
    )

    return rapid_api_repository
