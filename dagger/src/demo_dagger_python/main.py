import dagger
from dagger import dag, function, object_type


@object_type
class DemoDaggerPython:
    @function
    def container_echo(self, string_arg: str) -> dagger.Container:
        """Returns a container that echoes whatever string argument is provided"""
        return dag.container().from_("alpine:latest").with_exec(["echo", string_arg])

    @function
    async def grep_dir(self, directory_arg: dagger.Directory, pattern: str) -> str:
        """Returns lines that match a pattern in the files of the provided Directory"""
        return await (
            dag.container()
            .from_("alpine:latest")
            .with_mounted_directory("/mnt", directory_arg)
            .with_workdir("/mnt")
            .with_exec(["grep", "-R", pattern, "."])
            .stdout()
        )

    @function
    def build_env(self, source: dagger.Directory) -> dagger.Container:
        """Build a ready-to-use development environment"""
        python_cache = dag.cache_volume("python_cache")
        return (
            dag.container()
            .from_("python:3.13-slim")
            .with_directory("/src", source)
            .with_workdir("/src")
            .with_exec(["apt-get", "update"])
            .with_exec(["pip", "install", "--upgrade", "pip"])
        )
   