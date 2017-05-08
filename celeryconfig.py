print "celeryconfig!"

broker_url = 'amqp://guest@192.168.1.6:5672'
result_backend = 'rpc://'

include = ['test_celery.tasks']


def route_task(name, args, kwargs, options, task=None, **kw):
        if name == 'myapp.tasks.compress_video':
            return {'exchange': 'video',
                    'exchange_type': 'topic',
                    'routing_key': 'video.compress'}
        print "no route"

task_routes = (route_task,)
