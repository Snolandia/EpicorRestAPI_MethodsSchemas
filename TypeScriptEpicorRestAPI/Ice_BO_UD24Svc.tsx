import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Ice.BO.UD24Svc
// Description: User Defined Table 24
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UD24Svc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UD24Svc/$metadata", {
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
   Description: Get UD24s items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_UD24s
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.UD24Row
   */  
export function get_UD24s(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_UD24Row>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UD24Svc/UD24s", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_UD24Row)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_UD24s
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.UD24Row
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.UD24Row
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UD24s(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UD24Svc/UD24s", {
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
   Summary: Calls GetByID to retrieve the UD24 item
   Description: Calls GetByID to retrieve the UD24 item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_UD24
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.UD24Row
   */  
export function get_UD24s_Company_Key1_Key2_Key3_Key4_Key5(Company:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_UD24Row>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UD24Svc/UD24s(" + Company + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_UD24Row)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update UD24 for the service
   Description: Calls UpdateExt to update UD24. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_UD24
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.UD24Row
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_UD24s_Company_Key1_Key2_Key3_Key4_Key5(Company:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UD24Svc/UD24s(" + Company + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")", {
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
   Summary: Call UpdateExt to delete UD24 item
   Description: Call UpdateExt to delete UD24 item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_UD24
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_UD24s_Company_Key1_Key2_Key3_Key4_Key5(Company:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UD24Svc/UD24s(" + Company + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")", {
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
   Description: Get UD24Attchs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_UD24Attchs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.UD24AttchRow
   */  
export function get_UD24s_Company_Key1_Key2_Key3_Key4_Key5_UD24Attchs(Company:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_UD24AttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UD24Svc/UD24s(" + Company + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")/UD24Attchs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_UD24AttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the UD24Attch item
   Description: Calls GetByID to retrieve the UD24Attch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_UD24Attch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.UD24AttchRow
   */  
export function get_UD24s_Company_Key1_Key2_Key3_Key4_Key5_UD24Attchs_Company_Key1_Key2_Key3_Key4_Key5_DrawingSeq(Company:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_UD24AttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UD24Svc/UD24s(" + Company + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")/UD24Attchs(" + Company + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_UD24AttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get UD24Attchs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_UD24Attchs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.UD24AttchRow
   */  
export function get_UD24Attchs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_UD24AttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UD24Svc/UD24Attchs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_UD24AttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_UD24Attchs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.UD24AttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.UD24AttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UD24Attchs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UD24Svc/UD24Attchs", {
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
   Summary: Calls GetByID to retrieve the UD24Attch item
   Description: Calls GetByID to retrieve the UD24Attch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_UD24Attch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.UD24AttchRow
   */  
export function get_UD24Attchs_Company_Key1_Key2_Key3_Key4_Key5_DrawingSeq(Company:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_UD24AttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UD24Svc/UD24Attchs(" + Company + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_UD24AttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update UD24Attch for the service
   Description: Calls UpdateExt to update UD24Attch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_UD24Attch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.UD24AttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_UD24Attchs_Company_Key1_Key2_Key3_Key4_Key5_DrawingSeq(Company:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UD24Svc/UD24Attchs(" + Company + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete UD24Attch item
   Description: Call UpdateExt to delete UD24Attch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_UD24Attch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_UD24Attchs_Company_Key1_Key2_Key3_Key4_Key5_DrawingSeq(Company:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UD24Svc/UD24Attchs(" + Company + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + DrawingSeq + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.UD24ListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_UD24ListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UD24Svc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_UD24ListRow)
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
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseUD24:string, whereClauseUD24Attch:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseUD24!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseUD24=" + whereClauseUD24
   }
   if(typeof whereClauseUD24Attch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseUD24Attch=" + whereClauseUD24Attch
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UD24Svc/GetRows" + params, {
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
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(key1:string, key2:string, key3:string, key4:string, key5:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof key1!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "key1=" + key1
   }
   if(typeof key2!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "key2=" + key2
   }
   if(typeof key3!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "key3=" + key3
   }
   if(typeof key4!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "key4=" + key4
   }
   if(typeof key5!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "key5=" + key5
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UD24Svc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UD24Svc/GetList" + params, {
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
   Summary: Invoke method GetaNewUD24
   Description: Get new for UD24.
   OperationID: GetaNewUD24
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetaNewUD24_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetaNewUD24_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetaNewUD24(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UD24Svc/GetaNewUD24", {
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
   Summary: Invoke method GetNewUD24
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewUD24
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewUD24_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewUD24_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewUD24(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UD24Svc/GetNewUD24", {
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
   Summary: Invoke method GetNewUD24Attch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewUD24Attch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewUD24Attch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewUD24Attch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewUD24Attch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UD24Svc/GetNewUD24Attch", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UD24Svc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UD24Svc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UD24Svc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UD24Svc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UD24Svc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_UD24AttchRow{
   "odatametadata":string,
   "value":Ice_Tablesets_UD24AttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_UD24ListRow{
   "odatametadata":string,
   "value":Ice_Tablesets_UD24ListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_UD24Row{
   "odatametadata":string,
   "value":Ice_Tablesets_UD24Row[],
}

export interface Ice_Tablesets_UD24AttchRow{
   "Company":string,
   "Key1":string,
   "Key2":string,
   "Key3":string,
   "Key4":string,
   "Key5":string,
   "DrawingSeq":number,
   "XFileRefNum":number,
   "SysRevID":number,
   "SysRowID":string,
   "ForeignSysRowID":string,
   "DrawDesc":string,
   "FileName":string,
   "PDMDocID":string,
   "DocTypeID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_UD24ListRow{
      /**  Company  */  
   "Company":string,
      /**  Key1  */  
   "Key1":string,
      /**  Key2  */  
   "Key2":string,
      /**  Key3  */  
   "Key3":string,
      /**  Key4  */  
   "Key4":string,
      /**  Key5  */  
   "Key5":string,
      /**  Character01  */  
   "Character01":string,
      /**  Character02  */  
   "Character02":string,
      /**  Character03  */  
   "Character03":string,
      /**  Character04  */  
   "Character04":string,
      /**  Character05  */  
   "Character05":string,
      /**  Character06  */  
   "Character06":string,
      /**  Character07  */  
   "Character07":string,
      /**  Character08  */  
   "Character08":string,
      /**  Character09  */  
   "Character09":string,
      /**  Character10  */  
   "Character10":string,
      /**  Number01  */  
   "Number01":number,
      /**  Number02  */  
   "Number02":number,
      /**  Number03  */  
   "Number03":number,
      /**  Number04  */  
   "Number04":number,
      /**  Number05  */  
   "Number05":number,
      /**  Number06  */  
   "Number06":number,
      /**  Number07  */  
   "Number07":number,
      /**  Number08  */  
   "Number08":number,
      /**  Number09  */  
   "Number09":number,
      /**  Number10  */  
   "Number10":number,
      /**  Number11  */  
   "Number11":number,
      /**  Number12  */  
   "Number12":number,
      /**  Number13  */  
   "Number13":number,
      /**  Number14  */  
   "Number14":number,
      /**  Number15  */  
   "Number15":number,
      /**  Number16  */  
   "Number16":number,
      /**  Number17  */  
   "Number17":number,
      /**  Number18  */  
   "Number18":number,
      /**  Number19  */  
   "Number19":number,
      /**  Number20  */  
   "Number20":number,
      /**  Date01  */  
   "Date01":string,
      /**  Date02  */  
   "Date02":string,
      /**  Date03  */  
   "Date03":string,
      /**  Date04  */  
   "Date04":string,
      /**  Date05  */  
   "Date05":string,
      /**  Date06  */  
   "Date06":string,
      /**  Date07  */  
   "Date07":string,
      /**  Date08  */  
   "Date08":string,
      /**  Date09  */  
   "Date09":string,
      /**  Date10  */  
   "Date10":string,
      /**  Date11  */  
   "Date11":string,
      /**  Date12  */  
   "Date12":string,
      /**  Date13  */  
   "Date13":string,
      /**  Date14  */  
   "Date14":string,
      /**  Date15  */  
   "Date15":string,
      /**  Date16  */  
   "Date16":string,
      /**  Date17  */  
   "Date17":string,
      /**  Date18  */  
   "Date18":string,
      /**  Date19  */  
   "Date19":string,
      /**  Date20  */  
   "Date20":string,
      /**  CheckBox01  */  
   "CheckBox01":boolean,
      /**  CheckBox02  */  
   "CheckBox02":boolean,
      /**  CheckBox03  */  
   "CheckBox03":boolean,
      /**  CheckBox04  */  
   "CheckBox04":boolean,
      /**  CheckBox05  */  
   "CheckBox05":boolean,
      /**  CheckBox06  */  
   "CheckBox06":boolean,
      /**  CheckBox07  */  
   "CheckBox07":boolean,
      /**  CheckBox08  */  
   "CheckBox08":boolean,
      /**  CheckBox09  */  
   "CheckBox09":boolean,
      /**  CheckBox10  */  
   "CheckBox10":boolean,
      /**  CheckBox11  */  
   "CheckBox11":boolean,
      /**  CheckBox12  */  
   "CheckBox12":boolean,
      /**  CheckBox13  */  
   "CheckBox13":boolean,
      /**  CheckBox14  */  
   "CheckBox14":boolean,
      /**  CheckBox15  */  
   "CheckBox15":boolean,
      /**  CheckBox16  */  
   "CheckBox16":boolean,
      /**  CheckBox17  */  
   "CheckBox17":boolean,
      /**  CheckBox18  */  
   "CheckBox18":boolean,
      /**  CheckBox19  */  
   "CheckBox19":boolean,
      /**  CheckBox20  */  
   "CheckBox20":boolean,
      /**  ShortChar01  */  
   "ShortChar01":string,
      /**  ShortChar02  */  
   "ShortChar02":string,
      /**  ShortChar03  */  
   "ShortChar03":string,
      /**  ShortChar04  */  
   "ShortChar04":string,
      /**  ShortChar05  */  
   "ShortChar05":string,
      /**  ShortChar06  */  
   "ShortChar06":string,
      /**  ShortChar07  */  
   "ShortChar07":string,
      /**  ShortChar08  */  
   "ShortChar08":string,
      /**  ShortChar09  */  
   "ShortChar09":string,
      /**  ShortChar10  */  
   "ShortChar10":string,
      /**  ShortChar11  */  
   "ShortChar11":string,
      /**  ShortChar12  */  
   "ShortChar12":string,
      /**  ShortChar13  */  
   "ShortChar13":string,
      /**  ShortChar14  */  
   "ShortChar14":string,
      /**  ShortChar15  */  
   "ShortChar15":string,
      /**  ShortChar16  */  
   "ShortChar16":string,
      /**  ShortChar17  */  
   "ShortChar17":string,
      /**  ShortChar18  */  
   "ShortChar18":string,
      /**  ShortChar19  */  
   "ShortChar19":string,
      /**  ShortChar20  */  
   "ShortChar20":string,
      /**  GlobalUD24  */  
   "GlobalUD24":boolean,
      /**  GlobalLock  */  
   "GlobalLock":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_UD24Row{
      /**  Company  */  
   "Company":string,
      /**  Key1  */  
   "Key1":string,
      /**  Key2  */  
   "Key2":string,
      /**  Key3  */  
   "Key3":string,
      /**  Key4  */  
   "Key4":string,
      /**  Key5  */  
   "Key5":string,
      /**  Character01  */  
   "Character01":string,
      /**  Character02  */  
   "Character02":string,
      /**  Character03  */  
   "Character03":string,
      /**  Character04  */  
   "Character04":string,
      /**  Character05  */  
   "Character05":string,
      /**  Character06  */  
   "Character06":string,
      /**  Character07  */  
   "Character07":string,
      /**  Character08  */  
   "Character08":string,
      /**  Character09  */  
   "Character09":string,
      /**  Character10  */  
   "Character10":string,
      /**  Number01  */  
   "Number01":number,
      /**  Number02  */  
   "Number02":number,
      /**  Number03  */  
   "Number03":number,
      /**  Number04  */  
   "Number04":number,
      /**  Number05  */  
   "Number05":number,
      /**  Number06  */  
   "Number06":number,
      /**  Number07  */  
   "Number07":number,
      /**  Number08  */  
   "Number08":number,
      /**  Number09  */  
   "Number09":number,
      /**  Number10  */  
   "Number10":number,
      /**  Number11  */  
   "Number11":number,
      /**  Number12  */  
   "Number12":number,
      /**  Number13  */  
   "Number13":number,
      /**  Number14  */  
   "Number14":number,
      /**  Number15  */  
   "Number15":number,
      /**  Number16  */  
   "Number16":number,
      /**  Number17  */  
   "Number17":number,
      /**  Number18  */  
   "Number18":number,
      /**  Number19  */  
   "Number19":number,
      /**  Number20  */  
   "Number20":number,
      /**  Date01  */  
   "Date01":string,
      /**  Date02  */  
   "Date02":string,
      /**  Date03  */  
   "Date03":string,
      /**  Date04  */  
   "Date04":string,
      /**  Date05  */  
   "Date05":string,
      /**  Date06  */  
   "Date06":string,
      /**  Date07  */  
   "Date07":string,
      /**  Date08  */  
   "Date08":string,
      /**  Date09  */  
   "Date09":string,
      /**  Date10  */  
   "Date10":string,
      /**  Date11  */  
   "Date11":string,
      /**  Date12  */  
   "Date12":string,
      /**  Date13  */  
   "Date13":string,
      /**  Date14  */  
   "Date14":string,
      /**  Date15  */  
   "Date15":string,
      /**  Date16  */  
   "Date16":string,
      /**  Date17  */  
   "Date17":string,
      /**  Date18  */  
   "Date18":string,
      /**  Date19  */  
   "Date19":string,
      /**  Date20  */  
   "Date20":string,
      /**  CheckBox01  */  
   "CheckBox01":boolean,
      /**  CheckBox02  */  
   "CheckBox02":boolean,
      /**  CheckBox03  */  
   "CheckBox03":boolean,
      /**  CheckBox04  */  
   "CheckBox04":boolean,
      /**  CheckBox05  */  
   "CheckBox05":boolean,
      /**  CheckBox06  */  
   "CheckBox06":boolean,
      /**  CheckBox07  */  
   "CheckBox07":boolean,
      /**  CheckBox08  */  
   "CheckBox08":boolean,
      /**  CheckBox09  */  
   "CheckBox09":boolean,
      /**  CheckBox10  */  
   "CheckBox10":boolean,
      /**  CheckBox11  */  
   "CheckBox11":boolean,
      /**  CheckBox12  */  
   "CheckBox12":boolean,
      /**  CheckBox13  */  
   "CheckBox13":boolean,
      /**  CheckBox14  */  
   "CheckBox14":boolean,
      /**  CheckBox15  */  
   "CheckBox15":boolean,
      /**  CheckBox16  */  
   "CheckBox16":boolean,
      /**  CheckBox17  */  
   "CheckBox17":boolean,
      /**  CheckBox18  */  
   "CheckBox18":boolean,
      /**  CheckBox19  */  
   "CheckBox19":boolean,
      /**  CheckBox20  */  
   "CheckBox20":boolean,
      /**  ShortChar01  */  
   "ShortChar01":string,
      /**  ShortChar02  */  
   "ShortChar02":string,
      /**  ShortChar03  */  
   "ShortChar03":string,
      /**  ShortChar04  */  
   "ShortChar04":string,
      /**  ShortChar05  */  
   "ShortChar05":string,
      /**  ShortChar06  */  
   "ShortChar06":string,
      /**  ShortChar07  */  
   "ShortChar07":string,
      /**  ShortChar08  */  
   "ShortChar08":string,
      /**  ShortChar09  */  
   "ShortChar09":string,
      /**  ShortChar10  */  
   "ShortChar10":string,
      /**  ShortChar11  */  
   "ShortChar11":string,
      /**  ShortChar12  */  
   "ShortChar12":string,
      /**  ShortChar13  */  
   "ShortChar13":string,
      /**  ShortChar14  */  
   "ShortChar14":string,
      /**  ShortChar15  */  
   "ShortChar15":string,
      /**  ShortChar16  */  
   "ShortChar16":string,
      /**  ShortChar17  */  
   "ShortChar17":string,
      /**  ShortChar18  */  
   "ShortChar18":string,
      /**  ShortChar19  */  
   "ShortChar19":string,
      /**  ShortChar20  */  
   "ShortChar20":string,
      /**  GlobalUD24  */  
   "GlobalUD24":boolean,
      /**  GlobalLock  */  
   "GlobalLock":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param key1
      @param key2
      @param key3
      @param key4
      @param key5
   */  
export interface DeleteByID_input{
   key1:string,
   key2:string,
   key3:string,
   key4:string,
   key5:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param key1
      @param key2
      @param key3
      @param key4
      @param key5
   */  
export interface GetByID_input{
   key1:string,
   key2:string,
   key3:string,
   key4:string,
   key5:string,
}

export interface GetByID_output{
   returnObj:Ice_Tablesets_UD24Tableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Ice_Tablesets_UD24Tableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Ice_Tablesets_UD24Tableset[],
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
   returnObj:Ice_Tablesets_UD24ListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param key1
      @param key2
      @param key3
      @param key4
      @param key5
   */  
export interface GetNewUD24Attch_input{
   ds:Ice_Tablesets_UD24Tableset[],
   key1:string,
   key2:string,
   key3:string,
   key4:string,
   key5:string,
}

export interface GetNewUD24Attch_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_UD24Tableset[],
}
}

   /** Required : 
      @param ds
      @param key1
      @param key2
      @param key3
      @param key4
   */  
export interface GetNewUD24_input{
   ds:Ice_Tablesets_UD24Tableset[],
   key1:string,
   key2:string,
   key3:string,
   key4:string,
}

export interface GetNewUD24_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_UD24Tableset[],
}
}

   /** Required : 
      @param whereClauseUD24
      @param whereClauseUD24Attch
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseUD24:string,
   whereClauseUD24Attch:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Ice_Tablesets_UD24Tableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetaNewUD24_input{
   ds:Ice_Tablesets_UD24Tableset[],
}

export interface GetaNewUD24_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_UD24Tableset[],
}
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

export interface Ice_Tablesets_UD24AttchRow{
   Company:string,
   Key1:string,
   Key2:string,
   Key3:string,
   Key4:string,
   Key5:string,
   DrawingSeq:number,
   XFileRefNum:number,
   SysRevID:number,
   SysRowID:string,
   ForeignSysRowID:string,
   DrawDesc:string,
   FileName:string,
   PDMDocID:string,
   DocTypeID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_UD24ListRow{
      /**  Company  */  
   Company:string,
      /**  Key1  */  
   Key1:string,
      /**  Key2  */  
   Key2:string,
      /**  Key3  */  
   Key3:string,
      /**  Key4  */  
   Key4:string,
      /**  Key5  */  
   Key5:string,
      /**  Character01  */  
   Character01:string,
      /**  Character02  */  
   Character02:string,
      /**  Character03  */  
   Character03:string,
      /**  Character04  */  
   Character04:string,
      /**  Character05  */  
   Character05:string,
      /**  Character06  */  
   Character06:string,
      /**  Character07  */  
   Character07:string,
      /**  Character08  */  
   Character08:string,
      /**  Character09  */  
   Character09:string,
      /**  Character10  */  
   Character10:string,
      /**  Number01  */  
   Number01:number,
      /**  Number02  */  
   Number02:number,
      /**  Number03  */  
   Number03:number,
      /**  Number04  */  
   Number04:number,
      /**  Number05  */  
   Number05:number,
      /**  Number06  */  
   Number06:number,
      /**  Number07  */  
   Number07:number,
      /**  Number08  */  
   Number08:number,
      /**  Number09  */  
   Number09:number,
      /**  Number10  */  
   Number10:number,
      /**  Number11  */  
   Number11:number,
      /**  Number12  */  
   Number12:number,
      /**  Number13  */  
   Number13:number,
      /**  Number14  */  
   Number14:number,
      /**  Number15  */  
   Number15:number,
      /**  Number16  */  
   Number16:number,
      /**  Number17  */  
   Number17:number,
      /**  Number18  */  
   Number18:number,
      /**  Number19  */  
   Number19:number,
      /**  Number20  */  
   Number20:number,
      /**  Date01  */  
   Date01:string,
      /**  Date02  */  
   Date02:string,
      /**  Date03  */  
   Date03:string,
      /**  Date04  */  
   Date04:string,
      /**  Date05  */  
   Date05:string,
      /**  Date06  */  
   Date06:string,
      /**  Date07  */  
   Date07:string,
      /**  Date08  */  
   Date08:string,
      /**  Date09  */  
   Date09:string,
      /**  Date10  */  
   Date10:string,
      /**  Date11  */  
   Date11:string,
      /**  Date12  */  
   Date12:string,
      /**  Date13  */  
   Date13:string,
      /**  Date14  */  
   Date14:string,
      /**  Date15  */  
   Date15:string,
      /**  Date16  */  
   Date16:string,
      /**  Date17  */  
   Date17:string,
      /**  Date18  */  
   Date18:string,
      /**  Date19  */  
   Date19:string,
      /**  Date20  */  
   Date20:string,
      /**  CheckBox01  */  
   CheckBox01:boolean,
      /**  CheckBox02  */  
   CheckBox02:boolean,
      /**  CheckBox03  */  
   CheckBox03:boolean,
      /**  CheckBox04  */  
   CheckBox04:boolean,
      /**  CheckBox05  */  
   CheckBox05:boolean,
      /**  CheckBox06  */  
   CheckBox06:boolean,
      /**  CheckBox07  */  
   CheckBox07:boolean,
      /**  CheckBox08  */  
   CheckBox08:boolean,
      /**  CheckBox09  */  
   CheckBox09:boolean,
      /**  CheckBox10  */  
   CheckBox10:boolean,
      /**  CheckBox11  */  
   CheckBox11:boolean,
      /**  CheckBox12  */  
   CheckBox12:boolean,
      /**  CheckBox13  */  
   CheckBox13:boolean,
      /**  CheckBox14  */  
   CheckBox14:boolean,
      /**  CheckBox15  */  
   CheckBox15:boolean,
      /**  CheckBox16  */  
   CheckBox16:boolean,
      /**  CheckBox17  */  
   CheckBox17:boolean,
      /**  CheckBox18  */  
   CheckBox18:boolean,
      /**  CheckBox19  */  
   CheckBox19:boolean,
      /**  CheckBox20  */  
   CheckBox20:boolean,
      /**  ShortChar01  */  
   ShortChar01:string,
      /**  ShortChar02  */  
   ShortChar02:string,
      /**  ShortChar03  */  
   ShortChar03:string,
      /**  ShortChar04  */  
   ShortChar04:string,
      /**  ShortChar05  */  
   ShortChar05:string,
      /**  ShortChar06  */  
   ShortChar06:string,
      /**  ShortChar07  */  
   ShortChar07:string,
      /**  ShortChar08  */  
   ShortChar08:string,
      /**  ShortChar09  */  
   ShortChar09:string,
      /**  ShortChar10  */  
   ShortChar10:string,
      /**  ShortChar11  */  
   ShortChar11:string,
      /**  ShortChar12  */  
   ShortChar12:string,
      /**  ShortChar13  */  
   ShortChar13:string,
      /**  ShortChar14  */  
   ShortChar14:string,
      /**  ShortChar15  */  
   ShortChar15:string,
      /**  ShortChar16  */  
   ShortChar16:string,
      /**  ShortChar17  */  
   ShortChar17:string,
      /**  ShortChar18  */  
   ShortChar18:string,
      /**  ShortChar19  */  
   ShortChar19:string,
      /**  ShortChar20  */  
   ShortChar20:string,
      /**  GlobalUD24  */  
   GlobalUD24:boolean,
      /**  GlobalLock  */  
   GlobalLock:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_UD24ListTableset{
   UD24List:Ice_Tablesets_UD24ListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_UD24Row{
      /**  Company  */  
   Company:string,
      /**  Key1  */  
   Key1:string,
      /**  Key2  */  
   Key2:string,
      /**  Key3  */  
   Key3:string,
      /**  Key4  */  
   Key4:string,
      /**  Key5  */  
   Key5:string,
      /**  Character01  */  
   Character01:string,
      /**  Character02  */  
   Character02:string,
      /**  Character03  */  
   Character03:string,
      /**  Character04  */  
   Character04:string,
      /**  Character05  */  
   Character05:string,
      /**  Character06  */  
   Character06:string,
      /**  Character07  */  
   Character07:string,
      /**  Character08  */  
   Character08:string,
      /**  Character09  */  
   Character09:string,
      /**  Character10  */  
   Character10:string,
      /**  Number01  */  
   Number01:number,
      /**  Number02  */  
   Number02:number,
      /**  Number03  */  
   Number03:number,
      /**  Number04  */  
   Number04:number,
      /**  Number05  */  
   Number05:number,
      /**  Number06  */  
   Number06:number,
      /**  Number07  */  
   Number07:number,
      /**  Number08  */  
   Number08:number,
      /**  Number09  */  
   Number09:number,
      /**  Number10  */  
   Number10:number,
      /**  Number11  */  
   Number11:number,
      /**  Number12  */  
   Number12:number,
      /**  Number13  */  
   Number13:number,
      /**  Number14  */  
   Number14:number,
      /**  Number15  */  
   Number15:number,
      /**  Number16  */  
   Number16:number,
      /**  Number17  */  
   Number17:number,
      /**  Number18  */  
   Number18:number,
      /**  Number19  */  
   Number19:number,
      /**  Number20  */  
   Number20:number,
      /**  Date01  */  
   Date01:string,
      /**  Date02  */  
   Date02:string,
      /**  Date03  */  
   Date03:string,
      /**  Date04  */  
   Date04:string,
      /**  Date05  */  
   Date05:string,
      /**  Date06  */  
   Date06:string,
      /**  Date07  */  
   Date07:string,
      /**  Date08  */  
   Date08:string,
      /**  Date09  */  
   Date09:string,
      /**  Date10  */  
   Date10:string,
      /**  Date11  */  
   Date11:string,
      /**  Date12  */  
   Date12:string,
      /**  Date13  */  
   Date13:string,
      /**  Date14  */  
   Date14:string,
      /**  Date15  */  
   Date15:string,
      /**  Date16  */  
   Date16:string,
      /**  Date17  */  
   Date17:string,
      /**  Date18  */  
   Date18:string,
      /**  Date19  */  
   Date19:string,
      /**  Date20  */  
   Date20:string,
      /**  CheckBox01  */  
   CheckBox01:boolean,
      /**  CheckBox02  */  
   CheckBox02:boolean,
      /**  CheckBox03  */  
   CheckBox03:boolean,
      /**  CheckBox04  */  
   CheckBox04:boolean,
      /**  CheckBox05  */  
   CheckBox05:boolean,
      /**  CheckBox06  */  
   CheckBox06:boolean,
      /**  CheckBox07  */  
   CheckBox07:boolean,
      /**  CheckBox08  */  
   CheckBox08:boolean,
      /**  CheckBox09  */  
   CheckBox09:boolean,
      /**  CheckBox10  */  
   CheckBox10:boolean,
      /**  CheckBox11  */  
   CheckBox11:boolean,
      /**  CheckBox12  */  
   CheckBox12:boolean,
      /**  CheckBox13  */  
   CheckBox13:boolean,
      /**  CheckBox14  */  
   CheckBox14:boolean,
      /**  CheckBox15  */  
   CheckBox15:boolean,
      /**  CheckBox16  */  
   CheckBox16:boolean,
      /**  CheckBox17  */  
   CheckBox17:boolean,
      /**  CheckBox18  */  
   CheckBox18:boolean,
      /**  CheckBox19  */  
   CheckBox19:boolean,
      /**  CheckBox20  */  
   CheckBox20:boolean,
      /**  ShortChar01  */  
   ShortChar01:string,
      /**  ShortChar02  */  
   ShortChar02:string,
      /**  ShortChar03  */  
   ShortChar03:string,
      /**  ShortChar04  */  
   ShortChar04:string,
      /**  ShortChar05  */  
   ShortChar05:string,
      /**  ShortChar06  */  
   ShortChar06:string,
      /**  ShortChar07  */  
   ShortChar07:string,
      /**  ShortChar08  */  
   ShortChar08:string,
      /**  ShortChar09  */  
   ShortChar09:string,
      /**  ShortChar10  */  
   ShortChar10:string,
      /**  ShortChar11  */  
   ShortChar11:string,
      /**  ShortChar12  */  
   ShortChar12:string,
      /**  ShortChar13  */  
   ShortChar13:string,
      /**  ShortChar14  */  
   ShortChar14:string,
      /**  ShortChar15  */  
   ShortChar15:string,
      /**  ShortChar16  */  
   ShortChar16:string,
      /**  ShortChar17  */  
   ShortChar17:string,
      /**  ShortChar18  */  
   ShortChar18:string,
      /**  ShortChar19  */  
   ShortChar19:string,
      /**  ShortChar20  */  
   ShortChar20:string,
      /**  GlobalUD24  */  
   GlobalUD24:boolean,
      /**  GlobalLock  */  
   GlobalLock:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_UD24Tableset{
   UD24:Ice_Tablesets_UD24Row[],
   UD24Attch:Ice_Tablesets_UD24AttchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_UpdExtUD24Tableset{
   UD24:Ice_Tablesets_UD24Row[],
   UD24Attch:Ice_Tablesets_UD24AttchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Ice_Tablesets_UpdExtUD24Tableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_UpdExtUD24Tableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Ice_Tablesets_UD24Tableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_UD24Tableset[],
}
}
