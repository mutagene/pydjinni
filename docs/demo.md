---
template: demo.html
hide:
  - navigation
  - toc
---

<div id="demo" markdown>

<div class="demo-left" markdown>

=== "IDL"

    <span class=rich_editor>
        <code id="rich_idl_input" class="rich_text"></code>
        <textarea disabled id="idl_input" name="idl_input" placeholder="Define your PyDjinni interface here..." spellcheck="false">
    foo = enum {
        bar;
        baz;
    }
    </textarea>
    </span>
=== "Config"

    <span class=rich_editor>
        <code id="rich_config_input" class="rich_text"></code>
        <textarea disabled id="config_input" name="config_input" spellcheck="false">
    generate:
        cpp:
            namespace: foo::bar
        java:
            package: foo.bar
        jni:
            namespace: foo::bar::jni
        objc:
            type_prefix: FB
            swift_bridging_header: bridging_header.h
    </textarea>
    </span>

</div>

<div class="demo-right" markdown>

=== "C++"

    <span id="generated_cpp_files" class="generated_listing" markdown>
        <span class="teaser">:material-file-code:<br>Generated C++ interfaces will be displayed here.</span>
    </span>

=== "Java"

    <span id="generated_java_files" class="generated_listing" markdown>
        <span class="teaser">:material-file-code:<br>Generated Java code will be displayed here.</span>
    </span>

=== "Objective-C"

    <span id="generated_objc_files" class="generated_listing" markdown>
        <span class="teaser">:material-file-code:<br>Generated Objective-C interfaces will be displayed here.</span>
    </span>

</div>

</div>

<div id="demo_output">
    This demo uses Pyodide to execute Python code in the Browser. It requires Javascript and a good portion of luck to work!
</div>

----

# About this demo

This live demo visualizes the public interfaces that are generated by PyDjinni in C++ and the host languages.

It uses the amazing [Pyodide](https://pyodide.org/){ target=_blank } project to execute Python code in the browser.
No data is sent to a server!

!!! warning "Don't use this for serious work!"

    This demo is just intended for fuzzing around with the IDL, it is highly experimental and may crash unexpectedly or 
    stop working! All data will be lost once the browser tab is closed.

<br>

<small>This demo runs on PyDjinni v<span id="pydjinni_version">{{ pydjinni_version() }}</span></small>