#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
protoa = proto

print(proto)

print(proto[1])

proto.append("dns")
protoa.append("dna")

print(proto)

proto2 = [22,80,443,53]
proto.extend(proto2)
print(proto)
protoa.append(proto2)
print(protoa)

