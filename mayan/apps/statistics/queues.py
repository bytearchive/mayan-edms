from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from mayan_task_manager.classes import CeleryQueue

queue_statistics = CeleryQueue(
    name='statistics', label=_('Statistics'), transient=True
)

queue_statistics.add_task_type(
    name='statistics.tasks.task_execute_statistic',
    label=_('Execute statistic')
)