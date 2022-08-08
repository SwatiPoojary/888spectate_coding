from datetime import datetime

import pytz


def getUTCtime(time, timezone):
    try:
        time = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
        tz = pytz.timezone(timezone)
        tb = tz.localize(time)
        utc_time = tz.normalize(tb).astimezone(pytz.utc)
        return utc_time
    except Exception as ex:
        print("Exception occurred while converting to utc time:", ex)
        return None


def make_sports_filter(filters):
    try:
        sports_filter = " "
        if filters is not None:
            if 'active' in filters:
                sports_filter += " WHERE  sport.Active IN " + filters['active']
            else:
                sports_filter += " WHERE  sport.Active ='TRUE'"

            if 'id' in filters:
                sports_filter += " AND sport.id =" + str(filters['id'])
            if 'name' in filters:
                sports_filter += " AND sport.Name LIKE '%" + filters['name'] + "%'"
            if 'slug' in filters:
                sports_filter += " AND sport.Slug LIKE '%" + filters['slug'] + "%'"
            if 'min_event' in filters:
                sports_filter += "AND (SELECT count(1) FROM EVENT AS event where event.Active='TRUE' AND " \
                                 "event.Sport_id = sport.id) >= " + filters['min_event']
            if 'max_event' in filters:
                sports_filter += "AND (SELECT count(1) FROM EVENT AS event where event.Active='TRUE' AND " \
                                 "event.Sport_id = sport.id) <= " + filters['max_event']
            if 'equal_event' in filters:
                sports_filter += "AND (SELECT count(1) FROM EVENT AS event where event.Active='TRUE' AND " \
                                 "event.Sport_id = sport.id) = " + filters['equal_event']
        else:
            sports_filter += " WHERE  sport.Active ='TRUE'"
        return sports_filter

    except Exception as ex:
        print("Exception occurred while making sports filter:", ex)
        return None


def make_events_filter(filters):
    try:
        events_filter = " "
        if filters is not None:
            if 'active' in filters:
                events_filter += " WHERE  event.Active IN " + filters['active']
            else:
                events_filter += " WHERE  event.Active ='TRUE'"
            if 'id' in filters:
                events_filter += " AND event.id =" + str(filters['id'])
            if 'name' in filters:
                events_filter += " AND event.Name LIKE '%" + filters['name'] + "%'"
            if 'slug' in filters:
                events_filter += " AND event.Slug LIKE '%" + filters['slug'] + "%'"
            if 'type' in filters:
                events_filter += " AND event.Type ='" + filters['type'] + "'"
            if 'status' in filters:
                events_filter += " AND event.Status ='" + filters['status'] + "'"
            if 'sport_id' in filters:
                events_filter += " AND event.Sport_id =" + filters['sport_id']
            if 'min_selection' in filters:
                events_filter += "AND (SELECT count(1) FROM SELECTION AS selection where selection.Active='TRUE' AND " \
                                 "selection.Event_id = event.id) >= " + filters['min_selection']
            if 'max_selection' in filters:
                events_filter += "AND (SELECT count(1) FROM SELECTION AS selection where selection.Active='TRUE' AND " \
                                 "selection.Event_id = event.id) <= " + filters['max_selection']
            if 'equal_selection' in filters:
                events_filter += "AND (SELECT count(1) FROM SELECTION AS selection where selection.Active='TRUE' AND " \
                                 "selection.Event_id = event.id) = " + filters['equal_selection']

            timezone = ''
            if 'timezone' in filters:
                timezone = filters['timezone']
            if 'scheduled_start_gt' in filters and 'scheduled_start_lt' in filters:
                print('inside both')
                if timezone != '':
                    scheduled_start_gt = getUTCtime(filters['scheduled_start_gt'], timezone)
                    scheduled_start_lt = getUTCtime(filters['scheduled_start_lt'], timezone)
                else:
                    scheduled_start_gt = filters['scheduled_start_gt']
                    scheduled_start_lt = filters['scheduled_start_lt']
                print(scheduled_start_gt)
                print(scheduled_start_lt)
                events_filter += "AND event.Scheduled_start BETWEEN '" + str(scheduled_start_gt) + "' AND '" + \
                                 str(scheduled_start_lt) + "'"
            elif 'scheduled_start_gt' in filters and 'scheduled_start_lt' not in filters:
                if timezone != '':
                    scheduled_start_gt = getUTCtime(filters['scheduled_start_gt'], timezone)
                else:
                    scheduled_start_gt = filters['scheduled_start_gt']
                events_filter += "AND event.Scheduled_start >= '" + str(scheduled_start_gt) + "'"
            elif 'scheduled_start_gt' not in filters and 'scheduled_start_lt' in filters:
                if timezone != '':
                    scheduled_start_lt = getUTCtime(filters['scheduled_start_lt'], timezone)
                else:
                    scheduled_start_lt = filters['scheduled_start_lt']
                events_filter += "AND event.Scheduled_start <= '" + str(scheduled_start_lt) + "'"

            if 'actual_start_gt' in filters and 'actual_start_lt' in filters:
                if timezone != '':
                    actual_start_gt = getUTCtime(filters['actual_start_gt'], timezone)
                    actual_start_lt = getUTCtime(filters['actual_start_lt'], timezone)
                else:
                    actual_start_gt = filters['actual_start_gt']
                    actual_start_lt = filters['actual_start_lt']
                events_filter += "AND event.Actual_start BETWEEN '" + str(actual_start_gt) + "' AND '" + str(
                    actual_start_lt) + "'"
            elif 'actual_start_gt' in filters and 'actual_start_lt' not in filters:
                if timezone != '':
                    actual_start_gt = getUTCtime(filters['actual_start_gt'], timezone)
                else:
                    actual_start_gt = filters['actual_start_gt']
                events_filter += "AND event.Actual_start >= '" + str(actual_start_gt) + "'"
            elif 'actual_start_gt' not in filters and 'actual_start_lt' in filters:
                if timezone != '':
                    actual_start_lt = getUTCtime(filters['actual_start_lt'], timezone)
                else:
                    actual_start_lt = filters['actual_start_lt']
                events_filter += "AND event.Actual_start <= '" + str(actual_start_lt) + "'"
        else:
            events_filter += " WHERE  event.Active ='TRUE'"
        return events_filter

    except Exception as ex:
        print("Exception occurred while making events filter:", ex)
        return None


def make_selections_filter(filters):
    try:
        selections_filter = " "
        if filters is not None:
            if 'active' in filters:
                selections_filter += " WHERE  selection.Active IN " + filters['active']
            else:
                selections_filter += " WHERE  selection.Active ='TRUE'"
            if 'id' in filters:
                selections_filter += " AND selection.id =" + filters['id']
            if 'name' in filters:
                selections_filter += " AND selection.Name LIKE '%" + filters['name'] + "%'"
            if 'event_id' in filters:
                selections_filter += " AND selection.Event_id =" + filters['event_id']
            if 'price' in filters:
                selections_filter += " AND selection.Price =" + filters['price']
            if 'min_price' in filters:
                selections_filter += " AND selection.Price >=" + filters['min_price']
            if 'max_price' in filters:
                selections_filter += " AND selection.Price <=" + filters['max_price']
            if 'outcome' in filters:
                selections_filter += " AND selection.Outcome LIKE '%" + filters['outcome'] + "%'"
        else:
            selections_filter += " WHERE  selection.Active ='TRUE'"
        return selections_filter

    except Exception as ex:
        print("Exception occurred while making selections filter:", ex)
        return None
