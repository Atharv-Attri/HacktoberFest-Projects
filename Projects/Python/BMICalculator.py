CREATE PROCEDURE checkJourney (IN booking  int, IN ticket int) \   
BEGIN \
DECLARE A CURSOR WITH RETURN FOR \
	SELECT c.cust_name, b.booking_id, t.ticket_id, s.sche_date, s.sche_time, a.bus_plate, r.route_dep, r.route_arr \
	FROM booking b \
	JOIN ticket t \
	ON b.booking_id = t.booking_id \
	JOIN schedule s \
	ON s.sche_id = t.sche_id \
	JOIN bus a \
	ON s.bus_id = a.bus_id \
	JOIN route r \
	ON s.route_id = r.route_id \
	JOIN customer c \
	ON c.cust_id = b. cust_id \
	WHERE t.ticket_id = ticket  \
	AND b.booking_id = booking ; \
OPEN A; \
END