---
layout: ontology_detail
id: mma
title: Mouse Muscle Atlas
jobs:
  - id: https://travis-ci.org/MitraLab-Organization/mouse-muscle-atlas
    type: travis-ci
build:
  checkout: git clone https://github.com/MitraLab-Organization/mouse-muscle-atlas.git
  system: git
  path: "."
contact:
  email: 
  label: 
  github: 
description: Mouse Muscle Atlas is an ontology...
domain: stuff
homepage: https://github.com/MitraLab-Organization/mouse-muscle-atlas
products:
  - id: mma.owl
    name: "Mouse Muscle Atlas main release in OWL format"
  - id: mma.obo
    name: "Mouse Muscle Atlas additional release in OBO format"
  - id: mma.json
    name: "Mouse Muscle Atlas additional release in OBOJSon format"
  - id: mma/mma-base.owl
    name: "Mouse Muscle Atlas main release in OWL format"
  - id: mma/mma-base.obo
    name: "Mouse Muscle Atlas additional release in OBO format"
  - id: mma/mma-base.json
    name: "Mouse Muscle Atlas additional release in OBOJSon format"
dependencies:
- id: ro
- id: bfo
- id: pato
- id: omo
- id: uberon
tracker: https://github.com/MitraLab-Organization/mouse-muscle-atlas/issues
license:
  url: http://creativecommons.org/licenses/by/3.0/
  label: CC-BY
activity_status: active
---

Enter a detailed description of your ontology here. You can use arbitrary markdown and HTML.
You can also embed images too.

