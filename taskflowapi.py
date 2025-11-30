from airflow import DAG
from airflow.decorators import task
from datetime import datetime

"""
Apache Airflow TaskFlow API DAG for a math sequence:
1. Start with 10
2. Add 5
3. Multiply by 2
4. Subtract 3
5. Square the result
"""

with DAG(
    dag_id='math_sequence_dag_with_taskflow',
    start_date=datetime(2023, 1, 1),
    schedule=None,  # Run once
    catchup=False,
) as dag:

    @task
    def start_number():
        initial_value = 10
        print(f"Starting number: {initial_value}")
        return initial_value

    @task
    def add_five(number):
        new_value = number + 5
        print(f"Add 5: {number} + 5 = {new_value}")
        return new_value

    @task
    def multiply_by_two(number):
        new_value = number * 2
        print(f"Multiply by 2: {number} * 2 = {new_value}")
        return new_value

    @task
    def subtract_three(number):
        new_value = number - 3
        print(f"Subtract 3: {number} - 3 = {new_value}")
        return new_value

    @task
    def square_number(number):
        new_value = number ** 2
        print(f"Square the result: {number}^2 = {new_value}")
        return new_value

    # ----------------------
    # Define TaskFlow dependencies
    # ----------------------
    start_value = start_number()
    added_value = add_five(start_value)
    multiplied_value = multiply_by_two(added_value)
    subtracted_value = subtract_three(multiplied_value)
    square_value = square_number(subtracted_value)
