# pyurll
An object model for manipulating URL values.

## Project status
This project and the contents of this file are in early stages of
development.

## URL structure breakdown
Here is an example of the primary conceptual breakdown of a full URL
that includes all optional parts into components and sub-components
modeled in this package.

- URL: http://www.example.com:80/path/to/resource?key1=value1&key2=value2#PlaceInDocument
  - Network URL: http://www.example.com:80/path/to/resource?key1=value1&key2=value2
    - Origin: http://www.example.com:80
      - Scheme Part: http://
        - Scheme: http
      - Netloc: www.example.com:80
        - Hostname: www.example.com
        - Port Part: :80
          - Port: 80
    - Full Path: /path/to/resource?key1=value1&key2=value2
      - Pathname: /path/to/resource
      - Query part: ?key1=value1&key2=value2
        - Query: key1=value1&key2=value2
  - Fragment Part: #PlaceInDocument
    - Fragment: PlaceInDocument

### URL
The full URL including all applicable parts.  A full URL may be
absolute or relative and does not necessariy include every optional
component.

Examples of valid URLs include the one in the example above as
well as "http://127.0.0.1/", "https://company-server:8080/#page2",
"about", and "/products/123/overview#specs".

### Network URL
All of the full URL except for the Fragment Part.  The Fragment Part
is not sent to the server as part of a network request.

### Fragment Part and Fragment
The Fragment Part is the portion of the URL that is used by the client
to identify a location within content after receiving it in a
response.  It is the part of the URL starting with "#" and continuing
to the end of the URL string.

The Fragment is the portion of the Fragment Part following the initial
"#".

In other contexts, an Fragment Part or Fragment may often be referred
to as an Anchor or a Hash.

### Origin
The host and port number to which a connection can be established.

### Full Path
The path to the resource to retrieve from the Netloc, including the
Query Part if applicable.

In other contexts, a Full Path often simply referred to as a Path.

### Scheme Part and Scheme
The Scheme Part is the part of the URL that specifies the URI
scheme.  When present in a URL, it is at the beginning, and it ends
with "://".

The scheme is the actual name of the scheme that precedes the "://".

In other contexts, a Scheme is often referred to as a Protocol.

### Netloc
Specifies the network location to connect to in terms of a hostname
and optional port number.

In other contexts, a Netloc is usually referred to as Authority or
a Host.  This package uses Netloc to be consistent with the
terminology used in Python's netlib package.

### Hostname
Specifies the host to connect to.  That can be either a domain name or
an IP address.

### Port Part and Port
The Port Part specifies the port number to connect to on the host.  It
begins with a colon and is followed by 1 or more digits.

Port is the decimal number represented by the digits following the
colon.

### Pathname
The portion of the full path that precedes the query part (if
present).

In other contexts, a Pathname may be referred to as a Path or a File
Path.

### Query Part and Query
The Query Part is the portion of the full path that starts with a "?"
and includes all of the remaining characters in the full path part.

The Query is the portion of the query part following the initial "?".
