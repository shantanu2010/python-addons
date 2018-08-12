import click

@click.group()
@click.option('--removedigits/--no-removedigits', default=False,
              help="To remove digits or not")
@click.pass_context
def cli(ctx, removedigits):
    ctx.obj = dict(removedigits=removedigits)


def removedigits(ctx, a_string):
    if ctx.obj['removedigits']:
        a_string = ''.join(c for c in a_string if not c.isdigit())
    return a_string


@cli.command()
@click.option('-d',default=':',help="Used to define any custom concat delimiter")
@click.argument('arguments', nargs=-1)
@click.pass_context
def concat(ctx, arguments,d):
    
    click.echo(removedigits(ctx, d.join(arguments).upper()))	
   
@cli.command()
@click.argument('arguments', nargs=-1)
@click.pass_context
def upper(ctx, arguments):
    

    click.echo(removedigits(ctx, ' '.join(arguments).upper()))


@cli.command()
@click.argument('arguments', nargs=-1)
@click.pass_context
def lower(ctx, arguments):
    

    click.echo(removedigits(ctx, ' '.join(arguments).lower()))


if __name__ == '__main__':
    		
	cli();