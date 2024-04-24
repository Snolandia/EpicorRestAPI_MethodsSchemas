import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.QuickEntrySvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/$metadata", {
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
   Description: Get QuickEntries items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuickEntries
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EmpBasicRow
   */  
export function get_QuickEntries(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpBasicRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/QuickEntries", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpBasicRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuickEntries
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EmpBasicRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EmpBasicRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuickEntries(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/QuickEntries", {
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
   Summary: Calls GetByID to retrieve the QuickEntry item
   Description: Calls GetByID to retrieve the QuickEntry item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuickEntry
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EmpBasicRow
   */  
export function get_QuickEntries_Company_EmpID(Company:string, EmpID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EmpBasicRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/QuickEntries(" + Company + "," + EmpID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_EmpBasicRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QuickEntry for the service
   Description: Calls UpdateExt to update QuickEntry. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuickEntry
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EmpBasicRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QuickEntries_Company_EmpID(Company:string, EmpID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/QuickEntries(" + Company + "," + EmpID + ")", {
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
   Summary: Call UpdateExt to delete QuickEntry item
   Description: Call UpdateExt to delete QuickEntry item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuickEntry
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QuickEntries_Company_EmpID(Company:string, EmpID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/QuickEntries(" + Company + "," + EmpID + ")", {
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
   Description: Get QuickEntryExpenses items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuickEntryExpenses1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuickEntryExpenseRow
   */  
export function get_QuickEntries_Company_EmpID_QuickEntryExpenses(Company:string, EmpID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuickEntryExpenseRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/QuickEntries(" + Company + "," + EmpID + ")/QuickEntryExpenses", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuickEntryExpenseRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuickEntryExpense item
   Description: Calls GetByID to retrieve the QuickEntryExpense item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuickEntryExpense1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param QuickEntryType Desc: QuickEntryType   Required: True   Allow empty value : True
      @param QuickEntryCode Desc: QuickEntryCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuickEntryExpenseRow
   */  
export function get_QuickEntries_Company_EmpID_QuickEntryExpenses_Company_EmpID_QuickEntryType_QuickEntryCode(Company:string, EmpID:string, QuickEntryType:string, QuickEntryCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuickEntryExpenseRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/QuickEntries(" + Company + "," + EmpID + ")/QuickEntryExpenses(" + Company + "," + EmpID + "," + QuickEntryType + "," + QuickEntryCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuickEntryExpenseRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QuickEntryTimes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuickEntryTimes1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuickEntryTimeRow
   */  
export function get_QuickEntries_Company_EmpID_QuickEntryTimes(Company:string, EmpID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuickEntryTimeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/QuickEntries(" + Company + "," + EmpID + ")/QuickEntryTimes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuickEntryTimeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuickEntryTime item
   Description: Calls GetByID to retrieve the QuickEntryTime item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuickEntryTime1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param QuickEntryType Desc: QuickEntryType   Required: True   Allow empty value : True
      @param QuickEntryCode Desc: QuickEntryCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuickEntryTimeRow
   */  
export function get_QuickEntries_Company_EmpID_QuickEntryTimes_Company_EmpID_QuickEntryType_QuickEntryCode(Company:string, EmpID:string, QuickEntryType:string, QuickEntryCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuickEntryTimeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/QuickEntries(" + Company + "," + EmpID + ")/QuickEntryTimes(" + Company + "," + EmpID + "," + QuickEntryType + "," + QuickEntryCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuickEntryTimeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QuickEntryExpenses items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuickEntryExpenses
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuickEntryExpenseRow
   */  
export function get_QuickEntryExpenses(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuickEntryExpenseRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/QuickEntryExpenses", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuickEntryExpenseRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuickEntryExpenses
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuickEntryExpenseRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuickEntryExpenseRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuickEntryExpenses(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/QuickEntryExpenses", {
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
   Summary: Calls GetByID to retrieve the QuickEntryExpense item
   Description: Calls GetByID to retrieve the QuickEntryExpense item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuickEntryExpense
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param QuickEntryType Desc: QuickEntryType   Required: True   Allow empty value : True
      @param QuickEntryCode Desc: QuickEntryCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuickEntryExpenseRow
   */  
export function get_QuickEntryExpenses_Company_EmpID_QuickEntryType_QuickEntryCode(Company:string, EmpID:string, QuickEntryType:string, QuickEntryCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuickEntryExpenseRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/QuickEntryExpenses(" + Company + "," + EmpID + "," + QuickEntryType + "," + QuickEntryCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuickEntryExpenseRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QuickEntryExpense for the service
   Description: Calls UpdateExt to update QuickEntryExpense. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuickEntryExpense
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param QuickEntryType Desc: QuickEntryType   Required: True   Allow empty value : True
      @param QuickEntryCode Desc: QuickEntryCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuickEntryExpenseRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QuickEntryExpenses_Company_EmpID_QuickEntryType_QuickEntryCode(Company:string, EmpID:string, QuickEntryType:string, QuickEntryCode:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/QuickEntryExpenses(" + Company + "," + EmpID + "," + QuickEntryType + "," + QuickEntryCode + ")", {
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
   Summary: Call UpdateExt to delete QuickEntryExpense item
   Description: Call UpdateExt to delete QuickEntryExpense item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuickEntryExpense
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param QuickEntryType Desc: QuickEntryType   Required: True   Allow empty value : True
      @param QuickEntryCode Desc: QuickEntryCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QuickEntryExpenses_Company_EmpID_QuickEntryType_QuickEntryCode(Company:string, EmpID:string, QuickEntryType:string, QuickEntryCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/QuickEntryExpenses(" + Company + "," + EmpID + "," + QuickEntryType + "," + QuickEntryCode + ")", {
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
   Description: Get QuickEntryTimes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuickEntryTimes
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuickEntryTimeRow
   */  
export function get_QuickEntryTimes(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuickEntryTimeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/QuickEntryTimes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuickEntryTimeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuickEntryTimes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuickEntryTimeRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuickEntryTimeRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuickEntryTimes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/QuickEntryTimes", {
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
   Summary: Calls GetByID to retrieve the QuickEntryTime item
   Description: Calls GetByID to retrieve the QuickEntryTime item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuickEntryTime
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param QuickEntryType Desc: QuickEntryType   Required: True   Allow empty value : True
      @param QuickEntryCode Desc: QuickEntryCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuickEntryTimeRow
   */  
export function get_QuickEntryTimes_Company_EmpID_QuickEntryType_QuickEntryCode(Company:string, EmpID:string, QuickEntryType:string, QuickEntryCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuickEntryTimeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/QuickEntryTimes(" + Company + "," + EmpID + "," + QuickEntryType + "," + QuickEntryCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuickEntryTimeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QuickEntryTime for the service
   Description: Calls UpdateExt to update QuickEntryTime. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuickEntryTime
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param QuickEntryType Desc: QuickEntryType   Required: True   Allow empty value : True
      @param QuickEntryCode Desc: QuickEntryCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuickEntryTimeRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QuickEntryTimes_Company_EmpID_QuickEntryType_QuickEntryCode(Company:string, EmpID:string, QuickEntryType:string, QuickEntryCode:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/QuickEntryTimes(" + Company + "," + EmpID + "," + QuickEntryType + "," + QuickEntryCode + ")", {
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
   Summary: Call UpdateExt to delete QuickEntryTime item
   Description: Call UpdateExt to delete QuickEntryTime item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuickEntryTime
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param QuickEntryType Desc: QuickEntryType   Required: True   Allow empty value : True
      @param QuickEntryCode Desc: QuickEntryCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QuickEntryTimes_Company_EmpID_QuickEntryType_QuickEntryCode(Company:string, EmpID:string, QuickEntryType:string, QuickEntryCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/QuickEntryTimes(" + Company + "," + EmpID + "," + QuickEntryType + "," + QuickEntryCode + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EmpBasicListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpBasicListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpBasicListRow)
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
export function get_GetRows(whereClauseEmpBasic:string, whereClauseQuickEntryExpense:string, whereClauseQuickEntryTime:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseEmpBasic!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseEmpBasic=" + whereClauseEmpBasic
   }
   if(typeof whereClauseQuickEntryExpense!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQuickEntryExpense=" + whereClauseQuickEntryExpense
   }
   if(typeof whereClauseQuickEntryTime!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQuickEntryTime=" + whereClauseQuickEntryTime
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/GetRows" + params, {
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(empID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof empID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "empID=" + empID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/GetList" + params, {
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
   Summary: Invoke method GetCodeDescList
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCodeDescList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/GetCodeDescList", {
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
   Summary: Invoke method OnChangeIndirectCode
   Description: Method to call when changing the Indirect Code
   OperationID: OnChangeIndirectCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeIndirectCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeIndirectCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeIndirectCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/OnChangeIndirectCode", {
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
   Summary: Invoke method OnChangeLaborType
   Description: Method to call when changing the Labor Type
   OperationID: OnChangeLaborType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeLaborType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeLaborType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeLaborType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/OnChangeLaborType", {
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
   Summary: Invoke method OnChangeMiscCode
   Description: Method to call when changing the Miscellaneous Code.
   OperationID: OnChangeMiscCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMiscCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMiscCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/OnChangeMiscCode", {
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
   Summary: Invoke method OnChangeOprSeq
   Description: Method to call when changing the Operation Sequence
   OperationID: OnChangeOprSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOprSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOprSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOprSeq(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/OnChangeOprSeq", {
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
   Summary: Invoke method OnChangePaymentMethod
   Description: Method to call when changing the Payment Method.
   OperationID: OnChangePaymentMethod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePaymentMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePaymentMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePaymentMethod(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/OnChangePaymentMethod", {
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
   Summary: Invoke method OnChangePhaseID
   Description: Method to call when changing the Phase ID.
   OperationID: OnChangePhaseID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePhaseID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePhaseID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePhaseID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/OnChangePhaseID", {
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
   Summary: Invoke method OnChangeProjectID
   Description: Method to call when changing the Project ID.
   OperationID: OnChangeProjectID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeProjectID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeProjectID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeProjectID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/OnChangeProjectID", {
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
   Summary: Invoke method OnChangeRoleCd
   Description: This method defaults dataset fields when the RoleCd field changes.
   OperationID: OnChangeRoleCd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeRoleCd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeRoleCd_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeRoleCd(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/OnChangeRoleCd", {
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
   Summary: Invoke method BuildRoleCodeWhereClause
   OperationID: BuildRoleCodeWhereClause
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildRoleCodeWhereClause_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildRoleCodeWhereClause_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildRoleCodeWhereClause(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/BuildRoleCodeWhereClause", {
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
   Summary: Invoke method EmployeeExists
   OperationID: EmployeeExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EmployeeExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EmployeeExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EmployeeExists(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/EmployeeExists", {
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
   Summary: Invoke method IsEmpAuthToBookTime
   OperationID: IsEmpAuthToBookTime
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsEmpAuthToBookTime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsEmpAuthToBookTime_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsEmpAuthToBookTime(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/IsEmpAuthToBookTime", {
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
   Summary: Invoke method GetFilteredRoleCdList
   Description: Returns Filtered Role Codes.
   OperationID: GetFilteredRoleCdList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFilteredRoleCdList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFilteredRoleCdList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFilteredRoleCdList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/GetFilteredRoleCdList", {
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
   Summary: Invoke method GetNewEmpBasic
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEmpBasic
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEmpBasic_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEmpBasic_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewEmpBasic(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/GetNewEmpBasic", {
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
   Summary: Invoke method GetNewQuickEntryExpense
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuickEntryExpense
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuickEntryExpense_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuickEntryExpense_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQuickEntryExpense(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/GetNewQuickEntryExpense", {
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
   Summary: Invoke method GetNewQuickEntryTime
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuickEntryTime
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuickEntryTime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuickEntryTime_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQuickEntryTime(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/GetNewQuickEntryTime", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpBasicListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_EmpBasicListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpBasicRow{
   "odatametadata":string,
   "value":Erp_Tablesets_EmpBasicRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuickEntryExpenseRow{
   "odatametadata":string,
   "value":Erp_Tablesets_QuickEntryExpenseRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuickEntryTimeRow{
   "odatametadata":string,
   "value":Erp_Tablesets_QuickEntryTimeRow[],
}

export interface Erp_Tablesets_EmpBasicListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "EmpID":string,
      /**  First name of employee.  */  
   "FirstName":string,
      /**  Middle name of employee.  */  
   "MiddleInitial":string,
      /**  Last name of employee  */  
   "LastName":string,
      /**  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  */  
   "Name":string,
      /**  Home phone number  */  
   "Phone":string,
      /**  Normal work shift.  Value is to be defaulted from XASyst.DefaultShift (Production/Data Collection tab in Company Configuration) when available, otherwise it is not defaulted.  */  
   "Shift":number,
      /**  Labor rate that is used for Job Costing.  */  
   "LaborRate":number,
      /**  An internally assigned flag that Indicates if the employee needs to be established in payroll. (Existence of PREmpMas). This flag is used to allow payroll employee maintenance view new employees created by job costing that were flagged as being "Payroll" employees.  */  
   "PRSetupReq":boolean,
      /**  Indicates the employment status. Can be A-Active, I-InActive or T-Terminated.  */  
   "EmpStatus":string,
      /**  Name of file that contains the employee's photo image.  This can be blank (no photo available).  Employee photos are stored in the following directory structure ManufacturingSystem\Emphoto\(Company ID). directory  */  
   "PhotoFile":string,
      /**   The Job Department in which the employee works work was done. An optional field. If entered must be valid in JCDept table.
Used by data collection in the "Work Que" window to provide a default department to view.  */  
   "JCDept":string,
      /**   The ID of the Supervisor for the employee.  The Supervisor ID is actually the EmpID used for supervisor's PREmpMas record.
Validation: Can't be blank, if entered must be found in the PREmpMas file.  */  
   "SupervisorID":string,
      /**  This person usually goes out on service calls  */  
   "ServTech":boolean,
      /**   Links the employee to a UserID.  This link is used by the Shop Floor Menu(SFM).  In the SFM, the user signs on with their employee id instead of a User id. This link grants the menu security authorizations of the User to the employee. It also defines the language to be used.
Note: An employee can only be related to one UserFile record. Each UserFile, can be related to many employees.  Therefore, you might set up a few generic Users per language, or based on security levels or you might set up a user for each employee. Note: Many transactions, are stamped with the UserID, thus if you use generic users you will be tracking to the individual employee.
This field is OPTIONAL. However, employee will not be allowed to login to the SFM without a being linked to a UserID.  Also, the company of the employee must be an authorized company of the user. This is validated by the finding a record in UserComp table, using EmpBasic.Company, EmpBasic.DCDUserID.  */  
   "DcdUserID":string,
      /**  Indicates if this employee is a shop supervisor. This must be checked for employee to use the Shop Floor Menu Supervisor options.  */  
   "ShopSupervisor":boolean,
      /**  A warehouse manager has the access to the Manager's Queue tab in the Material Request Queue.  */  
   "WarehouseManager":boolean,
      /**  Resource Group ID for this employee, only allowed if the Project Billing module licensed.  */  
   "ResourceGrpID":string,
      /**  Resource D for this employee, only allowed if the Project Billing module licensed.  */  
   "ResourceID":string,
      /**  SupervisorName  */  
   "SupervisorName":string,
   "ShiftDescription":string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "ResourceGroupDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_EmpBasicRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "EmpID":string,
      /**  First name of employee.  */  
   "FirstName":string,
      /**  Middle name of employee.  */  
   "MiddleInitial":string,
      /**  Last name of employee  */  
   "LastName":string,
      /**  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  */  
   "Name":string,
      /**  First Address Line  */  
   "Address":string,
      /**  Second Address Line  */  
   "Address2":string,
      /**  City portion of address  */  
   "City":string,
      /**  Home State. Can be blank.  */  
   "State":string,
      /**  Postal Code or Zip code portion of address  */  
   "ZIP":string,
      /**  Country is used as part of the mailing address. It can be left blank.  */  
   "Country":string,
      /**  Home phone number  */  
   "Phone":string,
      /**  Emergency Phone number  */  
   "EmgPhone":string,
      /**  Normal work shift.  Value is to be defaulted from XASyst.DefaultShift (Production/Data Collection tab in Company Configuration) when available, otherwise it is not defaulted.  */  
   "Shift":number,
      /**  Labor rate that is used for Job Costing.  */  
   "LaborRate":number,
      /**   Indicates if this employee is should be paid through the Manufacturing System payroll module.  This does not mean they have been setup in payroll, only that they should be.
Once setup in payroll (existence of corresponding PREmpMas record) this field cannot be changed.  */  
   "Payroll":boolean,
      /**  An internally assigned flag that Indicates if the employee needs to be established in payroll. (Existence of PREmpMas). This flag is used to allow payroll employee maintenance view new employees created by job costing that were flagged as being "Payroll" employees.  */  
   "PRSetupReq":boolean,
      /**  Indicates the employment status. Can be A-Active, I-InActive or T-Terminated.  */  
   "EmpStatus":string,
      /**   The default expense code that will be for direct labor hours reported by this employee.  This must be valid in the LabExpCd master file.
This will be used unless labor is reported where the JobHead.ExpenseCode is not blank.  */  
   "ExpenseCode":string,
      /**  Name of file that contains the employee's photo image.  This can be blank (no photo available).  Employee photos are stored in the following directory structure ManufacturingSystem\Emphoto\(Company ID). directory  */  
   "PhotoFile":string,
      /**   The Job Department in which the employee works work was done. An optional field. If entered must be valid in JCDept table.
Used by data collection in the "Work Que" window to provide a default department to view.  */  
   "JCDept":string,
      /**  Emergency contact name.  */  
   "EmgContact":string,
      /**   The ID of the Supervisor for the employee.  The Supervisor ID is actually the EmpID used for supervisor's PREmpMas record.
Validation: Can't be blank, if entered must be found in the PREmpMas file.  */  
   "SupervisorID":string,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   "CountryNum":number,
      /**  This person usually goes out on service calls  */  
   "ServTech":boolean,
      /**  Email address of the Employee.  */  
   "EMailAddress":string,
      /**   Links the employee to a UserID.  This link is used by the Shop Floor Menu(SFM).  In the SFM, the user signs on with their employee id instead of a User id. This link grants the menu security authorizations of the User to the employee. It also defines the language to be used.
Note: An employee can only be related to one UserFile record. Each UserFile, can be related to many employees.  Therefore, you might set up a few generic Users per language, or based on security levels or you might set up a user for each employee. Note: Many transactions, are stamped with the UserID, thus if you use generic users you will be tracking to the individual employee.
This field is OPTIONAL. However, employee will not be allowed to login to the SFM without a being linked to a UserID.  Also, the company of the employee must be an authorized company of the user. This is validated by the finding a record in UserComp table, using EmpBasic.Company, EmpBasic.DCDUserID.  */  
   "DcdUserID":string,
      /**  Indicates if this employee works on the manufacturing line. This must be checked for employee to use the Shop Floor Menu production options.  */  
   "ProductionWorker":boolean,
      /**  Indicates if this employee is a material handler. This must be checked for employee to use the Shop Floor Menu material handler options.  */  
   "MaterialHandler":boolean,
      /**  Indicates if this employee is a shop supervisor. This must be checked for employee to use the Shop Floor Menu Supervisor options.  */  
   "ShopSupervisor":boolean,
      /**   Pertains to Data Collection only.
Indicates if the employee is allowed report completed quantities.  */  
   "CanReportQty":boolean,
      /**   Pertains to Data Collection only.
Indicates if the job/asm/opr can be overriden when reporting completed quantity.  If NO, then they will only be allowed to report against a job/asm/opr that they are currently working on (active labordtl record ) or where the job is open and the operation is marked as "quantity only" reporting .  If YES, they can enter the quantity for any open job without first having to do a start activity function.
( See also EmpBasic.CanReportQty )  */  
   "CanOverrideJob":boolean,
      /**   Pertains to Data Collection/Advanced Material Management only.
Indicates if the employee is allowed make requests for materials.  */  
   "CanRequestMaterial":boolean,
      /**   Pertains to Data Collection only.
Indicates if the employee is allowed report scrap quantities.  */  
   "CanReportScrapQty":boolean,
      /**   Pertains to Data Collection only.
Indicates if the employee is allowed report nonconformance quantities.  */  
   "CanReportNCQty":boolean,
      /**  Indicates if this employee is a Shipping/Receiving worker. This must be checked for employee to use the Shop Floor Menu Shipping/Receiving options.  */  
   "ShipRecv":boolean,
      /**  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "CnvEmpID":string,
      /**  A warehouse manager has the access to the Manager's Queue tab in the Material Request Queue.  */  
   "WarehouseManager":boolean,
      /**  Employee is able to override a hard allocation against inventory and select it from another Bin during the process of picking and packing orders, as long as it is not allocated to another Sales Order, Job or Transfer Order.  */  
   "CanOverrideAllocations":boolean,
      /**  If false the shop employee will not be allowed to book time to manufacturing jobs.  */  
   "AllowDirLbr":boolean,
      /**  True indicates that the shop employee is on contract rather than paid via the payroll. This flag is then used in the advanced billing invoice preparation process.  */  
   "ContractEmp":boolean,
      /**  Resource Group ID for this employee, only allowed if the Project Billing module licensed.  */  
   "ResourceGrpID":string,
      /**  Resource D for this employee, only allowed if the Project Billing module licensed.  */  
   "ResourceID":string,
      /**  Unique identifier of the workflow group for this employee's Time transactions.  */  
   "TimeWFGroupID":string,
      /**  This value will be true if the Employee is allowed to enter Expense.  */  
   "ExpenseEntryAllowed":boolean,
      /**  Unique identifier of the workflow group for this employee's Expense transactions.  */  
   "ExpenseWFGroupID":string,
      /**  The Supplier Number associated to the Employee for Expense entry.  */  
   "ExpenseVendorNum":number,
      /**  Unique identifier for a PerCon record.  */  
   "PerConID":number,
      /**  Default to True. If unchecked then changes to the Name fields on PerCon won't affect this record and vice versa.  */  
   "SyncNameToPerCon":boolean,
      /**  Default to True. If unchecked then changes to the Address fields on PerCon won't affect this record and visa versa.  */  
   "SyncAddressToPerCon":boolean,
      /**  Default to True. If unchecked then changes to the Phone fields on PerCon won't affect this record and vice versa.  */  
   "SyncPhoneToPerCon":boolean,
      /**  Default to True. If unchecked then changes to the email fields on PerCon won't affect this record and vice versa.  */  
   "SyncEmailToPerCon":boolean,
      /**   Pertains to Time Management.
Maintains whether the employee is allowed to enter Indirect time.  */  
   "CanEnterIndirectTime":boolean,
      /**   Pertains to Time Management.
Maintains whether the employee is allowed to enter Production time.  */  
   "CanEnterProductionTime":boolean,
      /**   Pertains to Time Management.
Maintains whether the employee is allowed to enter Project time.  */  
   "CanEnterProjectTime":boolean,
      /**   Pertains to Time Management.
Maintains whether the employee is allowed to enter Service time.  */  
   "CanEnterServiceTime":boolean,
      /**   Pertains to Time Management.
Maintains whether the employee is allowed to enter Setup time.  */  
   "CanEnterSetupTime":boolean,
      /**  Time transactions for the employee requiring employee approval logic will automatically be approved.  */  
   "TimeAutoApprove":boolean,
      /**  Expense transactions for the employee requiring employee approval logic will automatically be approved.  */  
   "ExpenseAutoApprove":boolean,
      /**  Mobile Password  */  
   "MobileUserPassword":string,
      /**  Default is True.  Determines if an employee can enter time with a labor type of Indirect.  If True, an employee may select Indirect labor type.  If false, employee may not select Indirect labor type in Time Entry.  */  
   "AllowIndirect":boolean,
      /**  Default is True.  Determines if an employee can enter time with a labor type of Production.  If True, an employee may select Production labor type.  If false, employee may not select Production labor type in Time Entry.  */  
   "AllowProduction":boolean,
      /**  Default is True.  Determines if an employee can enter time with a labor type of Project.  If True, an employee may select Project labor type.  If false, employee may not select Project labor type in Time Entry.  */  
   "AllowProject":boolean,
      /**  Default is True.  Determines if an employee can enter time with a labor type of Service.  If True, an employee may select Service labor type.  If false, employee may not select Service labor type in Time Entry.  */  
   "AllowService":boolean,
      /**  Default is True.  Determines if an employee can enter time with a labor type of Setup.  If True, an employee may select Setup labor type.  If false, employee may not select Setup labor type in Time Entry.  */  
   "AllowSetup":boolean,
      /**   Correlates to LaborType.  Indicates the type of labor transaction, however "Production" LaborType can be broken out into "Project", "Production" or "Service".  Valid Values are "I" = Indirect, "P" - Production, "S" - Setup, "J" - Project, or "V" - Service.
This value controls what fields are displayed/prompted for. 
"I" Indirect does not use JobNum, LotNum, SetupPctCmp, OprComplete, OpCode, LaborQty, ScrapQty, ScrapReasonCode, Rework, ReworkReasonCode.
"S" Setup does not use IndirectCode.
"P" Production does not use IndirectCode or SetupPctCmp,  */  
   "DefaultLaborTypePseudo":string,
      /**  Time Type Code  */  
   "DefaultTimeTypCd":string,
      /**  A code that links to the Indirect master record that describes the type of indirect labor for this transaction. This field IS DIRECTLY ENTERED, not via a description/selection list method.   This is only valid when LaborType = "I" and must then be valid.  */  
   "DefaultIndirectCode":string,
      /**  The expense code for this labor transaction. An expense code is a abbreviated method of indirectly assigning a G/L account for the labor expense. DEFAULTS: for direct labor;  use the JobHead.ExpenseCode if its non-blank,  else use the Employee.ExpenseCode.                                                                   For Indirect Labor use the Indirect.ExpenseCode if not blank, else use the employee.ExpenseCode.  */  
   "DefaultExpenseCode":string,
      /**   The Resource Group in which the labor was performed.  This code IS DIRECTLY entered in labor entry, instead of the finding it based on the description.  This is mandatory and must be valid in the Resource Group table.
For production labor (LaborType = "S" or "P") the default is from the JobOper.PrimaryProdDtl JobOpDtl.ResourceGrpID.
For indirect labor (LaborType = I) there is no default.  */  
   "DefaultResourceGrpID":string,
      /**  The ID of the Resource that was used to do the work. This field will be used to run reports using LaborDtl records to show how much work has been done on a specific Resource. This ID is directly entered in labor entry and Labor collection. It is only prompted for if the JcSyst.MachinePrompt = Yes/  */  
   "DefaultResourceID":string,
      /**  Labor hours are used in calculating labor cost for a job. It is stored as hours-hundredths. It is calculated whenever the start/stop time is changed. It can then be overridden.  */  
   "DefaultLaborHrs":number,
      /**  The currency the expense occurred in.  */  
   "DefaultExpCurrencyCode":string,
      /**  The currency the claim amounts are in.  */  
   "DefaultClaimCurrencyCode":string,
      /**  The payment method of the expense.  */  
   "DefaultPMUID":number,
      /**  The Tax Region for this expense.  */  
   "DefaultTaxRegionCode":string,
      /**  Indicates if the expense amount includes tax.  */  
   "DefaultTaxIncluded":boolean,
      /**  This value will be true if the Employee is allowed to enter Expense for advance requests.  */  
   "ExpenseAdvReqAllowed":boolean,
      /**  Unique identifier of the workflow group for this employee's Expense advance request transactions.  */  
   "ExpenseAdvReqWFGroupID":string,
      /**  Advance request expense transactions for the employee requiring employee approval logic will automatically be approved.  */  
   "ExpenseAdvReqAutoApprove":boolean,
      /**  MobileResourceID  */  
   "MobileResourceID":string,
      /**  AllowAsAltRemitTo  */  
   "AllowAsAltRemitTo":boolean,
      /**  UserNameInJDF  */  
   "UserNameInJDF":string,
      /**  Indicates the record is used with Machine MES  */  
   "ExternalMES":boolean,
      /**  PermitScrap  */  
   "PermitScrap":boolean,
      /**  PermitDown  */  
   "PermitDown":boolean,
      /**  PermitHelp  */  
   "PermitHelp":boolean,
      /**  PermitJobControl  */  
   "PermitJobControl":boolean,
      /**  PermitNextJobControl  */  
   "PermitNextJobControl":boolean,
      /**  PermitManualSqc  */  
   "PermitManualSqc":boolean,
      /**  PermitVariableSqc  */  
   "PermitVariableSqc":boolean,
      /**  PermitAttributeSqc  */  
   "PermitAttributeSqc":boolean,
      /**  PermitMaterialLot  */  
   "PermitMaterialLot":boolean,
      /**  PermitSetupMaterial  */  
   "PermitSetupMaterial":boolean,
      /**  PermitCavities  */  
   "PermitCavities":boolean,
      /**  PermitPercentRegrind  */  
   "PermitPercentRegrind":boolean,
      /**  PermitSaveProfile  */  
   "PermitSaveProfile":boolean,
      /**  PermitCalibration  */  
   "PermitCalibration":boolean,
      /**  PermitMachinePm  */  
   "PermitMachinePm":boolean,
      /**  PermitToolPm  */  
   "PermitToolPm":boolean,
      /**  PermitLanguage  */  
   "PermitLanguage":boolean,
      /**  PermitPreferences  */  
   "PermitPreferences":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The purpose of the flag is to disallow an employee to enter their own time in Time and Expense Entry  */  
   "DisallowTimeEntry":boolean,
      /**  Indicates that an employee can execute inbound related transactions on the shop floor. The default for the check box is unchecked.  */  
   "PkgInboundAllowed":boolean,
      /**  Indicates that an employee can execute outbound related transactions on the shop floor. The default for the check box is unchecked.  */  
   "PkgOutboundAllowed":boolean,
      /**  Indicates that an employee can execute inventory related transactions on the shop floor. The default for the check box is unchecked.  */  
   "PkgInventoryAllowed":boolean,
      /**  Indicates that an employee can execute manufacturing related transactions on the shop floor. The default for the check box is unchecked.  */  
   "PkgManufacturingAllowed":boolean,
      /**  Indicates that an employee can execute quality related transactions on the shop floor. The default for the check box is unchecked.  */  
   "PkgQualityAllowed":boolean,
      /**  ImageID  */  
   "ImageID":string,
      /**  Package Control Activity setting to indicate if the employee is allowed to print during the Master and MixedMaster.  */  
   "PkgMasterMixedPrint":boolean,
      /**  PkgSuppressPrintMessages  */  
   "PkgSuppressPrintMessages":boolean,
      /**  PayrollValuesForHCM  */  
   "PayrollValuesForHCM":string,
      /**  Determines if the employee has to be synchronized with Epicor FSA application.  */  
   "SendToFSA":boolean,
      /**  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  */  
   "ExternalMESSyncRequired":boolean,
      /**  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  */  
   "ExternalMESLastSync":string,
      /**  Identity Document  */  
   "IDDocument":string,
      /**  Birthdate  */  
   "BirthDate":string,
      /**  Sex  */  
   "Sex":string,
      /**  Department  */  
   "Department":string,
      /**  Enrollment Date  */  
   "EnrollmentDate":string,
      /**  Departure Date  */  
   "DepartureDate":string,
      /**  Should this employee receive email alert messages.  */  
   "AlertFlag":boolean,
      /**  Department Description  */  
   "DepartmentDescription":string,
      /**  external field for UI to use to know whether it should enable or disable the ExpenseVendorNumVendorID field.  */  
   "EnableExpenseSupplier":boolean,
      /**  Expense Description  */  
   "ExpenseDescription":string,
      /**  Indicates whether the user is allowed to create Expense transactions in Time and Expense Entry for another employee for which they are an Approver.  */  
   "ExpenseDisableCreate":boolean,
   "ExpenseRestrictEntry":boolean,
      /**  Payroll record has been found so changes to many fields are disallowed.  */  
   "FoundPayroll":boolean,
      /**  Payroll record has been found so changes to many fields are disallowed, but the user is in the employee's payroll class so can see the labor rate field  */  
   "FoundPayrollUserAllowed":boolean,
      /**  String value which contains the validations for the HCM Integration, possible values NON(Nothing configured), HDR (Header) DTL (Detail)  */  
   "HCMEnabledAt":string,
      /**  External field used on Employee Entry in order to enable/disable HCM configuration  */  
   "IsHCMAllowedByEmp":boolean,
      /**  Displays blank if "Allow Override Integrate Labor Pay Hours at Employee" checkbox in Site configuration is unchecked and Employee's value if checked.  */  
   "PayrollValuesForHCMDsp":string,
   "PerConName":string,
      /**  Path to the photo file if it exists.  */  
   "PhotoFilePath":string,
      /**  Flag used to indicate that the generate fill shop capacity process needs to be run to update the ShopCap records because new records won't be added due performance.  */  
   "SetShopLoad":boolean,
      /**  Shift end time in Hours:Minute format., used by Shop Tracker  */  
   "ShiftEndTime":string,
      /**  Shift start time in Hours:Minutes format  */  
   "ShiftStartTime":string,
      /**  SupervisorName  */  
   "SupervisorName":string,
      /**  Indicates whether the user is allowed to create a Time transaction in Time and Expense Entry for another employee for which they are an Approver.  */  
   "TimeDisableCreate":boolean,
   "TimeRestrictEntry":boolean,
      /**  User ID Name  */  
   "UserIDName":string,
   "CalendarID":string,
      /**  List of fields which are referenced by COA segments.  */  
   "COASegReferences":string,
      /**  This column used to display Time Approval Task tree in MetaUI  */  
   "TimeApprovalTasksTree":string,
      /**  This column used to display Time Approval Task tree in MetaUI  */  
   "ExpenseApprovalTasksTree":string,
   "ShiftLength":number,
   "BitFlag":number,
   "CompanySendToFSA":boolean,
   "CountryNumDescription":string,
   "ExpenseCodeDescription":string,
   "ExpenseVendorNumName":string,
   "ExpenseVendorNumCity":string,
   "ExpenseVendorNumTermsCode":string,
   "ExpenseVendorNumAddress3":string,
   "ExpenseVendorNumDefaultFOB":string,
   "ExpenseVendorNumCurrencyCode":string,
   "ExpenseVendorNumZIP":string,
   "ExpenseVendorNumVendorID":string,
   "ExpenseVendorNumAddress2":string,
   "ExpenseVendorNumAddress1":string,
   "ExpenseVendorNumCountry":string,
   "ExpenseVendorNumState":string,
   "JCDeptDescription":string,
   "MachineDescription":string,
   "ResourceDescription":string,
   "ResourceGroupDescription":string,
   "ShiftDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_QuickEntryExpenseRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "EmpID":string,
      /**  Defines whether the Quick Entry Code relates to Time or Expenses.  */  
   "QuickEntryType":string,
      /**  Unique identifier of this Quick Entry Code.  */  
   "QuickEntryCode":string,
      /**  This value is used to set the value for the Project.  */  
   "ProjectID":string,
      /**  This value is used to set the value for WBS Phase.  */  
   "PhaseID":string,
      /**  If Quick Entry Type is Expense, this value is used to set the quick value for Indirect Expense.  */  
   "IndirectExpense":boolean,
      /**  If Quick Entry Type is Expense, this value is used to set the quick value for Payment Method.  */  
   "PMUID":number,
      /**  If Quick Entry Type is Expense, this value is used to set the quick value for Miscellaneous Charge ID.  */  
   "MiscCode":string,
      /**  If Quick Entry Type is Expense, this value is used to set the quick value for Reimbursable.  */  
   "Reimbursable":boolean,
      /**  If Quick Entry Type is Expense, this value is used to set the quick value for Tax Liability.  */  
   "TaxRegionCode":string,
      /**  If Quick Entry Type is Expense, this value is used to set the quick value for Expense Currency.  */  
   "CurrencyCode":string,
      /**  If Quick Entry Type is Expense, this value is used to set the quick value for Tax Included.  */  
   "TaxIncluded":boolean,
      /**  The currency the claim amounts are in.  */  
   "ClaimCurrencyCode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Currency Description  */  
   "CurrencyCodeDescription":string,
      /**  Claim Currency Description  */  
   "ClaimCurrencyCodeDescription":string,
   "BitFlag":number,
   "MiscCodeLCAmount":number,
   "MiscCodeLCCurrencyCode":string,
   "MiscCodeLCDisburseMethod":string,
   "MiscCodeExpUnitBased":boolean,
   "MiscCodeDescription":string,
   "PayMethodType":number,
   "PayMethodName":string,
   "PayMethodSummarizePerCustomer":boolean,
   "PhaseDescription":string,
   "PurMiscDescription":string,
   "PurMiscLCDisburseMethod":string,
   "PurMiscLCAmount":number,
   "PurMiscLCCurrencyCode":string,
   "TaxRegionCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_QuickEntryTimeRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "EmpID":string,
      /**  Defines whether the Quick Entry Code relates to Time or Expenses.  */  
   "QuickEntryType":string,
      /**  Unique identifier of this Quick Entry Code.  */  
   "QuickEntryCode":string,
      /**  Defines whether the Quick Entry Code is related to Project, Production or Indirect labor.  Relates only to Time Quick Entry Codes.  Valid values are P (Production) and I (Indirect).  */  
   "LaborType":string,
      /**  This value is used to set the value for the Project.  */  
   "ProjectID":string,
      /**  This value is used to set the value for WBS Phase.  */  
   "PhaseID":string,
      /**  This value is used to set the Time Type Code.  Relates only to Time Quick Entry Codes.  */  
   "TimeTypCd":string,
      /**  This value is used to set the value for Job.  Relates only to Time Quick Entry Codes.  */  
   "JobNum":string,
      /**  This value is used to set the value for Assembly.  Relates only to Time Quick Entry Codes.  */  
   "AssemblySeq":number,
      /**  This value is used to set the value for Operation.  Relates only to Time Quick Entry Codes.  */  
   "OprSeq":number,
      /**  This value is used to set the value for Project Role Code.  Relates only to Time Quick Entry Codes.  */  
   "RoleCode":string,
      /**  This value is used to set the value for Indirect Code.  Relates only to Time Quick Entry Codes where the Labor Type is Indirect.  */  
   "IndirectCode":string,
      /**  The Expense Code for the labor transaction.  */  
   "ExpenseCode":string,
      /**  The Resource Group in which the labor is performed.  */  
   "ResourceGrpID":string,
      /**  The Resource that was used to do the work.  */  
   "ResourceID":string,
      /**  Labor hours.  */  
   "LaborHrs":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "RoleSelectionDisabled":boolean,
   "TimeTypSelectionDisabled":boolean,
   "BitFlag":number,
   "ExpenseCodeDescription":string,
   "IndirectCodeDescription":string,
   "PhaseDescription":string,
   "ResourceDescription":string,
   "ResourceGrpDescription":string,
   "RoleCodeRoleDescription":string,
   "TimeTypeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param iEmpID
      @param iProjID
      @param iJobNum
      @param iAssSeq
      @param iOprSeq
   */  
export interface BuildRoleCodeWhereClause_input{
   iEmpID:string,
   iProjID:string,
   iJobNum:string,
   iAssSeq:number,
   iOprSeq:number,
}

export interface BuildRoleCodeWhereClause_output{
   returnObj:string,
}

   /** Required : 
      @param empID
   */  
export interface DeleteByID_input{
   empID:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param empID
   */  
export interface EmployeeExists_input{
   empID:string,
}

export interface EmployeeExists_output{
   returnObj:boolean,
}

export interface Erp_Tablesets_EmpBasicListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   EmpID:string,
      /**  First name of employee.  */  
   FirstName:string,
      /**  Middle name of employee.  */  
   MiddleInitial:string,
      /**  Last name of employee  */  
   LastName:string,
      /**  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  */  
   Name:string,
      /**  Home phone number  */  
   Phone:string,
      /**  Normal work shift.  Value is to be defaulted from XASyst.DefaultShift (Production/Data Collection tab in Company Configuration) when available, otherwise it is not defaulted.  */  
   Shift:number,
      /**  Labor rate that is used for Job Costing.  */  
   LaborRate:number,
      /**  An internally assigned flag that Indicates if the employee needs to be established in payroll. (Existence of PREmpMas). This flag is used to allow payroll employee maintenance view new employees created by job costing that were flagged as being "Payroll" employees.  */  
   PRSetupReq:boolean,
      /**  Indicates the employment status. Can be A-Active, I-InActive or T-Terminated.  */  
   EmpStatus:string,
      /**  Name of file that contains the employee's photo image.  This can be blank (no photo available).  Employee photos are stored in the following directory structure ManufacturingSystem\Emphoto\(Company ID). directory  */  
   PhotoFile:string,
      /**   The Job Department in which the employee works work was done. An optional field. If entered must be valid in JCDept table.
Used by data collection in the "Work Que" window to provide a default department to view.  */  
   JCDept:string,
      /**   The ID of the Supervisor for the employee.  The Supervisor ID is actually the EmpID used for supervisor's PREmpMas record.
Validation: Can't be blank, if entered must be found in the PREmpMas file.  */  
   SupervisorID:string,
      /**  This person usually goes out on service calls  */  
   ServTech:boolean,
      /**   Links the employee to a UserID.  This link is used by the Shop Floor Menu(SFM).  In the SFM, the user signs on with their employee id instead of a User id. This link grants the menu security authorizations of the User to the employee. It also defines the language to be used.
Note: An employee can only be related to one UserFile record. Each UserFile, can be related to many employees.  Therefore, you might set up a few generic Users per language, or based on security levels or you might set up a user for each employee. Note: Many transactions, are stamped with the UserID, thus if you use generic users you will be tracking to the individual employee.
This field is OPTIONAL. However, employee will not be allowed to login to the SFM without a being linked to a UserID.  Also, the company of the employee must be an authorized company of the user. This is validated by the finding a record in UserComp table, using EmpBasic.Company, EmpBasic.DCDUserID.  */  
   DcdUserID:string,
      /**  Indicates if this employee is a shop supervisor. This must be checked for employee to use the Shop Floor Menu Supervisor options.  */  
   ShopSupervisor:boolean,
      /**  A warehouse manager has the access to the Manager's Queue tab in the Material Request Queue.  */  
   WarehouseManager:boolean,
      /**  Resource Group ID for this employee, only allowed if the Project Billing module licensed.  */  
   ResourceGrpID:string,
      /**  Resource D for this employee, only allowed if the Project Billing module licensed.  */  
   ResourceID:string,
      /**  SupervisorName  */  
   SupervisorName:string,
   ShiftDescription:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   ResourceGroupDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_EmpBasicListTableset{
   EmpBasicList:Erp_Tablesets_EmpBasicListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_EmpBasicRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   EmpID:string,
      /**  First name of employee.  */  
   FirstName:string,
      /**  Middle name of employee.  */  
   MiddleInitial:string,
      /**  Last name of employee  */  
   LastName:string,
      /**  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  */  
   Name:string,
      /**  First Address Line  */  
   Address:string,
      /**  Second Address Line  */  
   Address2:string,
      /**  City portion of address  */  
   City:string,
      /**  Home State. Can be blank.  */  
   State:string,
      /**  Postal Code or Zip code portion of address  */  
   ZIP:string,
      /**  Country is used as part of the mailing address. It can be left blank.  */  
   Country:string,
      /**  Home phone number  */  
   Phone:string,
      /**  Emergency Phone number  */  
   EmgPhone:string,
      /**  Normal work shift.  Value is to be defaulted from XASyst.DefaultShift (Production/Data Collection tab in Company Configuration) when available, otherwise it is not defaulted.  */  
   Shift:number,
      /**  Labor rate that is used for Job Costing.  */  
   LaborRate:number,
      /**   Indicates if this employee is should be paid through the Manufacturing System payroll module.  This does not mean they have been setup in payroll, only that they should be.
Once setup in payroll (existence of corresponding PREmpMas record) this field cannot be changed.  */  
   Payroll:boolean,
      /**  An internally assigned flag that Indicates if the employee needs to be established in payroll. (Existence of PREmpMas). This flag is used to allow payroll employee maintenance view new employees created by job costing that were flagged as being "Payroll" employees.  */  
   PRSetupReq:boolean,
      /**  Indicates the employment status. Can be A-Active, I-InActive or T-Terminated.  */  
   EmpStatus:string,
      /**   The default expense code that will be for direct labor hours reported by this employee.  This must be valid in the LabExpCd master file.
This will be used unless labor is reported where the JobHead.ExpenseCode is not blank.  */  
   ExpenseCode:string,
      /**  Name of file that contains the employee's photo image.  This can be blank (no photo available).  Employee photos are stored in the following directory structure ManufacturingSystem\Emphoto\(Company ID). directory  */  
   PhotoFile:string,
      /**   The Job Department in which the employee works work was done. An optional field. If entered must be valid in JCDept table.
Used by data collection in the "Work Que" window to provide a default department to view.  */  
   JCDept:string,
      /**  Emergency contact name.  */  
   EmgContact:string,
      /**   The ID of the Supervisor for the employee.  The Supervisor ID is actually the EmpID used for supervisor's PREmpMas record.
Validation: Can't be blank, if entered must be found in the PREmpMas file.  */  
   SupervisorID:string,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   CountryNum:number,
      /**  This person usually goes out on service calls  */  
   ServTech:boolean,
      /**  Email address of the Employee.  */  
   EMailAddress:string,
      /**   Links the employee to a UserID.  This link is used by the Shop Floor Menu(SFM).  In the SFM, the user signs on with their employee id instead of a User id. This link grants the menu security authorizations of the User to the employee. It also defines the language to be used.
Note: An employee can only be related to one UserFile record. Each UserFile, can be related to many employees.  Therefore, you might set up a few generic Users per language, or based on security levels or you might set up a user for each employee. Note: Many transactions, are stamped with the UserID, thus if you use generic users you will be tracking to the individual employee.
This field is OPTIONAL. However, employee will not be allowed to login to the SFM without a being linked to a UserID.  Also, the company of the employee must be an authorized company of the user. This is validated by the finding a record in UserComp table, using EmpBasic.Company, EmpBasic.DCDUserID.  */  
   DcdUserID:string,
      /**  Indicates if this employee works on the manufacturing line. This must be checked for employee to use the Shop Floor Menu production options.  */  
   ProductionWorker:boolean,
      /**  Indicates if this employee is a material handler. This must be checked for employee to use the Shop Floor Menu material handler options.  */  
   MaterialHandler:boolean,
      /**  Indicates if this employee is a shop supervisor. This must be checked for employee to use the Shop Floor Menu Supervisor options.  */  
   ShopSupervisor:boolean,
      /**   Pertains to Data Collection only.
Indicates if the employee is allowed report completed quantities.  */  
   CanReportQty:boolean,
      /**   Pertains to Data Collection only.
Indicates if the job/asm/opr can be overriden when reporting completed quantity.  If NO, then they will only be allowed to report against a job/asm/opr that they are currently working on (active labordtl record ) or where the job is open and the operation is marked as "quantity only" reporting .  If YES, they can enter the quantity for any open job without first having to do a start activity function.
( See also EmpBasic.CanReportQty )  */  
   CanOverrideJob:boolean,
      /**   Pertains to Data Collection/Advanced Material Management only.
Indicates if the employee is allowed make requests for materials.  */  
   CanRequestMaterial:boolean,
      /**   Pertains to Data Collection only.
Indicates if the employee is allowed report scrap quantities.  */  
   CanReportScrapQty:boolean,
      /**   Pertains to Data Collection only.
Indicates if the employee is allowed report nonconformance quantities.  */  
   CanReportNCQty:boolean,
      /**  Indicates if this employee is a Shipping/Receiving worker. This must be checked for employee to use the Shop Floor Menu Shipping/Receiving options.  */  
   ShipRecv:boolean,
      /**  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   CnvEmpID:string,
      /**  A warehouse manager has the access to the Manager's Queue tab in the Material Request Queue.  */  
   WarehouseManager:boolean,
      /**  Employee is able to override a hard allocation against inventory and select it from another Bin during the process of picking and packing orders, as long as it is not allocated to another Sales Order, Job or Transfer Order.  */  
   CanOverrideAllocations:boolean,
      /**  If false the shop employee will not be allowed to book time to manufacturing jobs.  */  
   AllowDirLbr:boolean,
      /**  True indicates that the shop employee is on contract rather than paid via the payroll. This flag is then used in the advanced billing invoice preparation process.  */  
   ContractEmp:boolean,
      /**  Resource Group ID for this employee, only allowed if the Project Billing module licensed.  */  
   ResourceGrpID:string,
      /**  Resource D for this employee, only allowed if the Project Billing module licensed.  */  
   ResourceID:string,
      /**  Unique identifier of the workflow group for this employee's Time transactions.  */  
   TimeWFGroupID:string,
      /**  This value will be true if the Employee is allowed to enter Expense.  */  
   ExpenseEntryAllowed:boolean,
      /**  Unique identifier of the workflow group for this employee's Expense transactions.  */  
   ExpenseWFGroupID:string,
      /**  The Supplier Number associated to the Employee for Expense entry.  */  
   ExpenseVendorNum:number,
      /**  Unique identifier for a PerCon record.  */  
   PerConID:number,
      /**  Default to True. If unchecked then changes to the Name fields on PerCon won't affect this record and vice versa.  */  
   SyncNameToPerCon:boolean,
      /**  Default to True. If unchecked then changes to the Address fields on PerCon won't affect this record and visa versa.  */  
   SyncAddressToPerCon:boolean,
      /**  Default to True. If unchecked then changes to the Phone fields on PerCon won't affect this record and vice versa.  */  
   SyncPhoneToPerCon:boolean,
      /**  Default to True. If unchecked then changes to the email fields on PerCon won't affect this record and vice versa.  */  
   SyncEmailToPerCon:boolean,
      /**   Pertains to Time Management.
Maintains whether the employee is allowed to enter Indirect time.  */  
   CanEnterIndirectTime:boolean,
      /**   Pertains to Time Management.
Maintains whether the employee is allowed to enter Production time.  */  
   CanEnterProductionTime:boolean,
      /**   Pertains to Time Management.
Maintains whether the employee is allowed to enter Project time.  */  
   CanEnterProjectTime:boolean,
      /**   Pertains to Time Management.
Maintains whether the employee is allowed to enter Service time.  */  
   CanEnterServiceTime:boolean,
      /**   Pertains to Time Management.
Maintains whether the employee is allowed to enter Setup time.  */  
   CanEnterSetupTime:boolean,
      /**  Time transactions for the employee requiring employee approval logic will automatically be approved.  */  
   TimeAutoApprove:boolean,
      /**  Expense transactions for the employee requiring employee approval logic will automatically be approved.  */  
   ExpenseAutoApprove:boolean,
      /**  Mobile Password  */  
   MobileUserPassword:string,
      /**  Default is True.  Determines if an employee can enter time with a labor type of Indirect.  If True, an employee may select Indirect labor type.  If false, employee may not select Indirect labor type in Time Entry.  */  
   AllowIndirect:boolean,
      /**  Default is True.  Determines if an employee can enter time with a labor type of Production.  If True, an employee may select Production labor type.  If false, employee may not select Production labor type in Time Entry.  */  
   AllowProduction:boolean,
      /**  Default is True.  Determines if an employee can enter time with a labor type of Project.  If True, an employee may select Project labor type.  If false, employee may not select Project labor type in Time Entry.  */  
   AllowProject:boolean,
      /**  Default is True.  Determines if an employee can enter time with a labor type of Service.  If True, an employee may select Service labor type.  If false, employee may not select Service labor type in Time Entry.  */  
   AllowService:boolean,
      /**  Default is True.  Determines if an employee can enter time with a labor type of Setup.  If True, an employee may select Setup labor type.  If false, employee may not select Setup labor type in Time Entry.  */  
   AllowSetup:boolean,
      /**   Correlates to LaborType.  Indicates the type of labor transaction, however "Production" LaborType can be broken out into "Project", "Production" or "Service".  Valid Values are "I" = Indirect, "P" - Production, "S" - Setup, "J" - Project, or "V" - Service.
This value controls what fields are displayed/prompted for. 
"I" Indirect does not use JobNum, LotNum, SetupPctCmp, OprComplete, OpCode, LaborQty, ScrapQty, ScrapReasonCode, Rework, ReworkReasonCode.
"S" Setup does not use IndirectCode.
"P" Production does not use IndirectCode or SetupPctCmp,  */  
   DefaultLaborTypePseudo:string,
      /**  Time Type Code  */  
   DefaultTimeTypCd:string,
      /**  A code that links to the Indirect master record that describes the type of indirect labor for this transaction. This field IS DIRECTLY ENTERED, not via a description/selection list method.   This is only valid when LaborType = "I" and must then be valid.  */  
   DefaultIndirectCode:string,
      /**  The expense code for this labor transaction. An expense code is a abbreviated method of indirectly assigning a G/L account for the labor expense. DEFAULTS: for direct labor;  use the JobHead.ExpenseCode if its non-blank,  else use the Employee.ExpenseCode.                                                                   For Indirect Labor use the Indirect.ExpenseCode if not blank, else use the employee.ExpenseCode.  */  
   DefaultExpenseCode:string,
      /**   The Resource Group in which the labor was performed.  This code IS DIRECTLY entered in labor entry, instead of the finding it based on the description.  This is mandatory and must be valid in the Resource Group table.
For production labor (LaborType = "S" or "P") the default is from the JobOper.PrimaryProdDtl JobOpDtl.ResourceGrpID.
For indirect labor (LaborType = I) there is no default.  */  
   DefaultResourceGrpID:string,
      /**  The ID of the Resource that was used to do the work. This field will be used to run reports using LaborDtl records to show how much work has been done on a specific Resource. This ID is directly entered in labor entry and Labor collection. It is only prompted for if the JcSyst.MachinePrompt = Yes/  */  
   DefaultResourceID:string,
      /**  Labor hours are used in calculating labor cost for a job. It is stored as hours-hundredths. It is calculated whenever the start/stop time is changed. It can then be overridden.  */  
   DefaultLaborHrs:number,
      /**  The currency the expense occurred in.  */  
   DefaultExpCurrencyCode:string,
      /**  The currency the claim amounts are in.  */  
   DefaultClaimCurrencyCode:string,
      /**  The payment method of the expense.  */  
   DefaultPMUID:number,
      /**  The Tax Region for this expense.  */  
   DefaultTaxRegionCode:string,
      /**  Indicates if the expense amount includes tax.  */  
   DefaultTaxIncluded:boolean,
      /**  This value will be true if the Employee is allowed to enter Expense for advance requests.  */  
   ExpenseAdvReqAllowed:boolean,
      /**  Unique identifier of the workflow group for this employee's Expense advance request transactions.  */  
   ExpenseAdvReqWFGroupID:string,
      /**  Advance request expense transactions for the employee requiring employee approval logic will automatically be approved.  */  
   ExpenseAdvReqAutoApprove:boolean,
      /**  MobileResourceID  */  
   MobileResourceID:string,
      /**  AllowAsAltRemitTo  */  
   AllowAsAltRemitTo:boolean,
      /**  UserNameInJDF  */  
   UserNameInJDF:string,
      /**  Indicates the record is used with Machine MES  */  
   ExternalMES:boolean,
      /**  PermitScrap  */  
   PermitScrap:boolean,
      /**  PermitDown  */  
   PermitDown:boolean,
      /**  PermitHelp  */  
   PermitHelp:boolean,
      /**  PermitJobControl  */  
   PermitJobControl:boolean,
      /**  PermitNextJobControl  */  
   PermitNextJobControl:boolean,
      /**  PermitManualSqc  */  
   PermitManualSqc:boolean,
      /**  PermitVariableSqc  */  
   PermitVariableSqc:boolean,
      /**  PermitAttributeSqc  */  
   PermitAttributeSqc:boolean,
      /**  PermitMaterialLot  */  
   PermitMaterialLot:boolean,
      /**  PermitSetupMaterial  */  
   PermitSetupMaterial:boolean,
      /**  PermitCavities  */  
   PermitCavities:boolean,
      /**  PermitPercentRegrind  */  
   PermitPercentRegrind:boolean,
      /**  PermitSaveProfile  */  
   PermitSaveProfile:boolean,
      /**  PermitCalibration  */  
   PermitCalibration:boolean,
      /**  PermitMachinePm  */  
   PermitMachinePm:boolean,
      /**  PermitToolPm  */  
   PermitToolPm:boolean,
      /**  PermitLanguage  */  
   PermitLanguage:boolean,
      /**  PermitPreferences  */  
   PermitPreferences:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The purpose of the flag is to disallow an employee to enter their own time in Time and Expense Entry  */  
   DisallowTimeEntry:boolean,
      /**  Indicates that an employee can execute inbound related transactions on the shop floor. The default for the check box is unchecked.  */  
   PkgInboundAllowed:boolean,
      /**  Indicates that an employee can execute outbound related transactions on the shop floor. The default for the check box is unchecked.  */  
   PkgOutboundAllowed:boolean,
      /**  Indicates that an employee can execute inventory related transactions on the shop floor. The default for the check box is unchecked.  */  
   PkgInventoryAllowed:boolean,
      /**  Indicates that an employee can execute manufacturing related transactions on the shop floor. The default for the check box is unchecked.  */  
   PkgManufacturingAllowed:boolean,
      /**  Indicates that an employee can execute quality related transactions on the shop floor. The default for the check box is unchecked.  */  
   PkgQualityAllowed:boolean,
      /**  ImageID  */  
   ImageID:string,
      /**  Package Control Activity setting to indicate if the employee is allowed to print during the Master and MixedMaster.  */  
   PkgMasterMixedPrint:boolean,
      /**  PkgSuppressPrintMessages  */  
   PkgSuppressPrintMessages:boolean,
      /**  PayrollValuesForHCM  */  
   PayrollValuesForHCM:string,
      /**  Determines if the employee has to be synchronized with Epicor FSA application.  */  
   SendToFSA:boolean,
      /**  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  */  
   ExternalMESSyncRequired:boolean,
      /**  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  */  
   ExternalMESLastSync:string,
      /**  Identity Document  */  
   IDDocument:string,
      /**  Birthdate  */  
   BirthDate:string,
      /**  Sex  */  
   Sex:string,
      /**  Department  */  
   Department:string,
      /**  Enrollment Date  */  
   EnrollmentDate:string,
      /**  Departure Date  */  
   DepartureDate:string,
      /**  Should this employee receive email alert messages.  */  
   AlertFlag:boolean,
      /**  Department Description  */  
   DepartmentDescription:string,
      /**  external field for UI to use to know whether it should enable or disable the ExpenseVendorNumVendorID field.  */  
   EnableExpenseSupplier:boolean,
      /**  Expense Description  */  
   ExpenseDescription:string,
      /**  Indicates whether the user is allowed to create Expense transactions in Time and Expense Entry for another employee for which they are an Approver.  */  
   ExpenseDisableCreate:boolean,
   ExpenseRestrictEntry:boolean,
      /**  Payroll record has been found so changes to many fields are disallowed.  */  
   FoundPayroll:boolean,
      /**  Payroll record has been found so changes to many fields are disallowed, but the user is in the employee's payroll class so can see the labor rate field  */  
   FoundPayrollUserAllowed:boolean,
      /**  String value which contains the validations for the HCM Integration, possible values NON(Nothing configured), HDR (Header) DTL (Detail)  */  
   HCMEnabledAt:string,
      /**  External field used on Employee Entry in order to enable/disable HCM configuration  */  
   IsHCMAllowedByEmp:boolean,
      /**  Displays blank if "Allow Override Integrate Labor Pay Hours at Employee" checkbox in Site configuration is unchecked and Employee's value if checked.  */  
   PayrollValuesForHCMDsp:string,
   PerConName:string,
      /**  Path to the photo file if it exists.  */  
   PhotoFilePath:string,
      /**  Flag used to indicate that the generate fill shop capacity process needs to be run to update the ShopCap records because new records won't be added due performance.  */  
   SetShopLoad:boolean,
      /**  Shift end time in Hours:Minute format., used by Shop Tracker  */  
   ShiftEndTime:string,
      /**  Shift start time in Hours:Minutes format  */  
   ShiftStartTime:string,
      /**  SupervisorName  */  
   SupervisorName:string,
      /**  Indicates whether the user is allowed to create a Time transaction in Time and Expense Entry for another employee for which they are an Approver.  */  
   TimeDisableCreate:boolean,
   TimeRestrictEntry:boolean,
      /**  User ID Name  */  
   UserIDName:string,
   CalendarID:string,
      /**  List of fields which are referenced by COA segments.  */  
   COASegReferences:string,
      /**  This column used to display Time Approval Task tree in MetaUI  */  
   TimeApprovalTasksTree:string,
      /**  This column used to display Time Approval Task tree in MetaUI  */  
   ExpenseApprovalTasksTree:string,
   ShiftLength:number,
   BitFlag:number,
   CompanySendToFSA:boolean,
   CountryNumDescription:string,
   ExpenseCodeDescription:string,
   ExpenseVendorNumName:string,
   ExpenseVendorNumCity:string,
   ExpenseVendorNumTermsCode:string,
   ExpenseVendorNumAddress3:string,
   ExpenseVendorNumDefaultFOB:string,
   ExpenseVendorNumCurrencyCode:string,
   ExpenseVendorNumZIP:string,
   ExpenseVendorNumVendorID:string,
   ExpenseVendorNumAddress2:string,
   ExpenseVendorNumAddress1:string,
   ExpenseVendorNumCountry:string,
   ExpenseVendorNumState:string,
   JCDeptDescription:string,
   MachineDescription:string,
   ResourceDescription:string,
   ResourceGroupDescription:string,
   ShiftDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_QuickEntryExpenseRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   EmpID:string,
      /**  Defines whether the Quick Entry Code relates to Time or Expenses.  */  
   QuickEntryType:string,
      /**  Unique identifier of this Quick Entry Code.  */  
   QuickEntryCode:string,
      /**  This value is used to set the value for the Project.  */  
   ProjectID:string,
      /**  This value is used to set the value for WBS Phase.  */  
   PhaseID:string,
      /**  If Quick Entry Type is Expense, this value is used to set the quick value for Indirect Expense.  */  
   IndirectExpense:boolean,
      /**  If Quick Entry Type is Expense, this value is used to set the quick value for Payment Method.  */  
   PMUID:number,
      /**  If Quick Entry Type is Expense, this value is used to set the quick value for Miscellaneous Charge ID.  */  
   MiscCode:string,
      /**  If Quick Entry Type is Expense, this value is used to set the quick value for Reimbursable.  */  
   Reimbursable:boolean,
      /**  If Quick Entry Type is Expense, this value is used to set the quick value for Tax Liability.  */  
   TaxRegionCode:string,
      /**  If Quick Entry Type is Expense, this value is used to set the quick value for Expense Currency.  */  
   CurrencyCode:string,
      /**  If Quick Entry Type is Expense, this value is used to set the quick value for Tax Included.  */  
   TaxIncluded:boolean,
      /**  The currency the claim amounts are in.  */  
   ClaimCurrencyCode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Currency Description  */  
   CurrencyCodeDescription:string,
      /**  Claim Currency Description  */  
   ClaimCurrencyCodeDescription:string,
   BitFlag:number,
   MiscCodeLCAmount:number,
   MiscCodeLCCurrencyCode:string,
   MiscCodeLCDisburseMethod:string,
   MiscCodeExpUnitBased:boolean,
   MiscCodeDescription:string,
   PayMethodType:number,
   PayMethodName:string,
   PayMethodSummarizePerCustomer:boolean,
   PhaseDescription:string,
   PurMiscDescription:string,
   PurMiscLCDisburseMethod:string,
   PurMiscLCAmount:number,
   PurMiscLCCurrencyCode:string,
   TaxRegionCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_QuickEntryTableset{
   EmpBasic:Erp_Tablesets_EmpBasicRow[],
   QuickEntryExpense:Erp_Tablesets_QuickEntryExpenseRow[],
   QuickEntryTime:Erp_Tablesets_QuickEntryTimeRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_QuickEntryTimeRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   EmpID:string,
      /**  Defines whether the Quick Entry Code relates to Time or Expenses.  */  
   QuickEntryType:string,
      /**  Unique identifier of this Quick Entry Code.  */  
   QuickEntryCode:string,
      /**  Defines whether the Quick Entry Code is related to Project, Production or Indirect labor.  Relates only to Time Quick Entry Codes.  Valid values are P (Production) and I (Indirect).  */  
   LaborType:string,
      /**  This value is used to set the value for the Project.  */  
   ProjectID:string,
      /**  This value is used to set the value for WBS Phase.  */  
   PhaseID:string,
      /**  This value is used to set the Time Type Code.  Relates only to Time Quick Entry Codes.  */  
   TimeTypCd:string,
      /**  This value is used to set the value for Job.  Relates only to Time Quick Entry Codes.  */  
   JobNum:string,
      /**  This value is used to set the value for Assembly.  Relates only to Time Quick Entry Codes.  */  
   AssemblySeq:number,
      /**  This value is used to set the value for Operation.  Relates only to Time Quick Entry Codes.  */  
   OprSeq:number,
      /**  This value is used to set the value for Project Role Code.  Relates only to Time Quick Entry Codes.  */  
   RoleCode:string,
      /**  This value is used to set the value for Indirect Code.  Relates only to Time Quick Entry Codes where the Labor Type is Indirect.  */  
   IndirectCode:string,
      /**  The Expense Code for the labor transaction.  */  
   ExpenseCode:string,
      /**  The Resource Group in which the labor is performed.  */  
   ResourceGrpID:string,
      /**  The Resource that was used to do the work.  */  
   ResourceID:string,
      /**  Labor hours.  */  
   LaborHrs:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   RoleSelectionDisabled:boolean,
   TimeTypSelectionDisabled:boolean,
   BitFlag:number,
   ExpenseCodeDescription:string,
   IndirectCodeDescription:string,
   PhaseDescription:string,
   ResourceDescription:string,
   ResourceGrpDescription:string,
   RoleCodeRoleDescription:string,
   TimeTypeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtQuickEntryTableset{
   EmpBasic:Erp_Tablesets_EmpBasicRow[],
   QuickEntryExpense:Erp_Tablesets_QuickEntryExpenseRow[],
   QuickEntryTime:Erp_Tablesets_QuickEntryTimeRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param empID
   */  
export interface GetByID_input{
   empID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_QuickEntryTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_QuickEntryTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_QuickEntryTableset[],
}

   /** Required : 
      @param tableName
      @param fieldName
   */  
export interface GetCodeDescList_input{
   tableName:string,
   fieldName:string,
}

export interface GetCodeDescList_output{
   returnObj:string,
}

   /** Required : 
      @param iEmpID
      @param iProjID
      @param iJobNum
      @param iAssSeq
      @param iOprSeq
   */  
export interface GetFilteredRoleCdList_input{
   iEmpID:string,
   iProjID:string,
   iJobNum:string,
   iAssSeq:number,
   iOprSeq:number,
}

export interface GetFilteredRoleCdList_output{
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
   returnObj:Erp_Tablesets_EmpBasicListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewEmpBasic_input{
   ds:Erp_Tablesets_QuickEntryTableset[],
}

export interface GetNewEmpBasic_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuickEntryTableset[],
}
}

   /** Required : 
      @param ds
      @param empID
      @param quickEntryType
   */  
export interface GetNewQuickEntryExpense_input{
   ds:Erp_Tablesets_QuickEntryTableset[],
   empID:string,
   quickEntryType:string,
}

export interface GetNewQuickEntryExpense_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuickEntryTableset[],
}
}

   /** Required : 
      @param ds
      @param empID
      @param quickEntryType
   */  
export interface GetNewQuickEntryTime_input{
   ds:Erp_Tablesets_QuickEntryTableset[],
   empID:string,
   quickEntryType:string,
}

export interface GetNewQuickEntryTime_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuickEntryTableset[],
}
}

   /** Required : 
      @param whereClauseEmpBasic
      @param whereClauseQuickEntryExpense
      @param whereClauseQuickEntryTime
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseEmpBasic:string,
   whereClauseQuickEntryExpense:string,
   whereClauseQuickEntryTime:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_QuickEntryTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
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

   /** Required : 
      @param iEmpID
      @param iProjID
   */  
export interface IsEmpAuthToBookTime_input{
   iEmpID:string,
   iProjID:string,
}

export interface IsEmpAuthToBookTime_output{
   returnObj:boolean,
}

   /** Required : 
      @param proposedIndirectCode
      @param ds
   */  
export interface OnChangeIndirectCode_input{
      /**  The proposed Indirect Code  */  
   proposedIndirectCode:string,
   ds:Erp_Tablesets_QuickEntryTableset[],
}

export interface OnChangeIndirectCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuickEntryTableset[],
}
}

   /** Required : 
      @param proposedLaborType
      @param ds
   */  
export interface OnChangeLaborType_input{
      /**  The proposed Labor Type  */  
   proposedLaborType:string,
   ds:Erp_Tablesets_QuickEntryTableset[],
}

export interface OnChangeLaborType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuickEntryTableset[],
}
}

   /** Required : 
      @param proposedMiscCode
      @param ds
   */  
export interface OnChangeMiscCode_input{
      /**  The proposed miscellaneous code  */  
   proposedMiscCode:string,
   ds:Erp_Tablesets_QuickEntryTableset[],
}

export interface OnChangeMiscCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuickEntryTableset[],
}
}

   /** Required : 
      @param proposedOprSeq
      @param ds
   */  
export interface OnChangeOprSeq_input{
      /**  The proposed Operation Sequence  */  
   proposedOprSeq:number,
   ds:Erp_Tablesets_QuickEntryTableset[],
}

export interface OnChangeOprSeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuickEntryTableset[],
}
}

   /** Required : 
      @param proposedPMUID
      @param ds
   */  
export interface OnChangePaymentMethod_input{
      /**  The proposed pay method id  */  
   proposedPMUID:number,
   ds:Erp_Tablesets_QuickEntryTableset[],
}

export interface OnChangePaymentMethod_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuickEntryTableset[],
}
}

   /** Required : 
      @param proposedPhaseID
      @param ds
   */  
export interface OnChangePhaseID_input{
      /**  The proposed phase ID  */  
   proposedPhaseID:string,
   ds:Erp_Tablesets_QuickEntryTableset[],
}

export interface OnChangePhaseID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuickEntryTableset[],
}
}

   /** Required : 
      @param proposedProjectID
      @param ds
   */  
export interface OnChangeProjectID_input{
      /**  The proposed project ID  */  
   proposedProjectID:string,
   ds:Erp_Tablesets_QuickEntryTableset[],
}

export interface OnChangeProjectID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuickEntryTableset[],
}
}

   /** Required : 
      @param ds
      @param ipRoleCd
   */  
export interface OnChangeRoleCd_input{
   ds:Erp_Tablesets_QuickEntryTableset[],
      /**  Proposed RoleCd change  */  
   ipRoleCd:string,
}

export interface OnChangeRoleCd_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuickEntryTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtQuickEntryTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtQuickEntryTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_QuickEntryTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuickEntryTableset[],
}
}

