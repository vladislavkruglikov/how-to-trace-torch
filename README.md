## Usage

Build container with dependencies

```bash
docker compose build dependencies
```

Now you have few options. First you can get into container via terminal

Start container

```bash
docker compose up -d dependencies
```

Get into started container

```bash
docker compose exec -it dependencies bash
```

And second option is to use visual studio extension that allows 
you to get into running container. This option will actually be better 
in the way that now visual studio code could see your installed dependencies
and show suggestions which is convinient
