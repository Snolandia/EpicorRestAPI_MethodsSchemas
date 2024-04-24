import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Ice.BO.BpMethodSvc
// Description: Manages BPM directives for customizing business object methods.
Contains BPM 4GL code generator for BPM directives.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/$metadata", {
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

   /**  
   Summary: Calls GetRows for the service
   Description: Get BpMethods items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BpMethods
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BpMethodRow
   */  
export function get_BpMethods(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BpMethodRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/BpMethods", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BpMethodRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BpMethods
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.BpMethodRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.BpMethodRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BpMethods(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/BpMethods", {
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
   Summary: Calls GetByID to retrieve the BpMethod item
   Description: Calls GetByID to retrieve the BpMethod item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BpMethod
      @param Source Desc: Source   Required: True   Allow empty value : True
      @param BpMethodCode Desc: BpMethodCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BpMethodRow
   */  
export function get_BpMethods_Source_BpMethodCode(Source:string, BpMethodCode:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_BpMethodRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/BpMethods(" + Source + "," + BpMethodCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_BpMethodRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update BpMethod for the service
   Description: Calls UpdateExt to update BpMethod. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BpMethod
      @param Source Desc: Source   Required: True   Allow empty value : True
      @param BpMethodCode Desc: BpMethodCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.BpMethodRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_BpMethods_Source_BpMethodCode(Source:string, BpMethodCode:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/BpMethods(" + Source + "," + BpMethodCode + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete BpMethod item
   Description: Call UpdateExt to delete BpMethod item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BpMethod
      @param Source Desc: Source   Required: True   Allow empty value : True
      @param BpMethodCode Desc: BpMethodCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_BpMethods_Source_BpMethodCode(Source:string, BpMethodCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/BpMethods(" + Source + "," + BpMethodCode + ")", {
          method: 'delete',
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
   Summary: Calls GetByID for the service
   Description: Get BpArguments items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BpArguments1
      @param Source Desc: Source   Required: True   Allow empty value : True
      @param BpMethodCode Desc: BpMethodCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BpArgumentRow
   */  
export function get_BpMethods_Source_BpMethodCode_BpArguments(Source:string, BpMethodCode:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BpArgumentRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/BpMethods(" + Source + "," + BpMethodCode + ")/BpArguments", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BpArgumentRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the BpArgument item
   Description: Calls GetByID to retrieve the BpArgument item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BpArgument1
      @param Source Desc: Source   Required: True   Allow empty value : True
      @param BpMethodCode Desc: BpMethodCode   Required: True   Allow empty value : True
      @param Order Desc: Order   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BpArgumentRow
   */  
export function get_BpMethods_Source_BpMethodCode_BpArguments_Source_BpMethodCode_Order(Source:string, BpMethodCode:string, Order:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_BpArgumentRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/BpMethods(" + Source + "," + BpMethodCode + ")/BpArguments(" + Source + "," + BpMethodCode + "," + Order + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_BpArgumentRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get BpDirectives items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BpDirectives1
      @param Source Desc: Source   Required: True   Allow empty value : True
      @param BpMethodCode Desc: BpMethodCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BpDirectiveRow
   */  
export function get_BpMethods_Source_BpMethodCode_BpDirectives(Source:string, BpMethodCode:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BpDirectiveRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/BpMethods(" + Source + "," + BpMethodCode + ")/BpDirectives", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BpDirectiveRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the BpDirective item
   Description: Calls GetByID to retrieve the BpDirective item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BpDirective1
      @param Source Desc: Source   Required: True   Allow empty value : True
      @param BpMethodCode Desc: BpMethodCode   Required: True   Allow empty value : True
      @param DirectiveID Desc: DirectiveID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BpDirectiveRow
   */  
export function get_BpMethods_Source_BpMethodCode_BpDirectives_DirectiveID(Source:string, BpMethodCode:string, DirectiveID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_BpDirectiveRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/BpMethods(" + Source + "," + BpMethodCode + ")/BpDirectives(" + DirectiveID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_BpDirectiveRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get BpArguments items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BpArguments
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BpArgumentRow
   */  
export function get_BpArguments(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BpArgumentRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/BpArguments", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BpArgumentRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BpArguments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.BpArgumentRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.BpArgumentRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BpArguments(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/BpArguments", {
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
   Summary: Calls GetByID to retrieve the BpArgument item
   Description: Calls GetByID to retrieve the BpArgument item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BpArgument
      @param Source Desc: Source   Required: True   Allow empty value : True
      @param BpMethodCode Desc: BpMethodCode   Required: True   Allow empty value : True
      @param Order Desc: Order   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BpArgumentRow
   */  
export function get_BpArguments_Source_BpMethodCode_Order(Source:string, BpMethodCode:string, Order:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_BpArgumentRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/BpArguments(" + Source + "," + BpMethodCode + "," + Order + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_BpArgumentRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update BpArgument for the service
   Description: Calls UpdateExt to update BpArgument. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BpArgument
      @param Source Desc: Source   Required: True   Allow empty value : True
      @param BpMethodCode Desc: BpMethodCode   Required: True   Allow empty value : True
      @param Order Desc: Order   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.BpArgumentRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_BpArguments_Source_BpMethodCode_Order(Source:string, BpMethodCode:string, Order:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/BpArguments(" + Source + "," + BpMethodCode + "," + Order + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete BpArgument item
   Description: Call UpdateExt to delete BpArgument item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BpArgument
      @param Source Desc: Source   Required: True   Allow empty value : True
      @param BpMethodCode Desc: BpMethodCode   Required: True   Allow empty value : True
      @param Order Desc: Order   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_BpArguments_Source_BpMethodCode_Order(Source:string, BpMethodCode:string, Order:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/BpArguments(" + Source + "," + BpMethodCode + "," + Order + ")", {
          method: 'delete',
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
   Summary: Calls GetRows for the service
   Description: Get BpDirectives items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BpDirectives
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BpDirectiveRow
   */  
export function get_BpDirectives(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BpDirectiveRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/BpDirectives", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BpDirectiveRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BpDirectives
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.BpDirectiveRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.BpDirectiveRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BpDirectives(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/BpDirectives", {
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
   Summary: Calls GetByID to retrieve the BpDirective item
   Description: Calls GetByID to retrieve the BpDirective item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BpDirective
      @param DirectiveID Desc: DirectiveID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BpDirectiveRow
   */  
export function get_BpDirectives_DirectiveID(DirectiveID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_BpDirectiveRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/BpDirectives(" + DirectiveID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_BpDirectiveRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update BpDirective for the service
   Description: Calls UpdateExt to update BpDirective. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BpDirective
      @param DirectiveID Desc: DirectiveID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.BpDirectiveRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_BpDirectives_DirectiveID(DirectiveID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/BpDirectives(" + DirectiveID + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete BpDirective item
   Description: Call UpdateExt to delete BpDirective item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BpDirective
      @param DirectiveID Desc: DirectiveID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_BpDirectives_DirectiveID(DirectiveID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/BpDirectives(" + DirectiveID + ")", {
          method: 'delete',
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
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BpMethodListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BpMethodListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BpMethodListRow)
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
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseBpMethod:string, whereClauseBpArgument:string, whereClauseBpDirective:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseBpMethod!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseBpMethod=" + whereClauseBpMethod
   }
   if(typeof whereClauseBpArgument!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseBpArgument=" + whereClauseBpArgument
   }
   if(typeof whereClauseBpDirective!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseBpDirective=" + whereClauseBpDirective
   }
   if(typeof pageSize!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pageSize=" + pageSize
   }
   if(typeof absolutePage!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "absolutePage=" + absolutePage
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/GetRows" + params, {
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

   /**  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(source:string, bpMethodCode:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof source!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "source=" + source
   }
   if(typeof bpMethodCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "bpMethodCode=" + bpMethodCode
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/GetByID" + params, {
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

   /**  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      @param whereClause Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      @param pageSize Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      @param absolutePage Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetList(whereClause:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClause!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClause=" + whereClause
   }
   if(typeof pageSize!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pageSize=" + pageSize
   }
   if(typeof absolutePage!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "absolutePage=" + absolutePage
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/GetList" + params, {
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

   /**  
   Summary: Invoke method DeleteDirectiveGroup
   Description: Deletes directives by group name for business objects and data tables. UBAQ directives are not involved in this process
   OperationID: DeleteDirectiveGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteDirectiveGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteDirectiveGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteDirectiveGroup(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/DeleteDirectiveGroup", {
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
   Summary: Invoke method GetAvailableReferences
   Description: Gets the available references.
   OperationID: GetAvailableReferences
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAvailableReferences_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailableReferences_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAvailableReferences(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/GetAvailableReferences", {
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
   Summary: Invoke method GetPagedAvailableReferences
   Description: Gets the available references.
   OperationID: GetPagedAvailableReferences
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPagedAvailableReferences_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPagedAvailableReferences_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPagedAvailableReferences(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/GetPagedAvailableReferences", {
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
   Summary: Invoke method GetMethodsByDirectiveGroup
   Description: Gets list of methods which have directives belong to specified directive group.
   OperationID: GetMethodsByDirectiveGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMethodsByDirectiveGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMethodsByDirectiveGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMethodsByDirectiveGroup(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/GetMethodsByDirectiveGroup", {
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
   Summary: Invoke method GetMethodsByDirectiveGroupAndSCCredentials
   Description: Gets list of methods which have directives belong to specified directive group and contain SC action with specified SC credentials.
   OperationID: GetMethodsByDirectiveGroupAndSCCredentials
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMethodsByDirectiveGroupAndSCCredentials_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMethodsByDirectiveGroupAndSCCredentials_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMethodsByDirectiveGroupAndSCCredentials(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/GetMethodsByDirectiveGroupAndSCCredentials", {
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
   Summary: Invoke method GetMethodsByDirectiveFlags
   Description: Gets list of methods which have directives with specified flags
   OperationID: GetMethodsByDirectiveFlags
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMethodsByDirectiveFlags_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMethodsByDirectiveFlags_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMethodsByDirectiveFlags(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/GetMethodsByDirectiveFlags", {
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
   Summary: Invoke method GetDirectiveGroups
   Description: Gets the directive groups.
   OperationID: GetDirectiveGroups
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDirectiveGroups_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDirectiveGroups_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDirectiveGroups(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/GetDirectiveGroups", {
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
   Summary: Invoke method GetEntityList
   Description: Gets the entity list.
   OperationID: GetEntityList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetEntityList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEntityList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetEntityList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/GetEntityList", {
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
   Summary: Invoke method GetMatchedClasses
   Description: Gets the matched classes.
   OperationID: GetMatchedClasses
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMatchedClasses_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMatchedClasses_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMatchedClasses(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/GetMatchedClasses", {
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
   Summary: Invoke method GetMatchedTypes
   Description: Gets the matched types.
   OperationID: GetMatchedTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMatchedTypes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMatchedTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMatchedTypes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/GetMatchedTypes", {
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
   Summary: Invoke method GetNewBpDirectiveEx
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBpDirectiveEx
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBpDirectiveEx_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBpDirectiveEx_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewBpDirectiveEx(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/GetNewBpDirectiveEx", {
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
   Summary: Invoke method GetRowsEx
   OperationID: GetRowsEx
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsEx_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsEx_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsEx(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/GetRowsEx", {
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
   Summary: Invoke method ImportMethod
   Description: Imports the method's directives into the current company.
   OperationID: ImportMethod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportMethod(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/ImportMethod", {
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
   Summary: Invoke method InvalidateCaches
   Description: Invalidate services specific caches.
   OperationID: InvalidateCaches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/InvalidateCaches_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InvalidateCaches(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/InvalidateCaches", {
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
   Summary: Invoke method PrepareArguments
   Description: Gets the method arguments.
   OperationID: PrepareArguments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PrepareArguments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrepareArguments_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PrepareArguments(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/PrepareArguments", {
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
   Summary: Invoke method PrepareTriggerDefinitions
   Description: Prepares the trigger definitions.
   OperationID: PrepareTriggerDefinitions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PrepareTriggerDefinitions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrepareTriggerDefinitions_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PrepareTriggerDefinitions(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/PrepareTriggerDefinitions", {
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
   Summary: Invoke method RegisterMethodCustomization
   Description: Creates or updated Service Method customization entry.
Method returns Method Codes of registered entries (e.g., "Ice.BO.Tip.Update")
   OperationID: RegisterMethodCustomization
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RegisterMethodCustomization_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RegisterMethodCustomization_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RegisterMethodCustomization(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/RegisterMethodCustomization", {
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
   Summary: Invoke method UpdateDirectivesByMethod
   Description: Updates all directives belong to specified method according to settings in DirectiveUpdateInfo
   OperationID: UpdateDirectivesByMethod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateDirectivesByMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateDirectivesByMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateDirectivesByMethod(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/UpdateDirectivesByMethod", {
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
   Summary: Invoke method ValidateMethod
   Description: Validates the method.
   OperationID: ValidateMethod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateMethod(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/ValidateMethod", {
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
   Summary: Invoke method ValidateUserCode
   Description: Validates the user code.
   OperationID: ValidateUserCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateUserCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateUserCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateUserCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/ValidateUserCode", {
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
   Summary: Invoke method GetDirectivesForMethodsCollection
   Description: Get all available directives for particular methods
   OperationID: GetDirectivesForMethodsCollection
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDirectivesForMethodsCollection_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDirectivesForMethodsCollection_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDirectivesForMethodsCollection(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/GetDirectivesForMethodsCollection", {
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
   Summary: Invoke method ExportByDirectiveGroup
   Description: Exports directives by group.
   OperationID: ExportByDirectiveGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportByDirectiveGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportByDirectiveGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExportByDirectiveGroup(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/ExportByDirectiveGroup", {
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
   Summary: Invoke method ExportByService
   Description: Exports directives by service.
   OperationID: ExportByService
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportByService_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportByService_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExportByService(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/ExportByService", {
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
   Summary: Invoke method ExportByTable
   Description: Exports directives by table.
   OperationID: ExportByTable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportByTable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportByTable_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExportByTable(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/ExportByTable", {
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
   Summary: Invoke method Import
   Description: Imports directives.
   OperationID: Import
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Import_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Import_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Import(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/Import", {
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
   Summary: Invoke method ImportBySource
   Description: Imports directives by source.
   OperationID: ImportBySource
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportBySource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportBySource_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportBySource(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/ImportBySource", {
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
   Summary: Invoke method ShallowValidate
   Description: Validates that the data selected for import appears valid.
   OperationID: ShallowValidate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ShallowValidate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ShallowValidate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ShallowValidate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/ShallowValidate", {
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
   Summary: Invoke method GetBpmDirectiveGroupsTS
   Description: Get BPM Directive groups as typed tableset.
   OperationID: GetBpmDirectiveGroupsTS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBpmDirectiveGroupsTS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBpmDirectiveGroupsTS_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBpmDirectiveGroupsTS(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/GetBpmDirectiveGroupsTS", {
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
   Summary: Invoke method GetNewBpMethod
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBpMethod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBpMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBpMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewBpMethod(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/GetNewBpMethod", {
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
   Summary: Invoke method GetNewBpArgument
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBpArgument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBpArgument_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBpArgument_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewBpArgument(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/GetNewBpArgument", {
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
   Summary: Invoke method GetNewBpDirective
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBpDirective
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBpDirective_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBpDirective_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewBpDirective(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/GetNewBpDirective", {
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
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteByID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/DeleteByID", {
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
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetBySysRowID(id:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof id!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "id=" + id
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/GetBySysRowID" + params, {
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

   /**  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetBySysRowIDs(ids:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof ids!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "ids=" + ids
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/GetBySysRowIDs" + params, {
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

   /**  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Update(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/Update", {
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
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateExt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/UpdateExt", {
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
   Summary: Invoke method GetDirectiveVariableTypes
   Description: Returns a list of available directive variable types
   OperationID: GetDirectiveVariableTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDirectiveVariableTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDirectiveVariableTypes(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/GetDirectiveVariableTypes", {
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
   Summary: Invoke method GetByIDBpMethod
   OperationID: GetByIDBpMethod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByIDBpMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDBpMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetByIDBpMethod(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/GetByIDBpMethod", {
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
   Summary: Invoke method GetKineticDirective
   Description: Get XAML directive transformed into JSON for Kinetic browser UI.
   OperationID: Get_GetKineticDirective
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetKineticDirective_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetKineticDirective(directiveId:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof directiveId!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "directiveId=" + directiveId
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/GetKineticDirective" + params, {
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

   /**  
   Summary: Invoke method GetTablesetRelations
   Description: Get tableset relations for execution rules.
   OperationID: GetTablesetRelations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTablesetRelations_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTablesetRelations_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTablesetRelations(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/GetTablesetRelations", {
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
   Summary: Invoke method PreProcessExpression
   Description: Prepare table parameters for the expression.
   OperationID: PreProcessExpression
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreProcessExpression_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreProcessExpression_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreProcessExpression(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/PreProcessExpression", {
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
   Summary: Invoke method ValidateExpression
   Description: Validate expression.
   OperationID: ValidateExpression
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateExpression_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateExpression_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateExpression(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/ValidateExpression", {
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
   Summary: Invoke method ValidateCustomCode
   Description: Validate custom code.
   OperationID: ValidateCustomCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateCustomCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCustomCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateCustomCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/ValidateCustomCode", {
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
   Summary: Invoke method IsValidIdentifier
   Description: Verify variable name.
   OperationID: IsValidIdentifier
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsValidIdentifier_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsValidIdentifier_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsValidIdentifier(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/IsValidIdentifier", {
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
   Summary: Invoke method GetAvailableReferencesWithFilter
   Description: Gets the available references.
   OperationID: GetAvailableReferencesWithFilter
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAvailableReferencesWithFilter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailableReferencesWithFilter_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAvailableReferencesWithFilter(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/GetAvailableReferencesWithFilter", {
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
   Summary: Invoke method GetFoldersForExternalAssemblies
   Description: Get external assembly directory.
   OperationID: GetFoldersForExternalAssemblies
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFoldersForExternalAssemblies_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFoldersForExternalAssemblies(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/GetFoldersForExternalAssemblies", {
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
   Summary: Invoke method ValidateKineticDirective
   Description: Validate directive from Kinetic browser UI.
   OperationID: ValidateKineticDirective
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateKineticDirective_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateKineticDirective_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateKineticDirective(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/ValidateKineticDirective", {
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
   Summary: Invoke method GeneratePICode
   Description: Generates the Programming Interface code.
   OperationID: GeneratePICode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GeneratePICode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GeneratePICode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GeneratePICode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/GeneratePICode", {
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
   Summary: Invoke method GetDirectiveLandingPageList
   Description: Get list of directives to show on landing page.
   OperationID: Get_GetDirectiveLandingPageList
      @param source Desc: Directive source.   Required: True   Allow empty value : True
      @param group Desc: Directive group or empty value.   Required: True   Allow empty value : True
      @param whereClause Desc: Filtering and sorting.   Required: True   Allow empty value : True
      @param pageSize Desc: Page size.   Required: True
      @param absolutePage Desc: Page to show.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDirectiveLandingPageList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetDirectiveLandingPageList(source:string, group:string, whereClause:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof source!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "source=" + source
   }
   if(typeof group!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "group=" + group
   }
   if(typeof whereClause!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClause=" + whereClause
   }
   if(typeof pageSize!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pageSize=" + pageSize
   }
   if(typeof absolutePage!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "absolutePage=" + absolutePage
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/GetDirectiveLandingPageList" + params, {
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

   /**  
   Summary: Invoke method PrepareAndSearchMethodRows
   OperationID: PrepareAndSearchMethodRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PrepareAndSearchMethodRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrepareAndSearchMethodRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PrepareAndSearchMethodRows(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/PrepareAndSearchMethodRows", {
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
   Summary: Invoke method GetWidgets
   Description: Get list of BPM widgets.
   OperationID: Get_GetWidgets
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetWidgets_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetWidgets(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BpMethodSvc/GetWidgets", {
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
// OData Schemas:
//////////////////////////////////////////////////////////////////////////
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BpArgumentRow{
   "odatametadata":string,
   "value":Ice_Tablesets_BpArgumentRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BpDirectiveRow{
   "odatametadata":string,
   "value":Ice_Tablesets_BpDirectiveRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BpMethodListRow{
   "odatametadata":string,
   "value":Ice_Tablesets_BpMethodListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BpMethodRow{
   "odatametadata":string,
   "value":Ice_Tablesets_BpMethodRow[],
}

export interface Ice_Tablesets_BpArgumentRow{
      /**  BPM Agument Source  */  
   "Source":string,
      /**  BPM customization target ID  */  
   "BpMethodCode":string,
      /**  BPM Argument Order sequence number  */  
   "Order":number,
      /**  BPM Argument Name  */  
   "BpArgumentName":string,
      /**  BPM Argument Type  */  
   "Type":string,
      /**  BPM Argument Direction: input, output  */  
   "Direction":string,
      /**  TypeInfo  */  
   "TypeInfo":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_BpDirectiveRow{
      /**  DirectiveID  */  
   "DirectiveID":string,
      /**  Source  */  
   "Source":string,
      /**  BPM customization target ID  */  
   "BpMethodCode":string,
      /**  BPM directive type  */  
   "DirectiveType":number,
      /**  Name  */  
   "Name":string,
      /**  Order  */  
   "Order":number,
      /**  IsEnabled  */  
   "IsEnabled":boolean,
      /**  ReenterMax  */  
   "ReenterMax":number,
      /**  PreventDeadloops  */  
   "PreventDeadloops":boolean,
      /**  VisibilityScope  */  
   "VisibilityScope":number,
      /**  Company  */  
   "Company":string,
      /**  DirectiveGroup  */  
   "DirectiveGroup":string,
      /**  IsUpToDate  */  
   "IsUpToDate":boolean,
      /**  CGCCode  */  
   "CGCCode":string,
      /**  Body  */  
   "Body":string,
      /**  Thumbnail  */  
   "Thumbnail":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  Description  */  
   "Description":string,
      /**  external column to sort directives in the UI.   Equal to Order but allows to change Order value on UI without resorting dataview  */  
   "DisplayOrder":number,
      /**  The compiler diagnostics if a compilation was done.  */  
   "CompilerDiagnostics":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_BpMethodListRow{
      /**  BPM source  */  
   "Source":string,
      /**  BPM customization target ID  */  
   "BpMethodCode":string,
      /**  SystemCode  */  
   "SystemCode":string,
      /**  ObjectNS  */  
   "ObjectNS":string,
      /**  Referenced Business Object  */  
   "BusinessObject":string,
      /**  BPM Method Name  */  
   "Name":string,
      /**  BPM Method Description  */  
   "Description":string,
      /**  Version  */  
   "Version":string,
      /**  Root Transaction flag  */  
   "HasRootTransaction":boolean,
      /**  SignatureStatus  */  
   "SignatureStatus":number,
      /**  BPM Method customization's enable/disable flag  */  
   "Disabled":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "HasOutdatedDirectives":boolean,
   "HasPreProcessing":boolean,
   "HasBaseProcessing":boolean,
   "HasPostProcessing":boolean,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_BpMethodRow{
      /**  BPM source  */  
   "Source":string,
      /**  BPM customization target ID  */  
   "BpMethodCode":string,
      /**  SystemCode  */  
   "SystemCode":string,
      /**  ObjectNS  */  
   "ObjectNS":string,
      /**  Referenced Business Object  */  
   "BusinessObject":string,
      /**  BPM Method Name  */  
   "Name":string,
      /**  BPM Method Description  */  
   "Description":string,
      /**  Version  */  
   "Version":string,
      /**  Root Transaction flag  */  
   "HasRootTransaction":boolean,
      /**  SignatureStatus  */  
   "SignatureStatus":number,
      /**  BPM Method customization's enable/disable flag  */  
   "Disabled":boolean,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  DebugMode  */  
   "DebugMode":boolean,
      /**  DumpSources  */  
   "DumpSources":boolean,
      /**  AdvTracing  */  
   "AdvTracing":boolean,
   "HasOutdatedDirectives":boolean,
   "HasPreProcessing":boolean,
   "HasBaseProcessing":boolean,
   "HasPostProcessing":boolean,
   "IsMDRSEnabled":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param source
      @param bpMethodCode
   */  
export interface DeleteByID_input{
   source:string,
   bpMethodCode:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param anyGroup
      @param directiveGroup
   */  
export interface DeleteDirectiveGroup_input{
      /**  if set to `true` [any group].  */  
   anyGroup:boolean,
      /**  The directive group.  */  
   directiveGroup:string,
}

export interface DeleteDirectiveGroup_output{
}

export interface Epicor_Customization_CodeCheckResult{
   diagnostics:Epicor_Customization_CodeDiagnostic[],
}

export interface Epicor_Customization_CodeDiagnostic{
   Severity:number,
   Code:string,
   Message:string,
   File:string,
   Span:Epicor_Customization_LineSpan[],
}

export interface Epicor_Customization_LinePosition{
   line:number,
   column:number,
}

export interface Epicor_Customization_LineSpan{
   start:Epicor_Customization_LinePosition[],
   end:Epicor_Customization_LinePosition[],
}

export interface Epicor_Customization_Metadata_TypeRef{
   wellknownType:number,
   namespace:string,
   name:string,
   assembly:string,
   options:number,
   elementType:Epicor_Customization_Metadata_TypeRef[],
   genericArguments:Epicor_Customization_Metadata_TypeRef[],
}

   /** Required : 
      @param groupName
   */  
export interface ExportByDirectiveGroup_input{
   groupName:string,
}

export interface ExportByDirectiveGroup_output{
   returnObj:Ice_BO_BpMethod_DirectiveExportResult[],
}

   /** Required : 
      @param systemCode
      @param serviceKind
      @param serviceName
   */  
export interface ExportByService_input{
   systemCode:string,
   serviceKind:string,
   serviceName:string,
}

export interface ExportByService_output{
   returnObj:Ice_BO_BpMethod_DirectiveExportResult[],
}

   /** Required : 
      @param systemCode
      @param tableName
   */  
export interface ExportByTable_input{
   systemCode:string,
   tableName:string,
}

export interface ExportByTable_output{
   returnObj:Ice_BO_BpMethod_DirectiveExportResult[],
}

   /** Required : 
      @param ds
      @param dotNetLanguage
   */  
export interface GeneratePICode_input{
   ds:Ice_Tablesets_BpMethodTableset[],
      /**  The dot net language. For example: CSharp, VbNet.  */  
   dotNetLanguage:string,
}

export interface GeneratePICode_output{
      /**  The generated code.  */  
   returnObj:string,
}

   /** Required : 
      @param referenceGroup
      @param filter
      @param pageNum
      @param pageSize
   */  
export interface GetAvailableReferencesWithFilter_input{
      /**  The reference group.  */  
   referenceGroup:string,
      /**  Search filter. If empty, * will be used.  */  
   filter:string,
      /**  Page number starting 1/  */  
   pageNum:number,
      /**  Page size between 1 and 50.  */  
   pageSize:number,
}

export interface GetAvailableReferencesWithFilter_output{
      /**  List of assembly names for specific filter/  */  
   returnObj:Ice_Contracts_BO_BpMethod_ReferenceInfo[],
}

   /** Required : 
      @param referenceGroup
   */  
export interface GetAvailableReferences_input{
      /**  The reference group.  */  
   referenceGroup:string,
}

export interface GetAvailableReferences_output{
   returnObj:Ice_Contracts_BO_BpMethod_ReferenceInfo[],
}

   /** Required : 
      @param includeUndefined
      @param includeAny
   */  
export interface GetBpmDirectiveGroupsTS_input{
      /**  include undefined.  */  
   includeUndefined:boolean,
      /**  include any.  */  
   includeAny:boolean,
}

export interface GetBpmDirectiveGroupsTS_output{
   returnObj:Ice_Tablesets_BpDirectiveGroupTableset[],
}

   /** Required : 
      @param source
      @param bpMethodCode
   */  
export interface GetByIDBpMethod_input{
   source:string,
   bpMethodCode:string,
}

export interface GetByIDBpMethod_output{
   returnObj:Ice_Tablesets_BpMethodTableset[],
}

   /** Required : 
      @param source
      @param bpMethodCode
   */  
export interface GetByID_input{
   source:string,
   bpMethodCode:string,
}

export interface GetByID_output{
   returnObj:Ice_Tablesets_BpMethodTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Ice_Tablesets_BpMethodTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Ice_Tablesets_BpMethodTableset[],
}

   /** Required : 
      @param sources
   */  
export interface GetDirectiveGroups_input{
      /**  The sources.  */  
   sources:string,
}

export interface GetDirectiveGroups_output{
   returnObj:string,
}

   /** Required : 
      @param source
      @param group
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetDirectiveLandingPageList_input{
      /**  Directive source.  */  
   source:string,
      /**  Directive group or empty value.  */  
   group:string,
      /**  Filtering and sorting.  */  
   whereClause:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Page to show.  */  
   absolutePage:number,
}

export interface GetDirectiveLandingPageList_output{
   returnObj:Ice_Tablesets_BpMethodListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface GetDirectiveVariableTypes_output{
   returnObj:string,
}

   /** Required : 
      @param boSource
      @param methods
   */  
export interface GetDirectivesForMethodsCollection_input{
      /**  The source.  */  
   boSource:string,
      /**  List of methods.  */  
   methods:string,
}

export interface GetDirectivesForMethodsCollection_output{
      /**  List of directives designed for selected methods  */  
   returnObj:Ice_Tablesets_BpDirectiveRow[],
}

   /** Required : 
      @param source
      @param filter
      @param withDirectivesOnly
   */  
export interface GetEntityList_input{
      /**  The source type (one of "BO", "DB", "DQ").  */  
   source:string,
   filter:number,
      /**  True if entities should be filtered by presence of linked directives  */  
   withDirectivesOnly:boolean,
}

export interface GetEntityList_output{
   returnObj:Ice_Contracts_BpmEntity[],
}

export interface GetFoldersForExternalAssemblies_output{
   returnObj:string,
}

   /** Required : 
      @param directiveId
   */  
export interface GetKineticDirective_input{
   directiveId:string,
}

export interface GetKineticDirective_output{
      /**  Directive serialized in JSON.  */  
   returnObj:string,
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetList_input{
      /**  An expression used to filter the rows. Can be left blank for all rows.  */  
   whereClause:string,
      /**  The maximum number of rows to return. Leave as zero for no maximum.  */  
   pageSize:number,
      /**  Page of rows to return.  */  
   absolutePage:number,
}

export interface GetList_output{
   returnObj:Ice_Tablesets_BpMethodListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param assemblyId
      @param matchToMethod
      @param methodSource
   */  
export interface GetMatchedClasses_input{
      /**  The assembly id.  */  
   assemblyId:string,
      /**  The match to method.  */  
   matchToMethod:string,
      /**  The match to method source.  */  
   methodSource:string,
}

export interface GetMatchedClasses_output{
   returnObj:Ice_Contracts_BO_BpMethod_ClassInfo[],
}

   /** Required : 
      @param assemblyId
      @param baseType
      @param typeStartsWith
      @param typeEndsWith
   */  
export interface GetMatchedTypes_input{
      /**  The assembly id.  */  
   assemblyId:string,
      /**  Searchable class must have this base type  */  
   baseType:string,
      /**  Searchable class name starts with...  */  
   typeStartsWith:string,
      /**  Searchable class name ends with...  */  
   typeEndsWith:string,
}

export interface GetMatchedTypes_output{
   returnObj:string,
}

   /** Required : 
      @param directivesState
      @param boSource
      @param directivesScope
      @param visibilityScopes
   */  
export interface GetMethodsByDirectiveFlags_input{
      /**  State of directives to find  */  
   directivesState:number,
      /**  if set to `BO` then selects methods which have source is BO. If set to `DB` then selects methods which have source is DB. If set to empty then selects all methods except DQ  */  
   boSource:string,
      /**  Scope of directives to find  */  
   directivesScope:number,
      /**  Sets of visibility scopes of directives to find  */  
   visibilityScopes:number,
}

export interface GetMethodsByDirectiveFlags_output{
   returnObj:Ice_Tablesets_BpMethodListTableset[],
}

   /** Required : 
      @param directiveGroup
      @param credentials
   */  
export interface GetMethodsByDirectiveGroupAndSCCredentials_input{
      /**  The directive group. `Null` value means don't filter by directive group  */  
   directiveGroup:string,
   credentials:Ice_Contracts_BO_BpMethod_EscCredentialsUpdateInfo[],
}

export interface GetMethodsByDirectiveGroupAndSCCredentials_output{
   returnObj:Ice_Tablesets_BpMethodListTableset[],
}

   /** Required : 
      @param directiveGroup
   */  
export interface GetMethodsByDirectiveGroup_input{
      /**  The directive group.  */  
   directiveGroup:string,
}

export interface GetMethodsByDirectiveGroup_output{
   returnObj:Ice_Tablesets_BpMethodListTableset[],
}

   /** Required : 
      @param ds
      @param source
      @param bpMethodCode
   */  
export interface GetNewBpArgument_input{
   ds:Ice_Tablesets_BpMethodTableset[],
   source:string,
   bpMethodCode:string,
}

export interface GetNewBpArgument_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_BpMethodTableset[],
}
}

   /** Required : 
      @param ds
      @param source
      @param bpMethodCode
      @param directiveType
   */  
export interface GetNewBpDirectiveEx_input{
   ds:Ice_Tablesets_BpMethodTableset[],
   source:string,
   bpMethodCode:string,
   directiveType:number,
}

export interface GetNewBpDirectiveEx_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_BpMethodTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewBpDirective_input{
   ds:Ice_Tablesets_BpMethodTableset[],
}

export interface GetNewBpDirective_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_BpMethodTableset[],
}
}

   /** Required : 
      @param ds
      @param source
   */  
export interface GetNewBpMethod_input{
   ds:Ice_Tablesets_BpMethodTableset[],
   source:string,
}

export interface GetNewBpMethod_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_BpMethodTableset[],
}
}

   /** Required : 
      @param referenceGroup
      @param pageNum
      @param pageSize
   */  
export interface GetPagedAvailableReferences_input{
      /**  The reference group.  */  
   referenceGroup:string,
      /**  Page number  */  
   pageNum:number,
      /**  Page size  */  
   pageSize:number,
}

export interface GetPagedAvailableReferences_output{
   returnObj:Ice_Contracts_BO_BpMethod_ReferenceInfo[],
}

   /** Required : 
      @param source
      @param whereClauseBpMethod
      @param whereClauseBpDirective
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsEx_input{
   source:string,
   whereClauseBpMethod:string,
   whereClauseBpDirective:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRowsEx_output{
   returnObj:Ice_Tablesets_BpMethodTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseBpMethod
      @param whereClauseBpArgument
      @param whereClauseBpDirective
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseBpMethod:string,
   whereClauseBpArgument:string,
   whereClauseBpDirective:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Ice_Tablesets_BpMethodTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param primaryTable
      @param tableSetParameters
      @param isDqMethod
   */  
export interface GetTablesetRelations_input{
      /**  Selected primary table.  */  
   primaryTable:string,
      /**  List of parameters with tableset types.  */  
   tableSetParameters:any,      //schema had no properties on an object.
      /**  If is called for UBAQ.  */  
   isDqMethod:boolean,
}

export interface GetTablesetRelations_output{
      /**  Serialized tableset relations.  */  
   returnObj:string,
}

export interface GetWidgets_output{
   returnObj:Ice_Tablesets_BpWidgetsTableset[],
}

export interface Ice_BO_BpMethod_DirectiveExportImportResult{
   Log:string,
   HasErrors:boolean,
}

export interface Ice_BO_BpMethod_DirectiveExportResult{
   Data:string,
   Log:string,
   HasErrors:boolean,
}

export interface Ice_BOUpdErrorRow{
   TableName:string,
   ErrorLevel:string,
   ErrorType:string,
   ErrorText:string,
   ErrorSysRowID:string,
   SysRowID:string,
   RowMod:string,
}

export interface Ice_BOUpdErrorTableset{
   BOUpdError:Ice_BOUpdErrorRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Contracts_BO_BpMethod_ClassInfo{
   Name:string,
   RequiresDbContext:boolean,
   Methods:System_Tuple_System_String_System_Boolean[],
   StaticMethods:System_Tuple_System_String_System_Boolean[],
}

export interface Ice_Contracts_BO_BpMethod_DirectiveCompileError{
   DirectiveID:string,
   DirectiveName:string,
   DirectiveType:string,
   CompileError:string,
   Company:string,
}

export interface Ice_Contracts_BO_BpMethod_DirectiveUpdateInfo{
   GroupName:string,
   NewGroupName:string,
   SetEnabled:boolean,
   SetVisibilityScope:number,
   SetPreventEndlessLoops:boolean,
   ReenterMax:number,
   Process:number,
   DirectivesState:number,
   RegenerateMethodSignature:boolean,
   EscCredentialsToSearch:Ice_Contracts_BO_BpMethod_EscCredentialsUpdateInfo[],
   EscCredentialsToUpdate:Ice_Contracts_BO_BpMethod_EscCredentialsUpdateInfo[],
   DirectivesScope:number,
   DirectivesVisibilityScopes:number,
}

export interface Ice_Contracts_BO_BpMethod_EscCredentialsUpdateInfo{
   ServerNameType:number,
   ServerName:string,
   UserType:number,
   User:string,
   Password:string,
}

export interface Ice_Contracts_BO_BpMethod_ReferenceInfo{
   Name:string,
   FileName:string,
   Version:string,
}

export interface Ice_Contracts_BpmEntity{
   SystemCode:string,
   Name:string,
   Type:number,
   Description:string,
}

export interface Ice_Extensions_ExtensionRow{
   ColumnValues:object
   RowMod:string,
   SysRowID:string,
}

export interface Ice_Extensions_ExtensionTableColumn{
   ColumnName:string,
   ColumnType:string,
}

export interface Ice_Extensions_ExtensionTableData{
   Table:Ice_Extensions_ExtensionRow[],
   SystemCode:string,
   TableName:string,
   Columns:Ice_Extensions_ExtensionTableColumn[],
   PrimaryKeyColumns:string,
   PeerTableSystemCode:string,
   PeerTableName:string,
}

export interface Ice_Tablesets_BpArgumentRow{
      /**  BPM Agument Source  */  
   Source:string,
      /**  BPM customization target ID  */  
   BpMethodCode:string,
      /**  BPM Argument Order sequence number  */  
   Order:number,
      /**  BPM Argument Name  */  
   BpArgumentName:string,
      /**  BPM Argument Type  */  
   Type:string,
      /**  BPM Argument Direction: input, output  */  
   Direction:string,
      /**  TypeInfo  */  
   TypeInfo:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_BpDirectiveGroupRow{
      /**  Directive group identifier.  */  
   GroupID:number,
      /**  Directive group name.  */  
   GroupName:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_BpDirectiveGroupTableset{
   BpDirectiveGroup:Ice_Tablesets_BpDirectiveGroupRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_BpDirectiveRow{
      /**  DirectiveID  */  
   DirectiveID:string,
      /**  Source  */  
   Source:string,
      /**  BPM customization target ID  */  
   BpMethodCode:string,
      /**  BPM directive type  */  
   DirectiveType:number,
      /**  Name  */  
   Name:string,
      /**  Order  */  
   Order:number,
      /**  IsEnabled  */  
   IsEnabled:boolean,
      /**  ReenterMax  */  
   ReenterMax:number,
      /**  PreventDeadloops  */  
   PreventDeadloops:boolean,
      /**  VisibilityScope  */  
   VisibilityScope:number,
      /**  Company  */  
   Company:string,
      /**  DirectiveGroup  */  
   DirectiveGroup:string,
      /**  IsUpToDate  */  
   IsUpToDate:boolean,
      /**  CGCCode  */  
   CGCCode:string,
      /**  Body  */  
   Body:string,
      /**  Thumbnail  */  
   Thumbnail:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Description  */  
   Description:string,
      /**  external column to sort directives in the UI.   Equal to Order but allows to change Order value on UI without resorting dataview  */  
   DisplayOrder:number,
      /**  The compiler diagnostics if a compilation was done.  */  
   CompilerDiagnostics:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_BpMethodListRow{
      /**  BPM source  */  
   Source:string,
      /**  BPM customization target ID  */  
   BpMethodCode:string,
      /**  SystemCode  */  
   SystemCode:string,
      /**  ObjectNS  */  
   ObjectNS:string,
      /**  Referenced Business Object  */  
   BusinessObject:string,
      /**  BPM Method Name  */  
   Name:string,
      /**  BPM Method Description  */  
   Description:string,
      /**  Version  */  
   Version:string,
      /**  Root Transaction flag  */  
   HasRootTransaction:boolean,
      /**  SignatureStatus  */  
   SignatureStatus:number,
      /**  BPM Method customization's enable/disable flag  */  
   Disabled:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   HasOutdatedDirectives:boolean,
   HasPreProcessing:boolean,
   HasBaseProcessing:boolean,
   HasPostProcessing:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_BpMethodListTableset{
   BpMethodList:Ice_Tablesets_BpMethodListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_BpMethodRow{
      /**  BPM source  */  
   Source:string,
      /**  BPM customization target ID  */  
   BpMethodCode:string,
      /**  SystemCode  */  
   SystemCode:string,
      /**  ObjectNS  */  
   ObjectNS:string,
      /**  Referenced Business Object  */  
   BusinessObject:string,
      /**  BPM Method Name  */  
   Name:string,
      /**  BPM Method Description  */  
   Description:string,
      /**  Version  */  
   Version:string,
      /**  Root Transaction flag  */  
   HasRootTransaction:boolean,
      /**  SignatureStatus  */  
   SignatureStatus:number,
      /**  BPM Method customization's enable/disable flag  */  
   Disabled:boolean,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  DebugMode  */  
   DebugMode:boolean,
      /**  DumpSources  */  
   DumpSources:boolean,
      /**  AdvTracing  */  
   AdvTracing:boolean,
   HasOutdatedDirectives:boolean,
   HasPreProcessing:boolean,
   HasBaseProcessing:boolean,
   HasPostProcessing:boolean,
   IsMDRSEnabled:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_BpMethodTableset{
   BpMethod:Ice_Tablesets_BpMethodRow[],
   BpArgument:Ice_Tablesets_BpArgumentRow[],
   BpDirective:Ice_Tablesets_BpDirectiveRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_BpWidgetRow{
      /**  Widget name  */  
   Name:string,
      /**  Widget group  */  
   Group:string,
      /**  TypeName of the widget  */  
   ElementType:string,
      /**  Tooltip message, the default is the widget name  */  
   Tooltip:string,
      /**  Widget icon identifier  */  
   IconId:string,
      /**  Used to check if a widget applies for the directive type  */  
   DirectiveType:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_BpWidgetsTableset{
   BpWidget:Ice_Tablesets_BpWidgetRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_UpdExtBpMethodTableset{
   BpMethod:Ice_Tablesets_BpMethodRow[],
   BpArgument:Ice_Tablesets_BpArgumentRow[],
   BpDirective:Ice_Tablesets_BpDirectiveRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ds
      @param source
   */  
export interface ImportBySource_input{
   ds:any,      //schema had no properties on an object.
   source:number,
}

export interface ImportBySource_output{
   returnObj:Ice_BO_BpMethod_DirectiveExportImportResult[],
}

   /** Required : 
      @param ds
   */  
export interface ImportMethod_input{
   ds:Ice_Tablesets_BpMethodTableset[],
}

export interface ImportMethod_output{
      /**  List of outdated directive names  */  
   returnObj:Ice_Contracts_BO_BpMethod_DirectiveCompileError[],
}

   /** Required : 
      @param data
      @param destinationGroup
      @param deleteExistingGroup
   */  
export interface Import_input{
   data:string,
   destinationGroup:string,
   deleteExistingGroup:boolean,
}

export interface Import_output{
   returnObj:Ice_BO_BpMethod_DirectiveExportImportResult[],
}

export interface InvalidateCaches_output{
}

   /** Required : 
      @param varName
   */  
export interface IsValidIdentifier_input{
      /**  Variable name.  */  
   varName:string,
}

export interface IsValidIdentifier_output{
      /**  True if valid identifier.  */  
   returnObj:boolean,
}

   /** Required : 
      @param expressionDefinition
      @param rowVariables
   */  
export interface PreProcessExpression_input{
      /**  Serialized expression definition.  */  
   expressionDefinition:string,
      /**  List of row variables in the directive.  */  
   rowVariables:any,      //schema had no properties on an object.
}

export interface PreProcessExpression_output{
      /**  Preprocessed serialized expression definition.  */  
   returnObj:string,
}

   /** Required : 
      @param source
      @param whereClauseBpMethod
      @param whereClauseBpDirective
      @param pageSize
      @param absolutePage
   */  
export interface PrepareAndSearchMethodRows_input{
   source:string,
   whereClauseBpMethod:string,
   whereClauseBpDirective:string,
   pageSize:number,
   absolutePage:number,
}

export interface PrepareAndSearchMethodRows_output{
   returnObj:Ice_Tablesets_BpMethodTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param methodRow
   */  
export interface PrepareArguments_input{
   methodRow:Ice_Tablesets_BpMethodRow[],
}

export interface PrepareArguments_output{
   returnObj:Ice_Tablesets_BpArgumentRow[],
parameters : {
      /**  output parameters  */  
   methodRow:Ice_Tablesets_BpMethodRow[],
}
}

   /** Required : 
      @param tableMask
      @param listMode
   */  
export interface PrepareTriggerDefinitions_input{
      /**  The table mask.  */  
   tableMask:string,
      /**  if set to `true` then table mask is treated as comma-separated list of tables.  */  
   listMode:boolean,
}

export interface PrepareTriggerDefinitions_output{
   returnObj:string,
}

   /** Required : 
      @param systemCode
      @param serviceKind
      @param serviceName
      @param methodMask
   */  
export interface RegisterMethodCustomization_input{
      /**  Code of system where service defined (e.g., "ICE", "ERP")  */  
   systemCode:string,
      /**  Kind of service. The following kinds are supported: "BO", "Lib", "Proc", and "Rpt"  */  
   serviceKind:string,
      /**  The service name.  */  
   serviceName:string,
      /**  The method mask.  */  
   methodMask:string,
}

export interface RegisterMethodCustomization_output{
   returnObj:string,
}

   /** Required : 
      @param data
   */  
export interface ShallowValidate_input{
   data:string,
}

export interface ShallowValidate_output{
   returnObj:boolean,
}

export interface System_Tuple_System_String_System_Boolean{
   Item1:string,
   Item2:boolean,
}

   /** Required : 
      @param source
      @param methodCode
      @param dirInfo
   */  
export interface UpdateDirectivesByMethod_input{
      /**  The source type (one of "BO", "DB", "DQ").  */  
   source:string,
      /**  Name of method including system code, business object name and method name  */  
   methodCode:string,
   dirInfo:Ice_Contracts_BO_BpMethod_DirectiveUpdateInfo[],
}

export interface UpdateDirectivesByMethod_output{
      /**  List of compilation errors if any occurs. Otherwise - empty list  */  
   returnObj:Ice_Contracts_BO_BpMethod_DirectiveCompileError[],
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Ice_Tablesets_UpdExtBpMethodTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_UpdExtBpMethodTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Ice_Tablesets_BpMethodTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_BpMethodTableset[],
}
}

   /** Required : 
      @param codeSnippetWithScope
      @param functionDefinition
      @param isAsync
   */  
export interface ValidateCustomCode_input{
      /**  Serialized code snippet definition.  */  
   codeSnippetWithScope:string,
      /**  Serialized function definition.  */  
   functionDefinition:string,
      /**  Async execution.  */  
   isAsync:boolean,
}

export interface ValidateCustomCode_output{
   returnObj:Epicor_Customization_CodeCheckResult[],
}

   /** Required : 
      @param expressionWithScope
      @param functionDefinition
   */  
export interface ValidateExpression_input{
      /**  Serialized expression definition.  */  
   expressionWithScope:string,
      /**  Serialized function definition.  */  
   functionDefinition:string,
}

export interface ValidateExpression_output{
   returnObj:Epicor_Customization_CodeCheckResult[],
}

   /** Required : 
      @param ds
   */  
export interface ValidateKineticDirective_input{
   ds:Ice_Tablesets_BpMethodTableset[],
}

export interface ValidateKineticDirective_output{
      /**  Array of Validation items as JSON string.
Example: [{"ElementId":"00000000-0000-0000-0000-000000000000","Element":"","Text":"Workflow validation succeeded. No issues were found","Severity":3}]  */  
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param source
      @param businessObject
      @param methodName
   */  
export interface ValidateMethod_input{
      /**  The source.  */  
   source:string,
      /**  The business object.  */  
   businessObject:string,
      /**  Name of the method.  */  
   methodName:string,
}

export interface ValidateMethod_output{
parameters : {
      /**  output parameters  */  
   regenMethod:boolean,
   blockDirs:boolean,
}
}

   /** Required : 
      @param source
      @param businessObject
      @param code
   */  
export interface ValidateUserCode_input{
      /**  The source.  */  
   source:string,
      /**  The business object.  */  
   businessObject:string,
      /**  The code.  */  
   code:string,
}

export interface ValidateUserCode_output{
parameters : {
      /**  output parameters  */  
   result:number,
   errorMsg:string,
   errorRow:number,
   errorCol:number,
}
}

