import time
from camunda.external_task.external_task import ExternalTask, TaskResult
from camunda.external_task.external_task_worker import ExternalTaskWorker


default_config = {
    "maxTasks": 1,
    "lockDuration": 10000,
    "asyncResponseTimeout": 5000,
    "retries": 3,
    "retryTimeout": 5000,
    "sleepSeconds": 30
}


def handle_task(task: ExternalTask) -> TaskResult:
    failure, bpmn_error = random_true(), random_true()
    if failure:
        return task.failure(error_message="task failed", error_details="failed task details",
                            max_retries=3, retry_timeout=5000)

    print("sent an external event")
    return task.complete()


def random_true():
    current_milli_time = int(round(time.time() * 1000))
    return current_milli_time % 2 == 0


if __name__ == '__main__':
    ExternalTaskWorker(worker_id="1", config=default_config).subscribe("topicName", handle_task)