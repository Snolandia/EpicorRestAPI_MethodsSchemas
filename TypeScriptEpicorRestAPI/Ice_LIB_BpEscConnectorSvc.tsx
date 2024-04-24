import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Ice.LIB.BpEscConnectorSvc
// Version: v1



//////////////////////////////////////////////////////////////////////////
// OData methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => application/json
   */  
export function getServiceDocument(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<JSON>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.BpEscConnectorSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as JSON)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: Returns metadata document => content
   */  
export function get_metadata(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.BpEscConnectorSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
// Custom methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Invoke method GetPackageList
   OperationID: GetPackageList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPackageList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPackageList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.BpEscConnectorSvc/GetPackageList", {
          method: 'post',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPackageProcessList
   OperationID: GetPackageProcessList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPackageProcessList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPackageProcessList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.BpEscConnectorSvc/GetPackageProcessList", {
          method: 'post',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetWorkflow
   OperationID: GetWorkflow
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetWorkflow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetWorkflow_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetWorkflow(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.BpEscConnectorSvc/GetWorkflow", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateUpdateWorkflow
   OperationID: CreateUpdateWorkflow
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateUpdateWorkflow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateUpdateWorkflow_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateUpdateWorkflow(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.BpEscConnectorSvc/CreateUpdateWorkflow", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateUserSchema
   OperationID: CreateUserSchema
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateUserSchema_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateUserSchema_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateUserSchema(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.BpEscConnectorSvc/CreateUserSchema", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateScalaIntegrationWorkflow
   OperationID: CreateScalaIntegrationWorkflow
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateScalaIntegrationWorkflow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateScalaIntegrationWorkflow_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateScalaIntegrationWorkflow(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.BpEscConnectorSvc/CreateScalaIntegrationWorkflow", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateScalaIntegrationWorkflow
   OperationID: UpdateScalaIntegrationWorkflow
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateScalaIntegrationWorkflow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateScalaIntegrationWorkflow_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateScalaIntegrationWorkflow(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.BpEscConnectorSvc/UpdateScalaIntegrationWorkflow", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
// OData Schemas:
//////////////////////////////////////////////////////////////////////////



//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param workflowMetadata
      @param workflowTemplate
      @param columnMetadata
   */  
export interface CreateScalaIntegrationWorkflow_input{
   workflowMetadata:Ice_Contracts_BpEscConnector_ScalaWorkflowMetadata[],
   workflowTemplate:Ice_Contracts_BpEscConnector_WorkflowInfo[],
   columnMetadata:Ice_Contracts_BpEscConnector_ScalaColumnMetadata[],
}

export interface CreateScalaIntegrationWorkflow_output{
   returnObj:Ice_Contracts_BpEscConnector_ScalaUpdateWorkflowResult[],
}

   /** Required : 
      @param workflow
      @param flags
   */  
export interface CreateUpdateWorkflow_input{
   workflow:Ice_Contracts_BpEscConnector_WorkflowInfo[],
   flags:number,
}

export interface CreateUpdateWorkflow_output{
}

   /** Required : 
      @param workflow
      @param overwrite
   */  
export interface CreateUserSchema_input{
   workflow:Ice_Contracts_BpEscConnector_WorkflowInfo[],
   overwrite:boolean,
}

export interface CreateUserSchema_output{
}

export interface GetPackageList_output{
   returnObj:string,
}

export interface GetPackageProcessList_output{
   returnObj:Ice_Contracts_BpEscConnector_PackageInfo[],
}

   /** Required : 
      @param package
      @param process
      @param flags
   */  
export interface GetWorkflow_input{
   package:string,
   process:string,
   flags:number,
}

export interface GetWorkflow_output{
   returnObj:Ice_Contracts_BpEscConnector_WorkflowInfo[],
}

export interface Ice_Contracts_BpEscConnector_PackageInfo{
   Name:string,
   Processes:string,
}

export interface Ice_Contracts_BpEscConnector_ScalaColumnMetadata{
   PhysicalTableName:string,
   PhysicalColumnName:string,
   XmlElementName:string,
   IsUpdatable:boolean,
   IsRequired:boolean,
}

export interface Ice_Contracts_BpEscConnector_ScalaUpdateWorkflowResult{
   WorkflowInfo:Ice_Contracts_BpEscConnector_WorkflowInfo[],
   Messages:string,
}

export interface Ice_Contracts_BpEscConnector_ScalaWorkflowMetadata{
   CompanyId:string,
   QueryId:string,
   AllowMultiRowUpdate:boolean,
   DatasetSchemaNamespace:string,
   DatasetSchemaUrl:string,
   RequestSchemaNamespace:string,
   RequestSchemaUrl:string,
   ResponseSchemaNamespace:string,
   ResponseSchemaUrl:string,
}

export interface Ice_Contracts_BpEscConnector_SchemaInfo{
   Content:System_Xml_Linq_XElement[],
   Includes:Ice_Contracts_BpEscConnector_SchemaInfo[],
   SourceUrl:string,
   Url:string,
}

export interface Ice_Contracts_BpEscConnector_TransformationInfo{
   Content:System_Xml_Linq_XElement[],
   IsCommon:boolean,
   Name:string,
}

export interface Ice_Contracts_BpEscConnector_WorkflowInfo{
   BizTalkCompatibility:boolean,
   CacheDuration:number,
   Content:System_Xml_Linq_XElement[],
   InputSchema:Ice_Contracts_BpEscConnector_SchemaInfo[],
   OutputSchema:Ice_Contracts_BpEscConnector_SchemaInfo[],
   Package:string,
   Process:string,
   Schemas:Ice_Contracts_BpEscConnector_SchemaInfo[],
   Transformations:Ice_Contracts_BpEscConnector_TransformationInfo[],
   WebService:string,
}

export interface System_Xml_Linq_XAttribute{
   IsNamespaceDeclaration:boolean,
   Name:System_Xml_Linq_XName[],
   NextAttribute:System_Xml_Linq_XAttribute[],
   NodeType:number,
   PreviousAttribute:System_Xml_Linq_XAttribute[],
   Value:string,
   BaseUri:string,
   Document:System_Xml_Linq_XDocument[],
   Parent:System_Xml_Linq_XElement[],
}

export interface System_Xml_Linq_XDeclaration{
   Encoding:string,
   Standalone:string,
   Version:string,
}

export interface System_Xml_Linq_XDocument{
   Declaration:System_Xml_Linq_XDeclaration[],
   DocumentType:System_Xml_Linq_XDocumentType[],
   NodeType:number,
   Root:System_Xml_Linq_XElement[],
   FirstNode:System_Xml_Linq_XNode[],
   LastNode:System_Xml_Linq_XNode[],
   NextNode:System_Xml_Linq_XNode[],
   PreviousNode:System_Xml_Linq_XNode[],
   BaseUri:string,
   Document:System_Xml_Linq_XDocument[],
   Parent:System_Xml_Linq_XElement[],
}

export interface System_Xml_Linq_XDocumentType{
   InternalSubset:string,
   Name:string,
   NodeType:number,
   PublicId:string,
   SystemId:string,
   NextNode:System_Xml_Linq_XNode[],
   PreviousNode:System_Xml_Linq_XNode[],
   BaseUri:string,
   Document:System_Xml_Linq_XDocument[],
   Parent:System_Xml_Linq_XElement[],
}

export interface System_Xml_Linq_XElement{
   FirstAttribute:System_Xml_Linq_XAttribute[],
   HasAttributes:boolean,
   HasElements:boolean,
   IsEmpty:boolean,
   LastAttribute:System_Xml_Linq_XAttribute[],
   Name:System_Xml_Linq_XName[],
   NodeType:number,
   Value:string,
   FirstNode:System_Xml_Linq_XNode[],
   LastNode:System_Xml_Linq_XNode[],
   NextNode:System_Xml_Linq_XNode[],
   PreviousNode:System_Xml_Linq_XNode[],
   BaseUri:string,
   Document:System_Xml_Linq_XDocument[],
   Parent:System_Xml_Linq_XElement[],
}

export interface System_Xml_Linq_XName{
   LocalName:string,
   Namespace:System_Xml_Linq_XNamespace[],
   NamespaceName:string,
}

export interface System_Xml_Linq_XNamespace{
   NamespaceName:string,
}

export interface System_Xml_Linq_XNode{
   NextNode:System_Xml_Linq_XNode[],
   PreviousNode:System_Xml_Linq_XNode[],
   BaseUri:string,
   Document:System_Xml_Linq_XDocument[],
   NodeType:number,
   Parent:System_Xml_Linq_XElement[],
}

   /** Required : 
      @param workflowMetadata
      @param oldWorkflow
      @param oldColumnMetadata
      @param workflowTemplate
      @param columnMetadata
   */  
export interface UpdateScalaIntegrationWorkflow_input{
   workflowMetadata:Ice_Contracts_BpEscConnector_ScalaWorkflowMetadata[],
   oldWorkflow:Ice_Contracts_BpEscConnector_WorkflowInfo[],
   oldColumnMetadata:Ice_Contracts_BpEscConnector_ScalaColumnMetadata[],
   workflowTemplate:Ice_Contracts_BpEscConnector_WorkflowInfo[],
   columnMetadata:Ice_Contracts_BpEscConnector_ScalaColumnMetadata[],
}

export interface UpdateScalaIntegrationWorkflow_output{
   returnObj:Ice_Contracts_BpEscConnector_ScalaUpdateWorkflowResult[],
}

