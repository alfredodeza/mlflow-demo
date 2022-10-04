import sys
import click
import mlflow
import pandas as pd
mlflow.autolog()

def carriage_returns(df):
    for index, row in df.iterrows():
        for column, field in row.items():
            try:
                if "\r\n" in field:
                    return index, column, field
            except TypeError:
                continue


def unnamed_columns(df):
    bad_columns = []
    for key in df.keys():
        if "Unnamed" in key:
            bad_columns.append(key)
    return len(bad_columns)


def zero_count_columns(df):
    bad_columns = []
    for key in df.keys():
        if df[key].count() == 0:
            bad_columns.append(key)
    return bad_columns


@click.command()
@click.argument('metrics', type=bool)
@click.argument('max_errors', type=int)
@click.argument('filename', type=click.Path(exists=True))
def main(metrics, max_errors, filename):
    df = pd.read_csv(filename)
    bad_columns = zero_count_columns(df)
    for column in bad_columns:
        click.echo(f"Warning: Column '{column}' has no items in it")
    unnamed = unnamed_columns(df)
    if unnamed:
        click.echo(f"Warning: found {unnamed} columns that are Unnamed")
    carriage_field = carriage_returns(df)
    if carriage_field:
        index, column, field = carriage_field
        click.echo((
           f"Warning: found carriage returns at index {index}"
           f" of column '{column}':")
        )
        click.echo(f"         '{field[:50]}'")

    if metrics:
        mlflow.log_metric("unnamed", unnamed)
        mlflow.log_metric("zero_count_columns", len(bad_columns))


if __name__ == '__main__':
    main()
