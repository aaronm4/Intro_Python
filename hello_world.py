message = 'Hello World!'
pad = 3
n = len(message) + 2 * pad + 2
print('*' * n)
print('*' + ' ' * (n - 2) + '*')
print('*' + ' ' * pad + message + ' ' * pad + '*')
print('*' + ' ' * (n - 2) + '*')
print('*' * n)
print()
print('Goodbye World')
