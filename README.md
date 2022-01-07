# pyurll
An object model for manipulating URL values.

## Project status
This project and the contents of this file are in early stages of
development.  It does not yet function as a distribution package.

See To Do section later in this document for details about what this
package is eventually indended to do.

## URL structure breakdown
Here is an example of a full URL that includes all optional parts,
and how its component parts are modeled in this package.

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
to identify a location within content after receiving  content in a
response.  It is the part of the URL starting with "#" and continuing
to the end of the URL string.

The Fragment is the portion of the Fragment Part after (not including)
 the "#".

What we are calling the Fragment Part here is also frequently referred
to as the "anchor" or "hash" elsewhere.

### Origin
The host and port number to which a connection can be established.

### Full Path
The path to the resource to retrieve from the Netloc, including the
Query Part if applicable.

What we are calling the Full Path here is also frequently referred
to simply as the "path" elsewhere.

### Scheme Part and Scheme
The Scheme Part is the part of the URL that specifies the URI scheme.
When present in a URL, it is at the beginning, and it ends with "://".

The scheme is the actual name of the scheme that precedes the "://".

What we are calling the Scheme here is also frequently referred to as
the "protocol" elsewhere.

### Netloc
Specifies the network location to connect to in terms of a hostname
and optional port number.

What we are calling the Netloc here is usually referred to as the
"authority" or "host" elsewhere.  We are using Netloc to be match the
nomenclature used in Python's netlib package.

### Hostname
Specifies the host to connect to.  It can be either a domain name or
an IP address.

### Port Part and Port
The Port Part specifies the port number to connect to on the host.  It
begins with a colon and is followed by 1 or more digits.

Port is the decimal number represented by the digits following the
colon.

### Pathname
The portion of the full path that precedes the query part (if
present).

What we are calling the Pathname here is also frequently referred to
as the "path" or "file path" elsewhere.

### Query Part and Query
The Query Part is the portion of the full path that starts with a "?"
and includes all of the remaining characters in the full path part.

The Query is the portion of the query part after (not including) the
"?".

## To Do

### Make this into a usable Python distribution package

Make this installable using pip with specifications of dependencies,
compatible Python versions, etc.

Not important before the functionality is sufficient too be useful to
anyone though.

### Figure out best representation of omitted component

Possibly use None value, but possibly perfer custom null-objects that
don't raise exceptions when sub-component properties are accessed.

### Allow construction of URLs from components and components from sub-components

Possibly allow and array of components to be passed as constructor
argument for this case.

### Make class instances formally read-only and usable as dict keys

Possibly make them dataclasses

### Implement "|" operator in cases where that makes sense

Probably just in cases where either the objects have the same class or
one is a component or subcomponent of the other.

### Add parsing and construction of form-encoded queries

...

### Add support for various kinds of encoding and decoding

...


### Add support for effective port number, based on protocol

Probably use a factory to instantiate URLs and components, and have a
registry of protocol name matchers.
