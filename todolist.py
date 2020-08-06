# Write your code here
from datetime import datetime, timedelta

from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker




class task(Base):
    __tablename__ = "task"
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())


    def __repr__(self):
        return self.task

def todays_tasks():
    rows = session.query(task).filter(task.deadline == datetime.today().date()).all()
    print(f"Today {datetime.today().strftime('%d %b')}:")
    if len(rows) > 0:
        for i in range(len(rows)):
            print(str(i + 1) + ". " + rows[i].task)
        print("")
    else:
        print(f"Nothing to do!")


def weeks_tasks():
    week_itr = datetime.today()
    for i in range(7):
        rows = session.query(task).filter(task.deadline == week_itr.date()).all()
        print(week_itr.strftime('%A %d %b:'))
        if (len(rows)) > 0:
            for i in range(len(rows)):
                print(f"{i + 1}. {rows[i].task}")
            print("")
        else:
            print("Nothing to do!\n")
        week_itr += timedelta(days=1)


def all_tasks():
    rows = session.query(task).order_by(task.deadline).all()
    print("All tasks:")
    for i in range(len(rows)):
        print(f"{i + 1}. {rows[i].task}. {rows[i].deadline.strftime('%#d %b')}")
    print("")


def missed_tasks():
    rows = session.query(task).filter(task.deadline < datetime.today().date()).all()
    print("Missed tasks:")
    if len(rows) > 0:
        for i in range(len(rows)):
            print(f"{i + 1}. {rows[i].task} {rows[i].deadline.strftime('%#d %b')}")
        print("")
    else:
        print("Nothing is missed!")


def add_task():
    rows = session.query(task).order_by(task.deadline).all()
    task_str = input("Enter task\n")
    deadline_str = input("Enter deadline\n")
    deadline_date = datetime(int(deadline_str[0:4]), int(deadline_str[5:7]), int(deadline_str[8:]))
    new_task = task(id=len(rows) + 1, task=task_str, deadline=deadline_date)
    session.add(new_task)
    session.commit()
    print("The task has been added!")


def delete_task():
    rows = session.query(task).all()
    print("Choose the number of the task you want to delete:")
    for i in range(len(rows)):
        print(f"{i + 1}. {rows[i].task}")
    task_number = int(input(""))
    task_to_delete = rows[task_number - 1]
    session.delete(task_to_delete)
    session.commit()
    print("The task has been deleted!")


engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base = declarative_base()
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
while True:
    print("1) Today's tasks")
    print("2) Week's tasks")
    print("3) All tasks")
    print("4) Missed tasks")
    print("5) Add task")
    print("6) Delete task")
    print("0) Exit")
    option = int(input("")
    if option == 1:
        todays_tasks()
    elif option == 2:
        weeks_tasks()
    elif option == 3:
        all_tasks()
    elif option == 4:
        missed_tasks()
    elif option == 5:
        add_task()
    elif option == 6:
        delete_task()
    else:
        break
print("Bye!")
