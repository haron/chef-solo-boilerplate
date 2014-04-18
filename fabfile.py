import os, json, tempfile
from fabric.api import *
from fabric.contrib.project import rsync_project
from fabric.contrib.files import upload_template

DIR = "/root/chef"
env.user = "root"
env.use_ssh_config = True

@task(default=True)
def deploy(run_list=None):
    rsync_project(
            local_dir="%s/chef" % os.path.dirname(__file__),
            remote_dir=os.path.dirname(DIR),
            delete=True,
            exclude="*.swp"
    )
    run("chef-solo --version || wget -qO - https://www.opscode.com/chef/install.sh | bash")

    actual_run_list = ["recipe[op]"]
    if run_list:
        actual_run_list += run_list.split(";")

    with tempfile.NamedTemporaryFile(bufsize=0) as f:
        json.dump({"run_list": actual_run_list}, f)
        put(f.name, "%s/run_list.json" % DIR)

    with cd(DIR):
        run("chef-solo -c ./solo.rb -j ./run_list.json")
