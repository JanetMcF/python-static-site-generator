import typer
from ssg.site import Site


def main(source='content', destination='dist'):
    config = {'source': source, 'destination': destination}
    Site.__init__(**config)
    Site.build()


typer.run(main)



