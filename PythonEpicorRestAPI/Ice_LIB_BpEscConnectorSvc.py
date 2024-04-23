import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.LIB.BpEscConnectorSvc
# Version: v1



#########################################################################
# OData methods:
#########################################################################
async def getServiceDocument(epicorHeaders = None):
   """  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => application/json
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.BpEscConnectorSvc/",headers=creds) as resp:
           return await resp.json()

async def get_metadata(epicorHeaders = None):
   """  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: Returns metadata document => content
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.BpEscConnectorSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetPackageList(epicorHeaders = None):
   """  
   Summary: Invoke method GetPackageList
   OperationID: GetPackageList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPackageList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.BpEscConnectorSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetPackageProcessList(epicorHeaders = None):
   """  
   Summary: Invoke method GetPackageProcessList
   OperationID: GetPackageProcessList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPackageProcessList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.BpEscConnectorSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetWorkflow(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetWorkflow
   OperationID: GetWorkflow
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetWorkflow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetWorkflow_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.BpEscConnectorSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateUpdateWorkflow(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateUpdateWorkflow
   OperationID: CreateUpdateWorkflow
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateUpdateWorkflow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateUpdateWorkflow_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.BpEscConnectorSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateUserSchema(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateUserSchema
   OperationID: CreateUserSchema
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateUserSchema_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateUserSchema_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.BpEscConnectorSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateScalaIntegrationWorkflow(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateScalaIntegrationWorkflow
   OperationID: CreateScalaIntegrationWorkflow
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateScalaIntegrationWorkflow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateScalaIntegrationWorkflow_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.BpEscConnectorSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateScalaIntegrationWorkflow(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateScalaIntegrationWorkflow
   OperationID: UpdateScalaIntegrationWorkflow
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateScalaIntegrationWorkflow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateScalaIntegrationWorkflow_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.BpEscConnectorSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class CreateScalaIntegrationWorkflow_input:
   """ Required : 
   workflowMetadata
   workflowTemplate
   columnMetadata
   """  
   def __init__(self, obj):
      self.workflowMetadata:list[Ice_Contracts_BpEscConnector_ScalaWorkflowMetadata] = obj["workflowMetadata"]
      self.workflowTemplate:list[Ice_Contracts_BpEscConnector_WorkflowInfo] = obj["workflowTemplate"]
      self.columnMetadata:list[Ice_Contracts_BpEscConnector_ScalaColumnMetadata] = obj["columnMetadata"]
      pass

class CreateScalaIntegrationWorkflow_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Contracts_BpEscConnector_ScalaUpdateWorkflowResult] = obj["returnObj"]
      pass

class CreateUpdateWorkflow_input:
   """ Required : 
   workflow
   flags
   """  
   def __init__(self, obj):
      self.workflow:list[Ice_Contracts_BpEscConnector_WorkflowInfo] = obj["workflow"]
      self.flags:int = obj["flags"]
      pass

class CreateUpdateWorkflow_output:
   def __init__(self, obj):
      pass

class CreateUserSchema_input:
   """ Required : 
   workflow
   overwrite
   """  
   def __init__(self, obj):
      self.workflow:list[Ice_Contracts_BpEscConnector_WorkflowInfo] = obj["workflow"]
      self.overwrite:bool = obj["overwrite"]
      pass

class CreateUserSchema_output:
   def __init__(self, obj):
      pass

class GetPackageList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetPackageProcessList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Contracts_BpEscConnector_PackageInfo] = obj["returnObj"]
      pass

class GetWorkflow_input:
   """ Required : 
   package
   process
   flags
   """  
   def __init__(self, obj):
      self.package:str = obj["package"]
      self.process:str = obj["process"]
      self.flags:int = obj["flags"]
      pass

class GetWorkflow_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Contracts_BpEscConnector_WorkflowInfo] = obj["returnObj"]
      pass

class Ice_Contracts_BpEscConnector_PackageInfo:
   def __init__(self, obj):
      self.Name:str = obj["Name"]
      self.Processes:str = obj["Processes"]
      pass

class Ice_Contracts_BpEscConnector_ScalaColumnMetadata:
   def __init__(self, obj):
      self.PhysicalTableName:str = obj["PhysicalTableName"]
      self.PhysicalColumnName:str = obj["PhysicalColumnName"]
      self.XmlElementName:str = obj["XmlElementName"]
      self.IsUpdatable:bool = obj["IsUpdatable"]
      self.IsRequired:bool = obj["IsRequired"]
      pass

class Ice_Contracts_BpEscConnector_ScalaUpdateWorkflowResult:
   def __init__(self, obj):
      self.WorkflowInfo:list[Ice_Contracts_BpEscConnector_WorkflowInfo] = obj["WorkflowInfo"]
      self.Messages:str = obj["Messages"]
      pass

class Ice_Contracts_BpEscConnector_ScalaWorkflowMetadata:
   def __init__(self, obj):
      self.CompanyId:str = obj["CompanyId"]
      self.QueryId:str = obj["QueryId"]
      self.AllowMultiRowUpdate:bool = obj["AllowMultiRowUpdate"]
      self.DatasetSchemaNamespace:str = obj["DatasetSchemaNamespace"]
      self.DatasetSchemaUrl:str = obj["DatasetSchemaUrl"]
      self.RequestSchemaNamespace:str = obj["RequestSchemaNamespace"]
      self.RequestSchemaUrl:str = obj["RequestSchemaUrl"]
      self.ResponseSchemaNamespace:str = obj["ResponseSchemaNamespace"]
      self.ResponseSchemaUrl:str = obj["ResponseSchemaUrl"]
      pass

class Ice_Contracts_BpEscConnector_SchemaInfo:
   def __init__(self, obj):
      self.Content:list[System_Xml_Linq_XElement] = obj["Content"]
      self.Includes:list[Ice_Contracts_BpEscConnector_SchemaInfo] = obj["Includes"]
      self.SourceUrl:str = obj["SourceUrl"]
      self.Url:str = obj["Url"]
      pass

class Ice_Contracts_BpEscConnector_TransformationInfo:
   def __init__(self, obj):
      self.Content:list[System_Xml_Linq_XElement] = obj["Content"]
      self.IsCommon:bool = obj["IsCommon"]
      self.Name:str = obj["Name"]
      pass

class Ice_Contracts_BpEscConnector_WorkflowInfo:
   def __init__(self, obj):
      self.BizTalkCompatibility:bool = obj["BizTalkCompatibility"]
      self.CacheDuration:int = obj["CacheDuration"]
      self.Content:list[System_Xml_Linq_XElement] = obj["Content"]
      self.InputSchema:list[Ice_Contracts_BpEscConnector_SchemaInfo] = obj["InputSchema"]
      self.OutputSchema:list[Ice_Contracts_BpEscConnector_SchemaInfo] = obj["OutputSchema"]
      self.Package:str = obj["Package"]
      self.Process:str = obj["Process"]
      self.Schemas:list[Ice_Contracts_BpEscConnector_SchemaInfo] = obj["Schemas"]
      self.Transformations:list[Ice_Contracts_BpEscConnector_TransformationInfo] = obj["Transformations"]
      self.WebService:str = obj["WebService"]
      pass

class System_Xml_Linq_XAttribute:
   def __init__(self, obj):
      self.IsNamespaceDeclaration:bool = obj["IsNamespaceDeclaration"]
      self.Name:list[System_Xml_Linq_XName] = obj["Name"]
      self.NextAttribute:list[System_Xml_Linq_XAttribute] = obj["NextAttribute"]
      self.NodeType:int = obj["NodeType"]
      self.PreviousAttribute:list[System_Xml_Linq_XAttribute] = obj["PreviousAttribute"]
      self.Value:str = obj["Value"]
      self.BaseUri:str = obj["BaseUri"]
      self.Document:list[System_Xml_Linq_XDocument] = obj["Document"]
      self.Parent:list[System_Xml_Linq_XElement] = obj["Parent"]
      pass

class System_Xml_Linq_XDeclaration:
   def __init__(self, obj):
      self.Encoding:str = obj["Encoding"]
      self.Standalone:str = obj["Standalone"]
      self.Version:str = obj["Version"]
      pass

class System_Xml_Linq_XDocument:
   def __init__(self, obj):
      self.Declaration:list[System_Xml_Linq_XDeclaration] = obj["Declaration"]
      self.DocumentType:list[System_Xml_Linq_XDocumentType] = obj["DocumentType"]
      self.NodeType:int = obj["NodeType"]
      self.Root:list[System_Xml_Linq_XElement] = obj["Root"]
      self.FirstNode:list[System_Xml_Linq_XNode] = obj["FirstNode"]
      self.LastNode:list[System_Xml_Linq_XNode] = obj["LastNode"]
      self.NextNode:list[System_Xml_Linq_XNode] = obj["NextNode"]
      self.PreviousNode:list[System_Xml_Linq_XNode] = obj["PreviousNode"]
      self.BaseUri:str = obj["BaseUri"]
      self.Document:list[System_Xml_Linq_XDocument] = obj["Document"]
      self.Parent:list[System_Xml_Linq_XElement] = obj["Parent"]
      pass

class System_Xml_Linq_XDocumentType:
   def __init__(self, obj):
      self.InternalSubset:str = obj["InternalSubset"]
      self.Name:str = obj["Name"]
      self.NodeType:int = obj["NodeType"]
      self.PublicId:str = obj["PublicId"]
      self.SystemId:str = obj["SystemId"]
      self.NextNode:list[System_Xml_Linq_XNode] = obj["NextNode"]
      self.PreviousNode:list[System_Xml_Linq_XNode] = obj["PreviousNode"]
      self.BaseUri:str = obj["BaseUri"]
      self.Document:list[System_Xml_Linq_XDocument] = obj["Document"]
      self.Parent:list[System_Xml_Linq_XElement] = obj["Parent"]
      pass

class System_Xml_Linq_XElement:
   def __init__(self, obj):
      self.FirstAttribute:list[System_Xml_Linq_XAttribute] = obj["FirstAttribute"]
      self.HasAttributes:bool = obj["HasAttributes"]
      self.HasElements:bool = obj["HasElements"]
      self.IsEmpty:bool = obj["IsEmpty"]
      self.LastAttribute:list[System_Xml_Linq_XAttribute] = obj["LastAttribute"]
      self.Name:list[System_Xml_Linq_XName] = obj["Name"]
      self.NodeType:int = obj["NodeType"]
      self.Value:str = obj["Value"]
      self.FirstNode:list[System_Xml_Linq_XNode] = obj["FirstNode"]
      self.LastNode:list[System_Xml_Linq_XNode] = obj["LastNode"]
      self.NextNode:list[System_Xml_Linq_XNode] = obj["NextNode"]
      self.PreviousNode:list[System_Xml_Linq_XNode] = obj["PreviousNode"]
      self.BaseUri:str = obj["BaseUri"]
      self.Document:list[System_Xml_Linq_XDocument] = obj["Document"]
      self.Parent:list[System_Xml_Linq_XElement] = obj["Parent"]
      pass

class System_Xml_Linq_XName:
   def __init__(self, obj):
      self.LocalName:str = obj["LocalName"]
      self.Namespace:list[System_Xml_Linq_XNamespace] = obj["Namespace"]
      self.NamespaceName:str = obj["NamespaceName"]
      pass

class System_Xml_Linq_XNamespace:
   def __init__(self, obj):
      self.NamespaceName:str = obj["NamespaceName"]
      pass

class System_Xml_Linq_XNode:
   def __init__(self, obj):
      self.NextNode:list[System_Xml_Linq_XNode] = obj["NextNode"]
      self.PreviousNode:list[System_Xml_Linq_XNode] = obj["PreviousNode"]
      self.BaseUri:str = obj["BaseUri"]
      self.Document:list[System_Xml_Linq_XDocument] = obj["Document"]
      self.NodeType:int = obj["NodeType"]
      self.Parent:list[System_Xml_Linq_XElement] = obj["Parent"]
      pass

class UpdateScalaIntegrationWorkflow_input:
   """ Required : 
   workflowMetadata
   oldWorkflow
   oldColumnMetadata
   workflowTemplate
   columnMetadata
   """  
   def __init__(self, obj):
      self.workflowMetadata:list[Ice_Contracts_BpEscConnector_ScalaWorkflowMetadata] = obj["workflowMetadata"]
      self.oldWorkflow:list[Ice_Contracts_BpEscConnector_WorkflowInfo] = obj["oldWorkflow"]
      self.oldColumnMetadata:list[Ice_Contracts_BpEscConnector_ScalaColumnMetadata] = obj["oldColumnMetadata"]
      self.workflowTemplate:list[Ice_Contracts_BpEscConnector_WorkflowInfo] = obj["workflowTemplate"]
      self.columnMetadata:list[Ice_Contracts_BpEscConnector_ScalaColumnMetadata] = obj["columnMetadata"]
      pass

class UpdateScalaIntegrationWorkflow_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Contracts_BpEscConnector_ScalaUpdateWorkflowResult] = obj["returnObj"]
      pass

