import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Ice.BO.CnvProgsSvc
// Description: Represents the CnvProgs Service
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/$metadata", {
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
   Description: Get CnvProgs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CnvProgs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.CnvProgsRow
   */  
export function get_CnvProgs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_CnvProgsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/CnvProgs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_CnvProgsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CnvProgs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.CnvProgsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.CnvProgsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CnvProgs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/CnvProgs", {
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
   Summary: Calls GetByID to retrieve the CnvProg item
   Description: Calls GetByID to retrieve the CnvProg item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CnvProg
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param ConversionID Desc: ConversionID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.CnvProgsRow
   */  
export function get_CnvProgs_SystemCode_ConversionID(SystemCode:string, ConversionID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_CnvProgsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/CnvProgs(" + SystemCode + "," + ConversionID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_CnvProgsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CnvProg for the service
   Description: Calls UpdateExt to update CnvProg. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CnvProg
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param ConversionID Desc: ConversionID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.CnvProgsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CnvProgs_SystemCode_ConversionID(SystemCode:string, ConversionID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/CnvProgs(" + SystemCode + "," + ConversionID + ")", {
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
   Summary: Call UpdateExt to delete CnvProg item
   Description: Call UpdateExt to delete CnvProg item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CnvProg
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param ConversionID Desc: ConversionID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CnvProgs_SystemCode_ConversionID(SystemCode:string, ConversionID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/CnvProgs(" + SystemCode + "," + ConversionID + ")", {
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
   Description: Get ConverLogs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ConverLogs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ConverLogRow
   */  
export function get_ConverLogs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ConverLogRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/ConverLogs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ConverLogRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ConverLogs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ConverLogRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ConverLogRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ConverLogs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/ConverLogs", {
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
   Summary: Calls GetByID to retrieve the ConverLog item
   Description: Calls GetByID to retrieve the ConverLog item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ConverLog
      @param SysTaskNum Desc: SysTaskNum   Required: True   Allow empty value : True
      @param EntryNum Desc: EntryNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ConverLogRow
   */  
export function get_ConverLogs_SysTaskNum_EntryNum(SysTaskNum:string, EntryNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ConverLogRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/ConverLogs(" + SysTaskNum + "," + EntryNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_ConverLogRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ConverLog for the service
   Description: Calls UpdateExt to update ConverLog. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ConverLog
      @param SysTaskNum Desc: SysTaskNum   Required: True   Allow empty value : True
      @param EntryNum Desc: EntryNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ConverLogRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ConverLogs_SysTaskNum_EntryNum(SysTaskNum:string, EntryNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/ConverLogs(" + SysTaskNum + "," + EntryNum + ")", {
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
   Summary: Call UpdateExt to delete ConverLog item
   Description: Call UpdateExt to delete ConverLog item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ConverLog
      @param SysTaskNum Desc: SysTaskNum   Required: True   Allow empty value : True
      @param EntryNum Desc: EntryNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ConverLogs_SysTaskNum_EntryNum(SysTaskNum:string, EntryNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/ConverLogs(" + SysTaskNum + "," + EntryNum + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.CnvProgsListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_CnvProgsListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_CnvProgsListRow)
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
export function get_GetRows(whereClauseCnvProgs:string, whereClauseConverLog:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseCnvProgs!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCnvProgs=" + whereClauseCnvProgs
   }
   if(typeof whereClauseConverLog!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseConverLog=" + whereClauseConverLog
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/GetRows" + params, {
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
export function get_GetByID(systemCode:string, conversionID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof systemCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "systemCode=" + systemCode
   }
   if(typeof conversionID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "conversionID=" + conversionID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/GetList" + params, {
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
   Summary: Invoke method GetSystemCodes
   Description: Returns a  delimited list of system codes.
   OperationID: GetSystemCodes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSystemCodes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSystemCodes(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/GetSystemCodes", {
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
   Summary: Invoke method AddPatchConversionRecords
   Description: Adds update conversion records.
   OperationID: AddPatchConversionRecords
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddPatchConversionRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddPatchConversionRecords(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/AddPatchConversionRecords", {
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
   Summary: Invoke method UpdatePatchConversionCache
   Description: Reset conversion cache
   OperationID: UpdatePatchConversionCache
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdatePatchConversionCache_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdatePatchConversionCache(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/UpdatePatchConversionCache", {
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
   Summary: Invoke method RunsConversion
   Description: Method to run conversion
   OperationID: RunsConversion
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RunsConversion_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RunsConversion_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RunsConversion(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/RunsConversion", {
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
   Summary: Invoke method UpdateSeedData
   Description: Ensures all conversion programs that update seed data are in the table ice.cnvprogs
   OperationID: UpdateSeedData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateSeedData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateSeedData(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/UpdateSeedData", {
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
   Summary: Invoke method UploadSettingsFileFromServerPath
   Description: Uploads the settings file from server path and delete it after finish.
   OperationID: UploadSettingsFileFromServerPath
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UploadSettingsFileFromServerPath_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UploadSettingsFileFromServerPath_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UploadSettingsFileFromServerPath(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/UploadSettingsFileFromServerPath", {
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
   Summary: Invoke method ExportSettingsFileToServerPath
   Description: Exports the settings file to a server path.
   OperationID: ExportSettingsFileToServerPath
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportSettingsFileToServerPath_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportSettingsFileToServerPath_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExportSettingsFileToServerPath(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/ExportSettingsFileToServerPath", {
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
   Summary: Invoke method DeleteSettingsFileFromServer
   Description: Deletes the settings file from the provided fileRelativePath.
   OperationID: DeleteSettingsFileFromServer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteSettingsFileFromServer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteSettingsFileFromServer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteSettingsFileFromServer(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/DeleteSettingsFileFromServer", {
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
   Summary: Invoke method GetNewCnvProgs
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCnvProgs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCnvProgs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCnvProgs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCnvProgs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/GetNewCnvProgs", {
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
   Summary: Invoke method GetNewConverLog
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewConverLog
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewConverLog_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewConverLog_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewConverLog(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/GetNewConverLog", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_CnvProgsListRow{
   "odatametadata":string,
   "value":Ice_Tablesets_CnvProgsListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_CnvProgsRow{
   "odatametadata":string,
   "value":Ice_Tablesets_CnvProgsRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ConverLogRow{
   "odatametadata":string,
   "value":Ice_Tablesets_ConverLogRow[],
}

export interface Ice_Tablesets_CnvProgsListRow{
      /**  SystemCode  */  
   "SystemCode":string,
      /**  ConversionID  */  
   "ConversionID":string,
      /**  RunSequence  */  
   "RunSequence":number,
      /**  Program  */  
   "Program":string,
      /**  RunLevel  */  
   "RunLevel":string,
      /**  LastRunLevel  */  
   "LastRunLevel":string,
      /**  Description  */  
   "Description":string,
      /**  AutoRun  */  
   "AutoRun":boolean,
      /**  InitialRun  */  
   "InitialRun":boolean,
      /**  UserRun  */  
   "UserRun":boolean,
      /**  ReCoverable  */  
   "ReCoverable":boolean,
      /**  ReRunable  */  
   "ReRunable":boolean,
      /**  RunInDisconnectedCRM  */  
   "RunInDisconnectedCRM":boolean,
      /**  ProgStatus  */  
   "ProgStatus":string,
      /**  LastRunOn  */  
   "LastRunOn":string,
      /**  RunUserID  */  
   "RunUserID":string,
      /**  RunLog  */  
   "RunLog":string,
      /**  ProcessID  */  
   "ProcessID":string,
      /**  RunTaskNum  */  
   "RunTaskNum":number,
      /**  ConversionSetting  */  
   "ConversionSetting":string,
      /**  SettingFilename  */  
   "SettingFilename":string,
      /**  SettingLastUpdated  */  
   "SettingLastUpdated":string,
      /**  SettingLastUpdatedBy  */  
   "SettingLastUpdatedBy":string,
      /**  ProgressPercent  */  
   "ProgressPercent":number,
      /**  UserPromptProgram  */  
   "UserPromptProgram":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  ConversionType  */  
   "ConversionType":string,
      /**  RunFrequency  */  
   "RunFrequency":string,
      /**  InternalRunDate  */  
   "InternalRunDate":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_CnvProgsRow{
      /**  SystemCode  */  
   "SystemCode":string,
      /**  ConversionID  */  
   "ConversionID":string,
      /**  RunSequence  */  
   "RunSequence":number,
      /**  Program  */  
   "Program":string,
      /**  RunLevel  */  
   "RunLevel":string,
      /**  LastRunLevel  */  
   "LastRunLevel":string,
      /**  Description  */  
   "Description":string,
      /**  AutoRun  */  
   "AutoRun":boolean,
      /**  InitialRun  */  
   "InitialRun":boolean,
      /**  UserRun  */  
   "UserRun":boolean,
      /**  ReCoverable  */  
   "ReCoverable":boolean,
      /**  ReRunable  */  
   "ReRunable":boolean,
      /**  RunInDisconnectedCRM  */  
   "RunInDisconnectedCRM":boolean,
      /**  ProgStatus  */  
   "ProgStatus":string,
      /**  LastRunOn  */  
   "LastRunOn":string,
      /**  RunUserID  */  
   "RunUserID":string,
      /**  RunLog  */  
   "RunLog":string,
      /**  ProcessID  */  
   "ProcessID":string,
      /**  RunTaskNum  */  
   "RunTaskNum":number,
      /**  ConversionSetting  */  
   "ConversionSetting":string,
      /**  SettingFilename  */  
   "SettingFilename":string,
      /**  SettingLastUpdated  */  
   "SettingLastUpdated":string,
      /**  SettingLastUpdatedBy  */  
   "SettingLastUpdatedBy":string,
      /**  ProgressPercent  */  
   "ProgressPercent":number,
      /**  UserPromptProgram  */  
   "UserPromptProgram":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  ConversionType  */  
   "ConversionType":string,
      /**  RunFrequency  */  
   "RunFrequency":string,
      /**  InternalRunDate  */  
   "InternalRunDate":string,
      /**  Execute  */  
   "Exec":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_ConverLogRow{
      /**  System Task Number  */  
   "SysTaskNum":number,
      /**  Entry Number  */  
   "EntryNum":number,
      /**  EnteredOn  */  
   "EnteredOn":string,
      /**  Error indicator  */  
   "IsError":boolean,
      /**  Message Text  */  
   "MsgText":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  MsgType  */  
   "MsgType":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
export interface AddPatchConversionRecords_output{
}

   /** Required : 
      @param systemCode
      @param conversionID
   */  
export interface DeleteByID_input{
   systemCode:string,
   conversionID:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param systemCode
      @param conversionId
      @param fileRelativePath
   */  
export interface DeleteSettingsFileFromServer_input{
      /**  The system code.  */  
   systemCode:string,
      /**  The conversion identifier.  */  
   conversionId:string,
      /**  The server file relative path.  */  
   fileRelativePath:string,
}

export interface DeleteSettingsFileFromServer_output{
}

   /** Required : 
      @param systemCode
      @param conversionId
   */  
export interface ExportSettingsFileToServerPath_input{
      /**  The system code.  */  
   systemCode:string,
      /**  The conversion identifier.  */  
   conversionId:string,
}

export interface ExportSettingsFileToServerPath_output{
      /**  The file server relative path in next format: temp\{RandomFolderName}\{SettingsFilename}  */  
   returnObj:string,
}

   /** Required : 
      @param systemCode
      @param conversionID
   */  
export interface GetByID_input{
   systemCode:string,
   conversionID:string,
}

export interface GetByID_output{
   returnObj:Ice_Tablesets_CnvProgsTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Ice_Tablesets_CnvProgsTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Ice_Tablesets_CnvProgsTableset[],
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
   returnObj:Ice_Tablesets_CnvProgsListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param systemCode
   */  
export interface GetNewCnvProgs_input{
   ds:Ice_Tablesets_CnvProgsTableset[],
   systemCode:string,
}

export interface GetNewCnvProgs_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_CnvProgsTableset[],
}
}

   /** Required : 
      @param ds
      @param sysTaskNum
   */  
export interface GetNewConverLog_input{
   ds:Ice_Tablesets_CnvProgsTableset[],
   sysTaskNum:number,
}

export interface GetNewConverLog_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_CnvProgsTableset[],
}
}

   /** Required : 
      @param whereClauseCnvProgs
      @param whereClauseConverLog
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseCnvProgs:string,
   whereClauseConverLog:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Ice_Tablesets_CnvProgsTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface GetSystemCodes_output{
   returnObj:string,
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

export interface Ice_Tablesets_CnvProgsListRow{
      /**  SystemCode  */  
   SystemCode:string,
      /**  ConversionID  */  
   ConversionID:string,
      /**  RunSequence  */  
   RunSequence:number,
      /**  Program  */  
   Program:string,
      /**  RunLevel  */  
   RunLevel:string,
      /**  LastRunLevel  */  
   LastRunLevel:string,
      /**  Description  */  
   Description:string,
      /**  AutoRun  */  
   AutoRun:boolean,
      /**  InitialRun  */  
   InitialRun:boolean,
      /**  UserRun  */  
   UserRun:boolean,
      /**  ReCoverable  */  
   ReCoverable:boolean,
      /**  ReRunable  */  
   ReRunable:boolean,
      /**  RunInDisconnectedCRM  */  
   RunInDisconnectedCRM:boolean,
      /**  ProgStatus  */  
   ProgStatus:string,
      /**  LastRunOn  */  
   LastRunOn:string,
      /**  RunUserID  */  
   RunUserID:string,
      /**  RunLog  */  
   RunLog:string,
      /**  ProcessID  */  
   ProcessID:string,
      /**  RunTaskNum  */  
   RunTaskNum:number,
      /**  ConversionSetting  */  
   ConversionSetting:string,
      /**  SettingFilename  */  
   SettingFilename:string,
      /**  SettingLastUpdated  */  
   SettingLastUpdated:string,
      /**  SettingLastUpdatedBy  */  
   SettingLastUpdatedBy:string,
      /**  ProgressPercent  */  
   ProgressPercent:number,
      /**  UserPromptProgram  */  
   UserPromptProgram:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  ConversionType  */  
   ConversionType:string,
      /**  RunFrequency  */  
   RunFrequency:string,
      /**  InternalRunDate  */  
   InternalRunDate:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_CnvProgsListTableset{
   CnvProgsList:Ice_Tablesets_CnvProgsListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_CnvProgsRow{
      /**  SystemCode  */  
   SystemCode:string,
      /**  ConversionID  */  
   ConversionID:string,
      /**  RunSequence  */  
   RunSequence:number,
      /**  Program  */  
   Program:string,
      /**  RunLevel  */  
   RunLevel:string,
      /**  LastRunLevel  */  
   LastRunLevel:string,
      /**  Description  */  
   Description:string,
      /**  AutoRun  */  
   AutoRun:boolean,
      /**  InitialRun  */  
   InitialRun:boolean,
      /**  UserRun  */  
   UserRun:boolean,
      /**  ReCoverable  */  
   ReCoverable:boolean,
      /**  ReRunable  */  
   ReRunable:boolean,
      /**  RunInDisconnectedCRM  */  
   RunInDisconnectedCRM:boolean,
      /**  ProgStatus  */  
   ProgStatus:string,
      /**  LastRunOn  */  
   LastRunOn:string,
      /**  RunUserID  */  
   RunUserID:string,
      /**  RunLog  */  
   RunLog:string,
      /**  ProcessID  */  
   ProcessID:string,
      /**  RunTaskNum  */  
   RunTaskNum:number,
      /**  ConversionSetting  */  
   ConversionSetting:string,
      /**  SettingFilename  */  
   SettingFilename:string,
      /**  SettingLastUpdated  */  
   SettingLastUpdated:string,
      /**  SettingLastUpdatedBy  */  
   SettingLastUpdatedBy:string,
      /**  ProgressPercent  */  
   ProgressPercent:number,
      /**  UserPromptProgram  */  
   UserPromptProgram:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  ConversionType  */  
   ConversionType:string,
      /**  RunFrequency  */  
   RunFrequency:string,
      /**  InternalRunDate  */  
   InternalRunDate:string,
      /**  Execute  */  
   Exec:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_CnvProgsTableset{
   CnvProgs:Ice_Tablesets_CnvProgsRow[],
   ConverLog:Ice_Tablesets_ConverLogRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_ConverLogRow{
      /**  System Task Number  */  
   SysTaskNum:number,
      /**  Entry Number  */  
   EntryNum:number,
      /**  EnteredOn  */  
   EnteredOn:string,
      /**  Error indicator  */  
   IsError:boolean,
      /**  Message Text  */  
   MsgText:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  MsgType  */  
   MsgType:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_UpdExtCnvProgsTableset{
   CnvProgs:Ice_Tablesets_CnvProgsRow[],
   ConverLog:Ice_Tablesets_ConverLogRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param systemCode
      @param conversionID
   */  
export interface RunsConversion_input{
      /**  The ssytem code.  */  
   systemCode:string,
      /**  The conversion ID to run.  */  
   conversionID:string,
}

export interface RunsConversion_output{
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Ice_Tablesets_UpdExtCnvProgsTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_UpdExtCnvProgsTableset[],
   errorsOccurred:boolean,
}
}

export interface UpdatePatchConversionCache_output{
}

export interface UpdateSeedData_output{
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Ice_Tablesets_CnvProgsTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_CnvProgsTableset[],
}
}

   /** Required : 
      @param systemCode
      @param conversionId
      @param fileRelativePath
   */  
export interface UploadSettingsFileFromServerPath_input{
      /**  The system code.  */  
   systemCode:string,
      /**  The conversion identifier.  */  
   conversionId:string,
      /**  The file relative path.  */  
   fileRelativePath:string,
}

export interface UploadSettingsFileFromServerPath_output{
}

