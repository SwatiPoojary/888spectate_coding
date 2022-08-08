from datetime import datetime
from flask import Flask, request, jsonify

from app.Sportsbook import Sport, Selection, Event
from app.constant import *
from app.db import DB

app = Flask(__name__)


#
# def configure_routes():
#     # SPORTS

@app.route('/sports', methods=['POST', 'PUT'])
def create_sports():
    try:
        request_data = request.get_json()
        data_missing = False
        message = 'Some fields are missing:'
        if request_data is not None and len(request_data) > 0:
            if 'name' in request_data:
                name = request_data['name']
            else:
                data_missing = True
                message += ' ,name '
                name = ''

            if 'slug' in request_data:
                slug = request_data['slug']
            else:
                data_missing = True
                message += ' ,slug '
                slug = ''

            if 'active' in request_data:
                active = request_data['active']
                active_values = [member.value for member in Active]
                if active not in active_values:
                    data = {"message": "Active Field should be either TRUE or FALSE "}
                    return jsonify(data), 400

            else:
                active = 'TRUE'
        else:
            data = {"message": "No sports data for saving!! "}
            return jsonify(data), 400

        if data_missing:
            data = {"message": message}
            return jsonify(data), 400

        sport = Sport(name, slug, active)
        db = DB()
        db.create_sport_table()
        data = {"message": ""}
        if request.method == 'POST':
            inserted_id = db.insert_sports(sport)
            print('Sport created with id: ', str(inserted_id))
            data = {"message": "Sport created with id: " + str(inserted_id)}
        elif request.method == 'PUT':
            if 'id' in request_data:
                sport_id = request_data['id']
            else:
                data = {"message": "No id provided for updating sports!!"}
                return jsonify(data), 400
            sport.set_id(sport_id)
            updated_id = db.update_sports(sport)
            print('Sport updated with id: ', str(updated_id))
            data = {"message": "Sport updated with id: " + str(updated_id)}

        db.close_connection()
        return jsonify(data), 200

    except Exception as ex:
        print('Some exception occurred while storing sports: ', ex)
        return jsonify({'message': 'Something went wrong!!'}), 400


@app.route('/sports', methods=['GET'])
def get_sports():
    try:
        sports = []
        request_data = request.args
        request_data = request_data.to_dict()
        filters = {}
        if request_data is not None:
            filters = request_data

        db = DB()
        rows = db.get_filtered_sports(filters)
        if rows is not None:
            for row in rows:
                sport = {
                    'name': row['name'],
                    'slug': row['slug'],
                    'active': row['active']
                }
                sports.append(sport)

        db.close_connection()
        if sports is not None and len(sports) > 0:
            return jsonify(sports)
        else:
            return jsonify({'message': 'No available sports !!'}), 200

    except Exception as ex:
        print('Some exception occurred while fetching sports: ', ex)
        return jsonify({'message': 'Something went wrong!!'}), 400


@app.route('/deactivate_sport', methods=['GET'])
def deactivate_sport():
    try:
        request_data = request.args
        request_data = request_data.to_dict()
        if request_data is not None and 'id' in request_data:
            sport_id = request_data['id']
        else:
            return jsonify({'message': 'No id provided for deactivating sport !!'}), 400

        db = DB()
        db.deactivate_sports(sport_id)
        return jsonify({'message': 'Sport deactivated !!'}), 200

    except Exception as ex:
        print('Some exception occurred while deactivating sports: ', ex)
        return jsonify({'message': 'Something went wrong!!'}), 400


# EVENTS
@app.route('/events', methods=['POST', 'PUT'])
def create_events():
    try:
        request_data = request.get_json()
        data_missing = False
        message = 'Some fields are missing:'
        if request_data is not None:
            if 'name' in request_data:
                name = request_data['name']
            else:
                data_missing = True
                message += ' ,name '
                name = ''

            if 'slug' in request_data:
                slug = request_data['slug']
            else:
                data_missing = True
                message += ' ,slug '
                slug = ''

            if 'active' in request_data:
                active = request_data['active']
                active_values = [member.value for member in Active]
                if active not in active_values:
                    data = {"message": "Active Field should be either TRUE or FALSE "}
                    return jsonify(data), 400
            else:
                active = 'TRUE'

            if 'type' in request_data:
                event_type = request_data['type']
                type_values = [member.value for member in Event_Type]
                if event_type not in type_values:
                    data = {"message": "Event Type Field should be either Preplay or Inplay "}
                    return jsonify(data), 400
            else:
                data_missing = True
                message += ' ,type '
                event_type = ''

            if 'sport_id' in request_data:
                sport_id = request_data['sport_id']
            else:
                data_missing = True
                message += ' ,sport_id '
                sport_id = 0

            if 'status' in request_data:
                status = request_data['status']
                status_values = [member.value for member in Status]
                if status not in status_values:
                    data = {
                        "message": "Status Type Field should be one of the value: [Pending, Started, Ended or "
                                   "Cancelled]"}
                    return jsonify(data), 400
            else:
                status = 'Pending'

            if 'scheduled_start' in request_data:
                scheduled_start = request_data['scheduled_start']
                scheduled_start = datetime.strptime(scheduled_start, '%Y-%m-%d %H:%M:%S')
            else:
                data_missing = True
                message += ' ,scheduled_start '
                scheduled_start = ''

            if 'actual_start' in request_data:
                actual_start = request_data['actual_start']
                actual_start = datetime.strptime(actual_start, '%Y-%m-%d %H:%M:%S')
            else:
                actual_start = None
        else:
            data = {"message": "No events data for saving!! "}, 400
            return jsonify(data), 200

        if data_missing:
            data = {"message": message}
            return jsonify(data), 400

        event = Event(name, slug, active, event_type, sport_id, status, scheduled_start, actual_start)
        db = DB()
        db.create_event_table()
        data = {"message": ""}
        if request.method == 'POST':
            sports_filter = {'id': sport_id}
            sports = db.get_filtered_sports(sports_filter)
            print(sports)
            if sports is None or len(sports) == 0:
                data = {"message": "No active sports present for the sport id provided!!"}
                return jsonify(data), 400
            inserted_id = db.insert_event(event)
            print('Event created with id: ', str(inserted_id))
            data = {"message": "Event created with id: " + str(inserted_id)}
        elif request.method == 'PUT':
            if 'id' in request_data:
                event_id = request_data['id']
            else:
                data = {"message": "No id provided for updating events!"}
                return jsonify(data), 400
            event.set_id(event_id)
            updated_id = db.update_event(event)

            if sport_id != 0:
                sport_filter = {'Sport_id': str(sport_id)}
                sport_rows = db.get_filtered_events(sport_filter)
                sport_length = len(sport_rows)
            else:
                filters = {'id': str(updated_id)}
                update_row = db.get_filtered_events(filters)
                for row in update_row:
                    sport_id = row['Sport_id']
                sport_filter = {'Sport_id': str(sport_id)}
                sport_rows = db.get_filtered_events(sport_filter)
                sport_length = len(sport_rows)

            if sport_length == 0:
                db.deactivate_sports(sport_id)

            print('Event updated with id: ', str(updated_id))
            data = {"message": "Event updated with id: " + str(updated_id)}
        db.close_connection()
        return jsonify(data), 200

    except Exception as ex:
        print('Some exception occurred while storing events: ', ex)
        return jsonify({'message': 'Something went wrong!!'}), 400


@app.route('/events', methods=['GET'])
def get_events():
    try:
        events = []
        request_data = request.args
        request_data = request_data.to_dict()
        filters = {}
        if request_data is not None:
            filters = request_data

        db = DB()
        rows = db.get_filtered_events(filters)
        if rows is not None:
            for row in rows:
                event = {
                    'id': row['id'],
                    'name': row['name'],
                    'slug': row['slug'],
                    'active': row['active'],
                    'type': row['type'],
                    'sport_id': row['sport_id'],
                    'status': row['status'],
                    'scheduled_start': row['scheduled_start'],
                    'actual_start': row['actual_start']
                }
                events.append(event)

        db.close_connection()
        if events is not None and len(events) > 0:
            return jsonify(events)
        else:
            return jsonify({'message': 'No available events !!'}), 200

    except Exception as ex:
        print('Some exception occurred while fetching events: ', ex)
        return jsonify({'message': 'Something went wrong!!'}), 400


@app.route('/deactivate_event', methods=['GET'])
def deactivate_event():
    try:
        request_data = request.args
        request_data = request_data.to_dict()
        if request_data is not None and 'id' in request_data:
            event_id = request_data['id']
        else:
            return jsonify({'message': 'No id provided for deactivating events !!'}), 400

        db = DB()
        db.deactivate_event(event_id)
        return jsonify({'message': 'Event deactivated !!'}), 200

    except Exception as ex:
        print('Some exception occurred while deactivating events: ', ex)
        return jsonify({'message': 'Something went wrong!!'}), 400


# SELECTIONS

@app.route('/selections', methods=['POST', 'PUT'])
def create_selection():
    try:
        request_data = request.get_json()
        data_missing = False
        message = 'Some fields are missing:'
        if request_data is not None:
            if 'name' in request_data:
                name = request_data['name']
            else:
                data_missing = True
                message += ' ,name '
                name = ''

            if 'event_id' in request_data:
                event_id = request_data['event_id']
            else:
                data_missing = True
                message += ' ,event_id '
                event_id = 0

            if 'price' in request_data:
                price = request_data['price']
            else:
                data_missing = True
                message += ' ,price '
                price = 0

            if 'active' in request_data:
                active = request_data['active']
                active_values = [member.value for member in Active]
                if active not in active_values:
                    data = {"message": "Active Field should be either TRUE or FALSE "}
                    return jsonify(data), 400
            else:
                active = 'TRUE'

            if 'outcome' in request_data:
                outcome = request_data['outcome']
                outcome_values = [member.value for member in Outcome]
                if outcome not in outcome_values:
                    data = {"message": "Outcome Field should be one of the following: [Unsettled, Void, Lose or Win] "}
                    return jsonify(data), 400
            else:
                outcome = 'Unsettled'
        else:
            data = {"message": "No selections data for saving!! "}, 400
            return jsonify(data), 200

        if data_missing:
            data = {"message": message}
            return jsonify(data), 400

        selection = Selection(name, event_id, price, active, outcome)
        db = DB()
        db.create_selection_table()
        data = {"message": ""}
        if request.method == 'POST':
            event_filter = {'id': event_id}
            events = db.get_filtered_events(event_filter)
            if events is None or len(events) == 0:
                data = {"message": "No active events present for the event id provided!!"}
                return jsonify(data), 400
            inserted_id = db.insert_selection(selection)
            print('Selection created with id: ', inserted_id)
            data = {"message": "Selection created with id: " + str(inserted_id)}
        elif request.method == 'PUT':
            if 'id' in request_data:
                selection_id = request_data['id']
            else:
                data = {"message": "No id provided for updating selection!!"}
                return jsonify(data), 400
            selection.set_id(selection_id)
            updated_id = db.update_selection(selection)
            if event_id != 0:
                event_filter = {'event_id': str(event_id)}
                event_rows = db.get_filtered_selections(event_filter)
                print('after filter')
                event_length = len(event_rows)
            else:
                filters = {'id': str(updated_id)}
                update_row = db.get_filtered_selections(filters)
                for row in update_row:
                    event_id = row['Event_id']
                event_filter = {'event_id': str(event_id)}
                event_rows = db.get_filtered_selections(event_filter)
                event_length = len(event_rows)
            print(event_length)
            if event_length == 0:
                print(event_id)
                event_filter['id'] = str(event_id)
                event_filter['active'] = "('TRUE','FALSE')"
                event_rows = db.get_filtered_events(event_filter)
                sport_id = 0
                for row in event_rows:
                    if row['id'] == event_id:
                        sport_id = row['Sport_id']
                        break
                print(sport_id)
                db.deactivate_event(event_id)
                db.deactivate_sports(sport_id)

            print('Selection updated with id: ', updated_id)
            data = {"message": "Selection update with id: " + str(updated_id)}

        db.close_connection()
        return jsonify(data), 200

    except Exception as ex:
        print('Some exception occurred while storing selections: ', ex)
        return jsonify({'message': 'Something went wrong!!'}), 400


@app.route('/selections', methods=['GET'])
def get_selections():
    try:
        selections = []
        request_data = request.args
        request_data = request_data.to_dict()
        filters = {}
        if request_data is not None:
            filters = request_data

        db = DB()
        rows = db.get_filtered_selections(filters)
        if rows is not None:
            for row in rows:
                selection = {
                    'id': row['id'],
                    'name': row['name'],
                    'event_id': row['event_id'],
                    'price': row['price'],
                    'active': row['active'],
                    'outcome': row['outcome']
                }
                selections.append(selection)

        db.close_connection()
        if selections is not None and len(selections) > 0:
            return jsonify(selections)
        else:
            return jsonify({'message': 'No available selections !!'}), 200

    except Exception as ex:
        print('Some exception occurred while fetching selections: ', ex)
        return jsonify({'message': 'Something went wrong!!'}), 400


@app.route('/deactivate_selection', methods=['GET'])
def deactivate_selection():
    try:
        request_data = request.args
        request_data = request_data.to_dict()
        if request_data is not None and 'id' in request_data:
            selection_id = request_data['id']
        else:
            return jsonify({'message': 'No id provided for deactivating selections !!'}), 400

        db = DB()
        db.deactivate_selection(selection_id)
        return jsonify({'message': 'Selection deactivated !!'}), 200

    except Exception as ex:
        print('Some exception occurred while deactivating selections: ', ex)
        return jsonify({'message': 'Something went wrong!!'}), 400


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
