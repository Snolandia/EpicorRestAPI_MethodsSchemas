import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.ECCCustomerSvc
// Description: ECC Customer/Consumer main object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ECCCustomerSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ECCCustomerSvc/$metadata", {
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
   Summary: Invoke method ECCCustomerPortal
   Description: Main portal for all customer/consumer connect processing
   OperationID: ECCCustomerPortal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ECCCustomerPortal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ECCCustomerPortal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ECCCustomerPortal(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ECCCustomerSvc/ECCCustomerPortal", {
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
   Summary: Invoke method ConfigurationChangePart
   Description: When a configurator part number becomes a standard part this method will pull in the pricing for that part similar to functionality in Sales Order and Quote
   OperationID: ConfigurationChangePart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ConfigurationChangePart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConfigurationChangePart_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ConfigurationChangePart(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ECCCustomerSvc/ConfigurationChangePart", {
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
      @param guid
   */  
export interface ConfigurationChangePart_input{
   guid:string,
}

export interface ConfigurationChangePart_output{
}

   /** Required : 
      @param requestMsg
   */  
export interface ECCCustomerPortal_input{
   requestMsg:System_Xml_Linq_XElement[],
}

export interface ECCCustomerPortal_output{
   returnObj:System_Xml_Linq_XElement[],
parameters : {
      /**  output parameters  */  
   requestMsg:System_Xml_Linq_XElement[],
}
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

