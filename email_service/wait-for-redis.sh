echo "⏳ Waiting for Redis to be ready..."
until nc -z redis 6379; do
  sleep 1
done

echo "✅ Redis is up. Continuing..."
exec "$@"