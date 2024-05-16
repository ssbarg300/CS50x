-- Keep a log of any SQL queries you execute as you solve the mystery.
-- look at the crime scene report:
SELECT * FROM crime_scene_reports WHERE month = 7 AND day = 28
AND street = "Humphrey Street";

--Check bakery sequrity logs!
SELECT * FROM bakery_security_logs
WHERE month = 7 AND day = 28 AND hour = 10;

-- see interviews
SELECT * FROM interviews WHERE month = 7 AND day = 28;

SELECT * FROM phone_calls where month = 7 and day = 28;

-- atm transactions.
SELECT * FROM atm_transactions WHERE month = 7
AND day = 28 AND atm_location = "Leggett Street";


-- check phone calls for person with this id
SELECT * FROM phone_calls WHERE month = 7 AND day = 28 AND id = 264;

--check for bank account
--SELECT * FROM bank_accounts WHERE account_name;

-- look for his name
SELECT * FROM people WHERE id = 686048;

--get flight id
SELECT * FROM passengers WHERE passport_number = 5773159633;

--check flights
SELECT * FROM flights WHERE id = 36;

-- origin flight is from fiftyville
SELECT * FROM airports WHERE id = 8;

--second guys destination is new york?
SELECT * FROM airports WHERE id = 4;


-- another way of searching
 SELECT id,name FROM people
 JOIN bank_accounts ON people.id = person_id
 WHERE account_number IN (SELECT account_number FROM atm_transactions
 WHERE day = 28 AND month = 7  AND year = 2021 AND atm_location= "Leggett Street");



-- i used this but i dont remember where lol.
SELECT * FROM people WHERE phone_number = "(375) 555-8161";
SELECT * FROM phone_calls WHERE month = 7 AND day = 28 AND caller = "(367) 555-5533";
SELECT * FROM phone_calls WHERE month = 7 AND day = 28;
SELECT * FROM people WHERE id = 686048;