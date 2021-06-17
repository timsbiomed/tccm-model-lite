# Auto generated from tccm_model.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-06-17 14:53
# Schema: tccm_model
#
# id: https://w3id.org/tccm_model
# description: Terminology Core Common Model
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import String, Uri, Uriorcurie
from linkml_runtime.utils.metamodelcore import URI, URIorCURIE

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
DC = CurieNamespace('dc', 'http://purl.org/dc/elements/1.1/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCT = CurieNamespace('sct', 'http://snomed.info/id/')
SH = CurieNamespace('sh', 'http://www.w3.org/ns/shacl#')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
TCCM = CurieNamespace('tccm', 'https://hotecosystem.org/tccm/')
DEFAULT_ = TCCM


# Types

# Class references
class ConceptReferenceUri(URIorCURIE):
    pass


class ConceptSystemUri(URIorCURIE):
    pass


class CodeSetUri(URIorCURIE):
    pass


@dataclass
class ConceptReference(YAMLRoot):
    """
    A minimal description of a class, individual, term or similar construct
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SKOS.Concept
    class_class_curie: ClassVar[str] = "skos:Concept"
    class_name: ClassVar[str] = "ConceptReference"
    class_model_uri: ClassVar[URIRef] = TCCM.ConceptReference

    uri: Union[str, ConceptReferenceUri] = None
    code: str = None
    defined_in: Union[str, ConceptSystemUri] = None
    designation: Optional[str] = None
    definition: Optional[str] = None
    reference: Optional[Union[Union[str, URI], List[Union[str, URI]]]] = empty_list()
    narrower_than: Optional[Union[Union[str, ConceptReferenceUri], List[Union[str, ConceptReferenceUri]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.uri):
            self.MissingRequiredField("uri")
        if not isinstance(self.uri, ConceptReferenceUri):
            self.uri = ConceptReferenceUri(self.uri)

        if self._is_empty(self.code):
            self.MissingRequiredField("code")
        if not isinstance(self.code, str):
            self.code = str(self.code)

        if self._is_empty(self.defined_in):
            self.MissingRequiredField("defined_in")
        if not isinstance(self.defined_in, ConceptSystemUri):
            self.defined_in = ConceptSystemUri(self.defined_in)

        if self.designation is not None and not isinstance(self.designation, str):
            self.designation = str(self.designation)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if not isinstance(self.reference, list):
            self.reference = [self.reference] if self.reference is not None else []
        self.reference = [v if isinstance(v, URI) else URI(v) for v in self.reference]

        if not isinstance(self.narrower_than, list):
            self.narrower_than = [self.narrower_than] if self.narrower_than is not None else []
        self.narrower_than = [v if isinstance(v, ConceptReferenceUri) else ConceptReferenceUri(v) for v in self.narrower_than]

        super().__post_init__(**kwargs)


@dataclass
class ConceptSystem(YAMLRoot):
    """
    A terminological resource (ontology, classification scheme, concept system, etc.)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SKOS.ConceptScheme
    class_class_curie: ClassVar[str] = "skos:ConceptScheme"
    class_name: ClassVar[str] = "ConceptSystem"
    class_model_uri: ClassVar[URIRef] = TCCM.ConceptSystem

    uri: Union[str, ConceptSystemUri] = None
    prefix: str = None
    namespace: Optional[Union[str, URI]] = None
    description: Optional[str] = None
    reference: Optional[Union[Union[str, URI], List[Union[str, URI]]]] = empty_list()
    root_concept: Optional[Union[Union[str, ConceptReferenceUri], List[Union[str, ConceptReferenceUri]]]] = empty_list()
    contents: Optional[Union[Dict[Union[str, ConceptReferenceUri], Union[dict, ConceptReference]], List[Union[dict, ConceptReference]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.uri):
            self.MissingRequiredField("uri")
        if not isinstance(self.uri, ConceptSystemUri):
            self.uri = ConceptSystemUri(self.uri)

        if self._is_empty(self.prefix):
            self.MissingRequiredField("prefix")
        if not isinstance(self.prefix, str):
            self.prefix = str(self.prefix)

        if self.namespace is not None and not isinstance(self.namespace, URI):
            self.namespace = URI(self.namespace)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.reference, list):
            self.reference = [self.reference] if self.reference is not None else []
        self.reference = [v if isinstance(v, URI) else URI(v) for v in self.reference]

        if not isinstance(self.root_concept, list):
            self.root_concept = [self.root_concept] if self.root_concept is not None else []
        self.root_concept = [v if isinstance(v, ConceptReferenceUri) else ConceptReferenceUri(v) for v in self.root_concept]

        self._normalize_inlined_as_list(slot_name="contents", slot_type=ConceptReference, key_name="uri", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class CodeSet(YAMLRoot):
    """
    A collection of terminological concept references
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SKOS.CodeSet
    class_class_curie: ClassVar[str] = "skos:CodeSet"
    class_name: ClassVar[str] = "CodeSet"
    class_model_uri: ClassVar[URIRef] = TCCM.CodeSet

    uri: Union[str, CodeSetUri] = None
    description: Optional[str] = None
    designation: Optional[str] = None
    members: Optional[Union[Dict[Union[str, ConceptReferenceUri], Union[dict, ConceptReference]], List[Union[dict, ConceptReference]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.uri):
            self.MissingRequiredField("uri")
        if not isinstance(self.uri, CodeSetUri):
            self.uri = CodeSetUri(self.uri)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.designation is not None and not isinstance(self.designation, str):
            self.designation = str(self.designation)

        self._normalize_inlined_as_list(slot_name="members", slot_type=ConceptReference, key_name="uri", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class Package(YAMLRoot):
    """
    A collection of ConceptSystems
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.Package
    class_class_curie: ClassVar[str] = "tccm:Package"
    class_name: ClassVar[str] = "Package"
    class_model_uri: ClassVar[URIRef] = TCCM.Package

    system: Optional[Union[Dict[Union[str, ConceptSystemUri], Union[dict, ConceptSystem]], List[Union[dict, ConceptSystem]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="system", slot_type=ConceptSystem, key_name="uri", keyed=True)

        super().__post_init__(**kwargs)


# Enumerations


# Slots

