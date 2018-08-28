
<p align="center">
	<a href="https://pypi.org/project/cu"><img src="https://cdn.abraham.gq/projects/consecutively-unique/logo.svg" width="30%"></a>
	<br>
	<br>
	<br>
	<br>
	<a href="https://pypi.org/project/cu"><b>cu</b></a>: generate a unique value from a consecutively number list
</p>

<p align="center">
	<a href="https://travis-ci.org/abranhe/cu"><img src="https://img.shields.io/travis/abranhe/cu.svg?logo=travis" /></a>
	<a href="https://github.com/abranhe/cu/blob/master/LICENSE"><img src="https://img.shields.io/github/license/abranhe/cu.svg" /></a>
	<a href="https://github.com/abranhe"><img src="https://abranhe.com/badge.svg"></a>
	<a href="https://cash.me/$abranhe"><img src="https://cdn.abraham.gq/badges/cash-me.svg"></a>
	<a href="https://www.patreon.com/abranhe"><img src="https://cdn.abraham.gq/badges/patreon.svg" /></a>
	<a href="https://paypal.me/abranhe/10"><img src="https://cdn.abraham.gq/badges/paypal.svg" /></a>
</p>

# Install

```
$ pip install cu
```

# Why?

- Why not 😂
- Clean and focused
- Actively maintained


# Usage

```py
import cu as consecutively_unique
val = consecutively_unique.cu(1, 5)

print(val(), val(), val(), val())
# => 18 7 1 10
```

# API

**cu(minValue, maxValue)**

> Return a function with a unique value unique value form a consecutively number list

# Related

- [consecutively-unique](https://github.com/abranhe/consecutively-unique): same thing but in **JavaScript**

# Team

|[![Carlos Abraham Logo](https://avatars3.githubusercontent.com/u/21347264?s=50&v=4)](https://19cah.com)|
| :-: |
| [Carlos Abraham](https://github.com/abranhe) |


# License

[MIT](https://github.com/abranhe/cu/blob/master/LICENSE) License © [Carlos Abraham](https://github.com/abranhe)
