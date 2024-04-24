import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.CreditCardProcSvc
// Description: Add your summary for this object here
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/$metadata", {
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
   Description: Get CreditCardProcs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CreditCardProcs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CreditCardProcRow
   */  
export function get_CreditCardProcs(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CreditCardProcRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/CreditCardProcs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CreditCardProcRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CreditCardProcs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CreditCardProcRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CreditCardProcRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreditCardProcs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/CreditCardProcs", {
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
   Summary: Calls GetByID to retrieve the CreditCardProc item
   Description: Calls GetByID to retrieve the CreditCardProc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CreditCardProc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CreditCardProcRow
   */  
export function get_CreditCardProcs_Company(Company:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CreditCardProcRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/CreditCardProcs(" + Company + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CreditCardProcRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CreditCardProc for the service
   Description: Calls UpdateExt to update CreditCardProc. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CreditCardProc
      @param Company Desc: Company   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CreditCardProcRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CreditCardProcs_Company(Company:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/CreditCardProcs(" + Company + ")", {
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
   Summary: Call UpdateExt to delete CreditCardProc item
   Description: Call UpdateExt to delete CreditCardProc item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CreditCardProc
      @param Company Desc: Company   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CreditCardProcs_Company(Company:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/CreditCardProcs(" + Company + ")", {
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
   Description: Get CreditCardProcessors items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CreditCardProcessors1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CreditCardProcessorRow
   */  
export function get_CreditCardProcs_Company_CreditCardProcessors(Company:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CreditCardProcessorRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/CreditCardProcs(" + Company + ")/CreditCardProcessors", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CreditCardProcessorRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CreditCardProcessor item
   Description: Calls GetByID to retrieve the CreditCardProcessor item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CreditCardProcessor1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProcessorNum Desc: ProcessorNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CreditCardProcessorRow
   */  
export function get_CreditCardProcs_Company_CreditCardProcessors_Company_ProcessorNum(Company:string, ProcessorNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CreditCardProcessorRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/CreditCardProcs(" + Company + ")/CreditCardProcessors(" + Company + "," + ProcessorNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CreditCardProcessorRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get CreditCardProcessors items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CreditCardProcessors
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CreditCardProcessorRow
   */  
export function get_CreditCardProcessors(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CreditCardProcessorRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/CreditCardProcessors", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CreditCardProcessorRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CreditCardProcessors
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CreditCardProcessorRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CreditCardProcessorRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreditCardProcessors(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/CreditCardProcessors", {
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
   Summary: Calls GetByID to retrieve the CreditCardProcessor item
   Description: Calls GetByID to retrieve the CreditCardProcessor item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CreditCardProcessor
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProcessorNum Desc: ProcessorNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CreditCardProcessorRow
   */  
export function get_CreditCardProcessors_Company_ProcessorNum(Company:string, ProcessorNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CreditCardProcessorRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/CreditCardProcessors(" + Company + "," + ProcessorNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CreditCardProcessorRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CreditCardProcessor for the service
   Description: Calls UpdateExt to update CreditCardProcessor. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CreditCardProcessor
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProcessorNum Desc: ProcessorNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CreditCardProcessorRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CreditCardProcessors_Company_ProcessorNum(Company:string, ProcessorNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/CreditCardProcessors(" + Company + "," + ProcessorNum + ")", {
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
   Summary: Call UpdateExt to delete CreditCardProcessor item
   Description: Call UpdateExt to delete CreditCardProcessor item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CreditCardProcessor
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProcessorNum Desc: ProcessorNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CreditCardProcessors_Company_ProcessorNum(Company:string, ProcessorNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/CreditCardProcessors(" + Company + "," + ProcessorNum + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CreditCardProcListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CreditCardProcListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CreditCardProcListRow)
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
export function get_GetRows(whereClauseCreditCardProc:string, whereClauseCreditCardProcessor:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseCreditCardProc!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCreditCardProc=" + whereClauseCreditCardProc
   }
   if(typeof whereClauseCreditCardProcessor!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCreditCardProcessor=" + whereClauseCreditCardProcessor
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/GetRows" + params, {
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/GetByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/GetList" + params, {
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
   Summary: Invoke method OnChangeProcessor
   Description: This method validates the Processor ID
   OperationID: OnChangeProcessor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeProcessor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeProcessor_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeProcessor(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/OnChangeProcessor", {
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
   Summary: Invoke method HasPendingAuthorizations
   Description: Returns if there is any authorization, unused, succeeded transaction.
   OperationID: HasPendingAuthorizations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/HasPendingAuthorizations_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_HasPendingAuthorizations(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/HasPendingAuthorizations", {
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
   Summary: Invoke method HasProcessorPendingAuthorizations
   Description: Returns if there is any unused success authorization for the processor.
   OperationID: HasProcessorPendingAuthorizations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/HasProcessorPendingAuthorizations_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/HasProcessorPendingAuthorizations_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_HasProcessorPendingAuthorizations(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/HasProcessorPendingAuthorizations", {
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
   Summary: Invoke method GetNewCreditCardProc
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCreditCardProc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCreditCardProc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCreditCardProc_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCreditCardProc(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/GetNewCreditCardProc", {
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
   Summary: Invoke method GetNewCreditCardProcessor
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCreditCardProcessor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCreditCardProcessor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCreditCardProcessor_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCreditCardProcessor(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/GetNewCreditCardProcessor", {
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
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteByID(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CreditCardProcListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CreditCardProcListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CreditCardProcRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CreditCardProcRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CreditCardProcessorRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CreditCardProcessorRow[],
}

export interface Erp_Tablesets_CreditCardProcListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Processor Interface code  */  
   "ProcInterfaceCode":string,
      /**  Processor Interface Description  */  
   "ProcInterfaceDesc":string,
      /**  Host Address  */  
   "HostAddress":string,
      /**  Host Port number  */  
   "HostPort":number,
      /**  Time Out  */  
   "TimeOut":number,
      /**  L = Low, M = Medium  */  
   "Verbosity":string,
      /**  Proxy Address  */  
   "ProxyAddress":string,
      /**  Proxy Port number  */  
   "ProxyPort":number,
      /**  Proxy Logon  */  
   "ProxyLogon":string,
      /**  Proxy Password  */  
   "ProxyPwd":string,
      /**  Allow Deposit Payments on Sales Orders  */  
   "AllowDepPay":boolean,
      /**  Failed DEPOSIT becomes SALE transaction  */  
   "FailDepToSalesTrans":boolean,
      /**  Credit card failure stops shipment  */  
   "FailStopsShip":boolean,
      /**  Reauthorize remaining balance on back order  */  
   "ReauthRemaining":boolean,
      /**  Number of days to retain credit card information  */  
   "DaysToRetainInfo":number,
      /**  Reauthorize before picking  */  
   "ReauthBeforePick":boolean,
      /**  Reauthorize credit card after number of days as passed  */  
   "ReauthAfterDays":number,
      /**  Reauthorize if Above value  */  
   "ReauthAbove":number,
      /**  Validate using CSC Code  */  
   "UseCSC":boolean,
      /**  Ignore CSC validation failure  */  
   "IgnoreCSCFail":boolean,
      /**  Use Address + Zip to verify credit card  */  
   "UseAVS":boolean,
      /**  Ignore address validation failure  */  
   "IgnoreAVSFail":boolean,
      /**  Indicates if the credit card transactions will be logged.  */  
   "IsTest":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CreditCardProcRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Processor Interface code  */  
   "ProcInterfaceCode":string,
      /**  Processor Interface Description  */  
   "ProcInterfaceDesc":string,
      /**  Host Address  */  
   "HostAddress":string,
      /**  Host Port number  */  
   "HostPort":number,
      /**  Time Out  */  
   "TimeOut":number,
      /**  L = Low, M = Medium  */  
   "Verbosity":string,
      /**  Proxy Address  */  
   "ProxyAddress":string,
      /**  Proxy Port number  */  
   "ProxyPort":number,
      /**  Proxy Logon  */  
   "ProxyLogon":string,
      /**  Proxy Password  */  
   "ProxyPwd":string,
      /**  Allow Deposit Payments on Sales Orders  */  
   "AllowDepPay":boolean,
      /**  Failed DEPOSIT becomes SALE transaction  */  
   "FailDepToSalesTrans":boolean,
      /**  Credit card failure stops shipment  */  
   "FailStopsShip":boolean,
      /**  Reauthorize remaining balance on back order  */  
   "ReauthRemaining":boolean,
      /**  Number of days to retain credit card information  */  
   "DaysToRetainInfo":number,
      /**  Reauthorize before picking  */  
   "ReauthBeforePick":boolean,
      /**  Reauthorize credit card after number of days as passed  */  
   "ReauthAfterDays":number,
      /**  Reauthorize if Above value  */  
   "ReauthAbove":number,
      /**  Validate using CSC Code  */  
   "UseCSC":boolean,
      /**  Ignore CSC validation failure  */  
   "IgnoreCSCFail":boolean,
      /**  Use Address + Zip to verify credit card  */  
   "UseAVS":boolean,
      /**  Ignore address validation failure  */  
   "IgnoreAVSFail":boolean,
      /**  Indicates if the credit card transactions will be logged.  */  
   "IsTest":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Host Address for the Paygate Hosted Token Service.  */  
   "PayGateHostAddress":string,
      /**  NameSpace for the Paygate Hosted Token Service.  */  
   "PayGateNameSpace":string,
      /**  Public Key for the Paygate Hosted Token Service EWA component.  */  
   "PayGatePublicKey":string,
      /**  Indicates if the credit card setup will be using a testing Paygate instance for transactions. Force requests to use Paygate test url: paygate-test1.eaglesoa.com.  */  
   "IsTraining":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CreditCardProcessorRow{
      /**  Company  */  
   "Company":string,
      /**  ProcessorNum  */  
   "ProcessorNum":number,
      /**  Processor  */  
   "Processor":string,
      /**  ProcessorDesc  */  
   "ProcessorDesc":string,
      /**  Partner  */  
   "Partner":string,
      /**  PartnerUser  */  
   "PartnerUser":string,
      /**  PartnerVendor  */  
   "PartnerVendor":string,
      /**  PartnerPwd  */  
   "PartnerPwd":string,
      /**  TPPID  */  
   "TPPID":string,
      /**  FDMSGroupID  */  
   "FDMSGroupID":string,
      /**  FDMSCustomerID  */  
   "FDMSCustomerID":string,
      /**  FDMSPhoneNum  */  
   "FDMSPhoneNum":string,
      /**  BankAcctID  */  
   "BankAcctID":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  Credit Card Masked password field  */  
   "PartnerPwdMasked":string,
   "BitFlag":number,
   "BankAcctDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
export interface DeleteByID_output{
}

export interface Erp_Tablesets_CreditCardProcListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Processor Interface code  */  
   ProcInterfaceCode:string,
      /**  Processor Interface Description  */  
   ProcInterfaceDesc:string,
      /**  Host Address  */  
   HostAddress:string,
      /**  Host Port number  */  
   HostPort:number,
      /**  Time Out  */  
   TimeOut:number,
      /**  L = Low, M = Medium  */  
   Verbosity:string,
      /**  Proxy Address  */  
   ProxyAddress:string,
      /**  Proxy Port number  */  
   ProxyPort:number,
      /**  Proxy Logon  */  
   ProxyLogon:string,
      /**  Proxy Password  */  
   ProxyPwd:string,
      /**  Allow Deposit Payments on Sales Orders  */  
   AllowDepPay:boolean,
      /**  Failed DEPOSIT becomes SALE transaction  */  
   FailDepToSalesTrans:boolean,
      /**  Credit card failure stops shipment  */  
   FailStopsShip:boolean,
      /**  Reauthorize remaining balance on back order  */  
   ReauthRemaining:boolean,
      /**  Number of days to retain credit card information  */  
   DaysToRetainInfo:number,
      /**  Reauthorize before picking  */  
   ReauthBeforePick:boolean,
      /**  Reauthorize credit card after number of days as passed  */  
   ReauthAfterDays:number,
      /**  Reauthorize if Above value  */  
   ReauthAbove:number,
      /**  Validate using CSC Code  */  
   UseCSC:boolean,
      /**  Ignore CSC validation failure  */  
   IgnoreCSCFail:boolean,
      /**  Use Address + Zip to verify credit card  */  
   UseAVS:boolean,
      /**  Ignore address validation failure  */  
   IgnoreAVSFail:boolean,
      /**  Indicates if the credit card transactions will be logged.  */  
   IsTest:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CreditCardProcListTableset{
   CreditCardProcList:Erp_Tablesets_CreditCardProcListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CreditCardProcRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Processor Interface code  */  
   ProcInterfaceCode:string,
      /**  Processor Interface Description  */  
   ProcInterfaceDesc:string,
      /**  Host Address  */  
   HostAddress:string,
      /**  Host Port number  */  
   HostPort:number,
      /**  Time Out  */  
   TimeOut:number,
      /**  L = Low, M = Medium  */  
   Verbosity:string,
      /**  Proxy Address  */  
   ProxyAddress:string,
      /**  Proxy Port number  */  
   ProxyPort:number,
      /**  Proxy Logon  */  
   ProxyLogon:string,
      /**  Proxy Password  */  
   ProxyPwd:string,
      /**  Allow Deposit Payments on Sales Orders  */  
   AllowDepPay:boolean,
      /**  Failed DEPOSIT becomes SALE transaction  */  
   FailDepToSalesTrans:boolean,
      /**  Credit card failure stops shipment  */  
   FailStopsShip:boolean,
      /**  Reauthorize remaining balance on back order  */  
   ReauthRemaining:boolean,
      /**  Number of days to retain credit card information  */  
   DaysToRetainInfo:number,
      /**  Reauthorize before picking  */  
   ReauthBeforePick:boolean,
      /**  Reauthorize credit card after number of days as passed  */  
   ReauthAfterDays:number,
      /**  Reauthorize if Above value  */  
   ReauthAbove:number,
      /**  Validate using CSC Code  */  
   UseCSC:boolean,
      /**  Ignore CSC validation failure  */  
   IgnoreCSCFail:boolean,
      /**  Use Address + Zip to verify credit card  */  
   UseAVS:boolean,
      /**  Ignore address validation failure  */  
   IgnoreAVSFail:boolean,
      /**  Indicates if the credit card transactions will be logged.  */  
   IsTest:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Host Address for the Paygate Hosted Token Service.  */  
   PayGateHostAddress:string,
      /**  NameSpace for the Paygate Hosted Token Service.  */  
   PayGateNameSpace:string,
      /**  Public Key for the Paygate Hosted Token Service EWA component.  */  
   PayGatePublicKey:string,
      /**  Indicates if the credit card setup will be using a testing Paygate instance for transactions. Force requests to use Paygate test url: paygate-test1.eaglesoa.com.  */  
   IsTraining:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CreditCardProcTableset{
   CreditCardProc:Erp_Tablesets_CreditCardProcRow[],
   CreditCardProcessor:Erp_Tablesets_CreditCardProcessorRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CreditCardProcessorRow{
      /**  Company  */  
   Company:string,
      /**  ProcessorNum  */  
   ProcessorNum:number,
      /**  Processor  */  
   Processor:string,
      /**  ProcessorDesc  */  
   ProcessorDesc:string,
      /**  Partner  */  
   Partner:string,
      /**  PartnerUser  */  
   PartnerUser:string,
      /**  PartnerVendor  */  
   PartnerVendor:string,
      /**  PartnerPwd  */  
   PartnerPwd:string,
      /**  TPPID  */  
   TPPID:string,
      /**  FDMSGroupID  */  
   FDMSGroupID:string,
      /**  FDMSCustomerID  */  
   FDMSCustomerID:string,
      /**  FDMSPhoneNum  */  
   FDMSPhoneNum:string,
      /**  BankAcctID  */  
   BankAcctID:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Credit Card Masked password field  */  
   PartnerPwdMasked:string,
   BitFlag:number,
   BankAcctDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtCreditCardProcTableset{
   CreditCardProc:Erp_Tablesets_CreditCardProcRow[],
   CreditCardProcessor:Erp_Tablesets_CreditCardProcessorRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_CreditCardProcTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_CreditCardProcTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_CreditCardProcTableset[],
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
   returnObj:Erp_Tablesets_CreditCardProcListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewCreditCardProc_input{
   ds:Erp_Tablesets_CreditCardProcTableset[],
}

export interface GetNewCreditCardProc_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CreditCardProcTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewCreditCardProcessor_input{
   ds:Erp_Tablesets_CreditCardProcTableset[],
}

export interface GetNewCreditCardProcessor_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CreditCardProcTableset[],
}
}

   /** Required : 
      @param whereClauseCreditCardProc
      @param whereClauseCreditCardProcessor
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseCreditCardProc:string,
   whereClauseCreditCardProcessor:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_CreditCardProcTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface HasPendingAuthorizations_output{
   returnObj:boolean,
}

   /** Required : 
      @param processor
   */  
export interface HasProcessorPendingAuthorizations_input{
   processor:string,
}

export interface HasProcessorPendingAuthorizations_output{
   returnObj:boolean,
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
      @param procInterfaceCode
      @param ds
   */  
export interface OnChangeProcessor_input{
      /**  New Process interface code  */  
   procInterfaceCode:string,
   ds:Erp_Tablesets_CreditCardProcTableset[],
}

export interface OnChangeProcessor_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CreditCardProcTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtCreditCardProcTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtCreditCardProcTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_CreditCardProcTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CreditCardProcTableset[],
}
}

