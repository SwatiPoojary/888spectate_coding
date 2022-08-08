#Files description:
For Question 1:
    Internal_Nodes.py : This file contains the code for the method
    test_Internal_Nodes.py : This file has the pytest cases

For Question 2:
    There are two packages: app and tests
    app package:
        This package contains all the development code
        app.py : Contains all the apis
        constant.py : Contains all the enums required by the application
        db.py : Contains all the db scripts
        db_helper.py : Contains methods with filtering queries
        Sportsbook.py : Contains classes for sports, events and selections
    tests package:
        test_sportsbook.py : Contains all the pytest cases for the application

#PRODUCTION READY
Dockerfile is present to dockerzie the application
build docker image using script:
    docker image build -t sportsbook-docker .
run application:
    docker run -p 5000:5000 -d sportsbook-docker

#URL description:
For Sports:
    /sports 
        POST method - to insert sports data
        sample input: 
            mock_request_data = {
                "name": "Basket ball",
                "slug": "Basket ball",
                "active": "TRUE"
            }
    /sports
        PUT method - to update sports data
        sample input:
            mock_request_data = {
                "id": 7,
                "name": "Basket ball",
                "slug": "Basket ball",
                "active": "FALSE"
            }
    /sports
        GET method - to get sports data with filter
        samples:
            '/sports'
            '/sports?id=7'
    /deactivate_sport
        GET method - to deactivate sports
        sample: '/deactivate_sport?id=7'
        
For events:
    /events 
        POST method - to insert events data
        sample input: 
               mock_request_data =  {
                "name": "Football",
                "slug": "Football",
                "active": "TRUE",
                "type": "Inplay",
                "sport_id": 6,
                "status": "Pending",
                "scheduled_start": "2022-08-21 16:30:00"
            }
    /events
        PUT method - to update events data
        sample input:
            mock_request_data = {
                    "id": 3,
                    "name": "Football",
                    "slug": "Football",
                    "active": "TRUE",
                    "type": "Inplay",
                    "sport_id": 6,
                    "status": "Pending",
                    "scheduled_start": "2022-08-21 16:30:00",
                    "actual_start": "2022-08-21 16:30:00"
                }
    /events
        GET method - to get events data with filter
        samples:
            '/events'
            '/events?id=3'
    /deactivate_event
        GET method - to deactivate events
        sample: '/deactivate_event?id=3'

For selections:
    /selections 
        POST method - to insert selections data
        sample input: 
                mock_request_data = {
                    "name":"Football",
                    "event_id":1,
                    "price":"2.00",
                    "active":"FALSE",
                    "outcome":"Unsettled"
                }
    /selections
        PUT method - to update selections data
        sample input:
            mock_request_data = {
                "id":1,
                "name":"Football",
                "event_id":1,
                "price":"2.00",
                "active":"FALSE",
                "outcome":"Unsettled"
            }
    /selections
        GET method - to get selections data with filter
        samples:
            '/selections'
            '/selections?id=1'
    /deactivate_selection
        GET method - to deactivate selections
        sample: '/deactivate_selection?id=3'