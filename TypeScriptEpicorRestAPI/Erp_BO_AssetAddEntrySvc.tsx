import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.AssetAddEntrySvc
// Description: FA Asset Addition Entry Business Object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/$metadata", {
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
   Description: Get AssetAddEntries items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AssetAddEntries
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FAAdditionRow
   */  
export function get_AssetAddEntries(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAAdditionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/AssetAddEntries", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAAdditionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AssetAddEntries
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FAAdditionRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FAAdditionRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AssetAddEntries(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/AssetAddEntries", {
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
   Summary: Calls GetByID to retrieve the AssetAddEntry item
   Description: Calls GetByID to retrieve the AssetAddEntry item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AssetAddEntry
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param AdditionNum Desc: AdditionNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FAAdditionRow
   */  
export function get_AssetAddEntries_Company_AssetNum_AdditionNum(Company:string, AssetNum:string, AdditionNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FAAdditionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/AssetAddEntries(" + Company + "," + AssetNum + "," + AdditionNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FAAdditionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update AssetAddEntry for the service
   Description: Calls UpdateExt to update AssetAddEntry. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AssetAddEntry
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param AdditionNum Desc: AdditionNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FAAdditionRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_AssetAddEntries_Company_AssetNum_AdditionNum(Company:string, AssetNum:string, AdditionNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/AssetAddEntries(" + Company + "," + AssetNum + "," + AdditionNum + ")", {
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
   Summary: Call UpdateExt to delete AssetAddEntry item
   Description: Call UpdateExt to delete AssetAddEntry item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AssetAddEntry
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param AdditionNum Desc: AdditionNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_AssetAddEntries_Company_AssetNum_AdditionNum(Company:string, AssetNum:string, AdditionNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/AssetAddEntries(" + Company + "," + AssetNum + "," + AdditionNum + ")", {
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
   Description: Get FAAddRegs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FAAddRegs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param AdditionNum Desc: AdditionNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FAAddRegRow
   */  
export function get_AssetAddEntries_Company_AssetNum_AdditionNum_FAAddRegs(Company:string, AssetNum:string, AdditionNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAAddRegRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/AssetAddEntries(" + Company + "," + AssetNum + "," + AdditionNum + ")/FAAddRegs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAAddRegRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the FAAddReg item
   Description: Calls GetByID to retrieve the FAAddReg item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FAAddReg1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param AdditionNum Desc: AdditionNum   Required: True
      @param AssetRegID Desc: AssetRegID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FAAddRegRow
   */  
export function get_AssetAddEntries_Company_AssetNum_AdditionNum_FAAddRegs_Company_AssetNum_AdditionNum_AssetRegID(Company:string, AssetNum:string, AdditionNum:string, AssetRegID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FAAddRegRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/AssetAddEntries(" + Company + "," + AssetNum + "," + AdditionNum + ")/FAAddRegs(" + Company + "," + AssetNum + "," + AdditionNum + "," + AssetRegID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FAAddRegRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get FAAdditionAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FAAdditionAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param AdditionNum Desc: AdditionNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FAAdditionAttchRow
   */  
export function get_AssetAddEntries_Company_AssetNum_AdditionNum_FAAdditionAttches(Company:string, AssetNum:string, AdditionNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAAdditionAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/AssetAddEntries(" + Company + "," + AssetNum + "," + AdditionNum + ")/FAAdditionAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAAdditionAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the FAAdditionAttch item
   Description: Calls GetByID to retrieve the FAAdditionAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FAAdditionAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param AdditionNum Desc: AdditionNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FAAdditionAttchRow
   */  
export function get_AssetAddEntries_Company_AssetNum_AdditionNum_FAAdditionAttches_Company_AssetNum_AdditionNum_DrawingSeq(Company:string, AssetNum:string, AdditionNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FAAdditionAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/AssetAddEntries(" + Company + "," + AssetNum + "," + AdditionNum + ")/FAAdditionAttches(" + Company + "," + AssetNum + "," + AdditionNum + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FAAdditionAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get FAAddRegs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FAAddRegs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FAAddRegRow
   */  
export function get_FAAddRegs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAAddRegRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/FAAddRegs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAAddRegRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FAAddRegs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FAAddRegRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FAAddRegRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FAAddRegs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/FAAddRegs", {
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
   Summary: Calls GetByID to retrieve the FAAddReg item
   Description: Calls GetByID to retrieve the FAAddReg item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FAAddReg
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param AdditionNum Desc: AdditionNum   Required: True
      @param AssetRegID Desc: AssetRegID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FAAddRegRow
   */  
export function get_FAAddRegs_Company_AssetNum_AdditionNum_AssetRegID(Company:string, AssetNum:string, AdditionNum:string, AssetRegID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FAAddRegRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/FAAddRegs(" + Company + "," + AssetNum + "," + AdditionNum + "," + AssetRegID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FAAddRegRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update FAAddReg for the service
   Description: Calls UpdateExt to update FAAddReg. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FAAddReg
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param AdditionNum Desc: AdditionNum   Required: True
      @param AssetRegID Desc: AssetRegID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FAAddRegRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_FAAddRegs_Company_AssetNum_AdditionNum_AssetRegID(Company:string, AssetNum:string, AdditionNum:string, AssetRegID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/FAAddRegs(" + Company + "," + AssetNum + "," + AdditionNum + "," + AssetRegID + ")", {
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
   Summary: Call UpdateExt to delete FAAddReg item
   Description: Call UpdateExt to delete FAAddReg item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FAAddReg
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param AdditionNum Desc: AdditionNum   Required: True
      @param AssetRegID Desc: AssetRegID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_FAAddRegs_Company_AssetNum_AdditionNum_AssetRegID(Company:string, AssetNum:string, AdditionNum:string, AssetRegID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/FAAddRegs(" + Company + "," + AssetNum + "," + AdditionNum + "," + AssetRegID + ")", {
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
   Description: Get FAAdditionAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FAAdditionAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FAAdditionAttchRow
   */  
export function get_FAAdditionAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAAdditionAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/FAAdditionAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAAdditionAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FAAdditionAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FAAdditionAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FAAdditionAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FAAdditionAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/FAAdditionAttches", {
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
   Summary: Calls GetByID to retrieve the FAAdditionAttch item
   Description: Calls GetByID to retrieve the FAAdditionAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FAAdditionAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param AdditionNum Desc: AdditionNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FAAdditionAttchRow
   */  
export function get_FAAdditionAttches_Company_AssetNum_AdditionNum_DrawingSeq(Company:string, AssetNum:string, AdditionNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FAAdditionAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/FAAdditionAttches(" + Company + "," + AssetNum + "," + AdditionNum + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FAAdditionAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update FAAdditionAttch for the service
   Description: Calls UpdateExt to update FAAdditionAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FAAdditionAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param AdditionNum Desc: AdditionNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FAAdditionAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_FAAdditionAttches_Company_AssetNum_AdditionNum_DrawingSeq(Company:string, AssetNum:string, AdditionNum:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/FAAdditionAttches(" + Company + "," + AssetNum + "," + AdditionNum + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete FAAdditionAttch item
   Description: Call UpdateExt to delete FAAdditionAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FAAdditionAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param AdditionNum Desc: AdditionNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_FAAdditionAttches_Company_AssetNum_AdditionNum_DrawingSeq(Company:string, AssetNum:string, AdditionNum:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/FAAdditionAttches(" + Company + "," + AssetNum + "," + AdditionNum + "," + DrawingSeq + ")", {
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
   Description: Get SelectedSerialNumbers items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SelectedSerialNumbers
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SelectedSerialNumbersRow
   */  
export function get_SelectedSerialNumbers(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SelectedSerialNumbersRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/SelectedSerialNumbers", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SelectedSerialNumbersRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SelectedSerialNumbers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SelectedSerialNumbers(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/SelectedSerialNumbers", {
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
   Summary: Calls GetByID to retrieve the SelectedSerialNumber item
   Description: Calls GetByID to retrieve the SelectedSerialNumber item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SelectedSerialNumber
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param SerialNumber Desc: SerialNumber   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
   */  
export function get_SelectedSerialNumbers_Company_PartNum_SerialNumber(Company:string, PartNum:string, SerialNumber:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_SelectedSerialNumbersRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_SelectedSerialNumbersRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update SelectedSerialNumber for the service
   Description: Calls UpdateExt to update SelectedSerialNumber. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SelectedSerialNumber
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param SerialNumber Desc: SerialNumber   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_SelectedSerialNumbers_Company_PartNum_SerialNumber(Company:string, PartNum:string, SerialNumber:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")", {
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
   Summary: Call UpdateExt to delete SelectedSerialNumber item
   Description: Call UpdateExt to delete SelectedSerialNumber item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SelectedSerialNumber
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param SerialNumber Desc: SerialNumber   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_SelectedSerialNumbers_Company_PartNum_SerialNumber(Company:string, PartNum:string, SerialNumber:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")", {
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
   Description: Get SNFormats items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SNFormats
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SNFormatRow
   */  
export function get_SNFormats(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SNFormatRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/SNFormats", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SNFormatRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SNFormats
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SNFormatRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SNFormatRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SNFormats(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/SNFormats", {
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
   Summary: Calls GetByID to retrieve the SNFormat item
   Description: Calls GetByID to retrieve the SNFormat item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SNFormat
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SNFormatRow
   */  
export function get_SNFormats_Company_PartNum_Plant(Company:string, PartNum:string, Plant:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_SNFormatRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_SNFormatRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update SNFormat for the service
   Description: Calls UpdateExt to update SNFormat. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SNFormat
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SNFormatRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_SNFormats_Company_PartNum_Plant(Company:string, PartNum:string, Plant:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")", {
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
   Summary: Call UpdateExt to delete SNFormat item
   Description: Call UpdateExt to delete SNFormat item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SNFormat
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_SNFormats_Company_PartNum_Plant(Company:string, PartNum:string, Plant:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FAAdditionListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAAdditionListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAAdditionListRow)
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
export function get_GetRows(whereClauseFAAddition:string, whereClauseFAAdditionAttch:string, whereClauseFAAddReg:string, whereClauseSelectedSerialNumbers:string, whereClauseSNFormat:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseFAAddition!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseFAAddition=" + whereClauseFAAddition
   }
   if(typeof whereClauseFAAdditionAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseFAAdditionAttch=" + whereClauseFAAdditionAttch
   }
   if(typeof whereClauseFAAddReg!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseFAAddReg=" + whereClauseFAAddReg
   }
   if(typeof whereClauseSelectedSerialNumbers!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseSelectedSerialNumbers=" + whereClauseSelectedSerialNumbers
   }
   if(typeof whereClauseSNFormat!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseSNFormat=" + whereClauseSNFormat
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/GetRows" + params, {
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
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(assetNum:string, additionNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof assetNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "assetNum=" + assetNum
   }
   if(typeof additionNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "additionNum=" + additionNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/GetList" + params, {
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
   Summary: Invoke method CheckAssetTransactions
   Description: Checks if there are any transactions for this Asset marked as Ready To Post
   OperationID: CheckAssetTransactions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckAssetTransactions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckAssetTransactions_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckAssetTransactions(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/CheckAssetTransactions", {
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
   Summary: Invoke method ClearReadyToPost
   Description: Clears Ready To Post flag on Asset transactions with SysRowID different from the one provided
   OperationID: ClearReadyToPost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ClearReadyToPost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClearReadyToPost_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ClearReadyToPost(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/ClearReadyToPost", {
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
   Summary: Invoke method LeaveAdded
   Description: To be called on leave of FAAddition.Added field to update costs based on
new exchange rate derived from this apply date.
   OperationID: LeaveAdded
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveAdded_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveAdded_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LeaveAdded(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/LeaveAdded", {
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
   Summary: Invoke method LeaveAdditionCost
   Description: To be called on leave of addition cost field to update the Book Value field.
   OperationID: LeaveAdditionCost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveAdditionCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveAdditionCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LeaveAdditionCost(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/LeaveAdditionCost", {
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
   Summary: Invoke method LeaveAdditionType
   Description: To be called on leave of AdditionType field
   OperationID: LeaveAdditionType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveAdditionType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveAdditionType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LeaveAdditionType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/LeaveAdditionType", {
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
   Summary: Invoke method LeaveGrantAmt
   Description: To be called on leave of grant amount field to update the Book Value field.
   OperationID: LeaveGrantAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveGrantAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveGrantAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LeaveGrantAmt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/LeaveGrantAmt", {
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
   Summary: Invoke method LeaveInvoiceLine
   Description: Called on the leave of FAAddition.InvoiceLine for validation purpose.
   OperationID: LeaveInvoiceLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveInvoiceLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveInvoiceLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LeaveInvoiceLine(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/LeaveInvoiceLine", {
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
   Summary: Invoke method LeaveInvoiceNum
   Description: Called on the leave of Invoice Number for validation purpose.
   OperationID: LeaveInvoiceNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveInvoiceNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveInvoiceNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LeaveInvoiceNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/LeaveInvoiceNum", {
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
   Summary: Invoke method LeaveJobNum
   Description: To be called on leave of Job Number field for validating an existing Job.
   OperationID: LeaveJobNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LeaveJobNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/LeaveJobNum", {
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
   Summary: Invoke method LeaveLotNum
   Description: To be called on leave of FAAddition.LotNum field
   OperationID: LeaveLotNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveLotNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveLotNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LeaveLotNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/LeaveLotNum", {
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
   Summary: Invoke method LeavePartNum
   Description: To be called on leave of FAAddition.PartNum field
   OperationID: LeavePartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeavePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeavePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LeavePartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/LeavePartNum", {
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
   Summary: Invoke method LeavePONum
   Description: To be called on leave of VendorID field to validate an existing PO
   OperationID: LeavePONum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeavePONum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeavePONum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LeavePONum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/LeavePONum", {
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
   Summary: Invoke method LeaveRegCurrDepreciation
   Description: To be called on leave of FAAddReg.CurrDepreciation field to update the Book Value field.
   OperationID: LeaveRegCurrDepreciation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveRegCurrDepreciation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveRegCurrDepreciation_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LeaveRegCurrDepreciation(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/LeaveRegCurrDepreciation", {
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
   Summary: Invoke method LeaveRegCurrGrantDep
   Description: To be called on leave of FAAddReg.CurrGrantDep field to update the Grant Book Value field.
   OperationID: LeaveRegCurrGrantDep
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveRegCurrGrantDep_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveRegCurrGrantDep_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LeaveRegCurrGrantDep(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/LeaveRegCurrGrantDep", {
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
   Summary: Invoke method LeaveRegPrevDepreciation
   Description: To be called on leave of FAAddReg.PrevDepreciation field to update the Book Value field.
   OperationID: LeaveRegPrevDepreciation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveRegPrevDepreciation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveRegPrevDepreciation_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LeaveRegPrevDepreciation(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/LeaveRegPrevDepreciation", {
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
   Summary: Invoke method LeaveRegPrevGrantDep
   Description: To be called on leave of FAAddReg.PrevGrantDep field to update the Grant Book Value field.
   OperationID: LeaveRegPrevGrantDep
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveRegPrevGrantDep_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveRegPrevGrantDep_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LeaveRegPrevGrantDep(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/LeaveRegPrevGrantDep", {
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
   Summary: Invoke method LeaveTransferQty
   Description: To be called on leave of FAAddition.TransferQty field. This qty is always expressed in IUM.
   OperationID: LeaveTransferQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveTransferQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveTransferQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LeaveTransferQty(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/LeaveTransferQty", {
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
   Summary: Invoke method LeaveVendorID
   Description: To be called on leave of VendorID field to validate an existing Vendor
   OperationID: LeaveVendorID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveVendorID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveVendorID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LeaveVendorID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/LeaveVendorID", {
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
   Summary: Invoke method LeaveWarehouse
   Description: To be called on leave of FAAddition.WarehouseCode field.
   OperationID: LeaveWarehouse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveWarehouse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveWarehouse_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LeaveWarehouse(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/LeaveWarehouse", {
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
   Summary: Invoke method PreUpdate
   Description: To be called before Update
   OperationID: PreUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreUpdate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/PreUpdate", {
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
   Summary: Invoke method ChangePlaceInServDate
   OperationID: ChangePlaceInServDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePlaceInServDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePlaceInServDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePlaceInServDate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/ChangePlaceInServDate", {
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
   Summary: Invoke method GetSelectSerialNumbersParams
   Description: Purpose:  sets up the parameters for invoking the Serial Number Selection form
Notes:
<param name="ds">Asset Addition DataSet</param><returns>The SelectSerialNumbersParams dataset</returns>
   OperationID: GetSelectSerialNumbersParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSelectSerialNumbersParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectSerialNumbersParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSelectSerialNumbersParams(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/GetSelectSerialNumbersParams", {
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
   Summary: Invoke method ValidateSN
   Description: Validates that a single serial number scanned in the serial number selection form is valid for this transaction
   OperationID: ValidateSN
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSN_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSN_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateSN(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/ValidateSN", {
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
   Summary: Invoke method GetSelectedSerialNumbers
   Description: This method will retrieve the serial numbers for FAAddition record and
update the SelectedSerialNumbers table with these records.
   OperationID: GetSelectedSerialNumbers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSelectedSerialNumbers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectedSerialNumbers_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSelectedSerialNumbers(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/GetSelectedSerialNumbers", {
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
   Summary: Invoke method GetNewFAAddition
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFAAddition
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFAAddition_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFAAddition_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewFAAddition(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/GetNewFAAddition", {
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
   Summary: Invoke method GetNewFAAdditionAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFAAdditionAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFAAdditionAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFAAdditionAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewFAAdditionAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/GetNewFAAdditionAttch", {
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
   Summary: Invoke method GetNewFAAddReg
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFAAddReg
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFAAddReg_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFAAddReg_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewFAAddReg(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/GetNewFAAddReg", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAAddRegRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FAAddRegRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAAdditionAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FAAdditionAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAAdditionListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FAAdditionListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAAdditionRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FAAdditionRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SNFormatRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SNFormatRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SelectedSerialNumbersRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SelectedSerialNumbersRow[],
}

export interface Erp_Tablesets_FAAddRegRow{
      /**  Company of the Addition.  */  
   "Company":string,
      /**  Asset number of the Addition.  */  
   "AssetNum":string,
      /**  Unique number to identify the Addition of an asset.  */  
   "AdditionNum":number,
      /**  Identifier of the Asset Register.  */  
   "AssetRegID":string,
      /**  The depreciation already applied to this addition in another system in previous years. Applies to inter-group transfers only.  */  
   "PrevDepreciation":number,
      /**  The depreciation already applied to this addition in another system within the same holding company for this year. This amount is only posted to the balance sheet and not as charge to the P&L, because the the charge has already been charged in a sister company.  */  
   "CurrDepreciation":number,
      /**  Book Value of the addition is a calculated field. It is Addition Cost minus previous years Addition Depreciation minus current year Addition Depreciation.  */  
   "BookValue":number,
      /**  Grant Book Value of the addition is a calculated field. It is Grant Amount minus previous years Addition Grant Depreciation minus current year Addition Grant Depreciation.  */  
   "GrantBookValue":number,
      /**  The Grant Depreciation already applied to the grant addition from another system for previous years. Applies to inter-group transfers only.  */  
   "PrevGrantDep":number,
      /**  The Grant Depreciation already applied to the grant addition from another system for the current year. Applies to inter-group transfers only.  */  
   "CurrGrantDep":number,
      /**  The depreciation already applied to this addition in another system in previous years in the specified currency. Applies to inter-group transfers only.  */  
   "DocPrevDepreciation":number,
      /**  The depreciation already applied to this addition in another system within the same holding company for this year in the specified currency.  */  
   "DocCurrDepreciation":number,
      /**  This is the Addition Book Value in the specified currency.  */  
   "DocBookValue":number,
      /**  Grant Book Value of the addition is a calculated field. It is Grant Amount minus previous years Addition Grant Depreciation minus current year Addition Grant Depreciation.  */  
   "DocGrantBookValue":number,
      /**  The previous years grant depreciation for this addition in the specified currency.  */  
   "DocPrevGrantDep":number,
      /**  The current year grant depreciation for this addition in the specified currency.  */  
   "DocCurrGrantDep":number,
      /**  Reporting currency value of the previous years addition depreciation.  */  
   "Rpt1PrevDepreciation":number,
      /**  Reporting currency value of the current year addition depreciation.  */  
   "Rpt1CurrDepreciation":number,
      /**  Reporting currency value of the addition book value.  */  
   "Rpt1BookValue":number,
      /**  Grant Book Value of the addition is a calculated field. It is Grant Amount minus previous years Addition Grant Depreciation minus current year Addition Grant Depreciation.  */  
   "Rpt1GrantBookValue":number,
      /**  Reporting currency value of the previous years addition grant depreciation.  */  
   "Rpt1PrevGrantDep":number,
      /**  Reporting currency value of the current year addition grant depreciation.  */  
   "Rpt1CurrGrantDep":number,
      /**  Reporting currency value of the previous years addition depreciation.  */  
   "Rpt2PrevDepreciation":number,
      /**  Reporting currency value of the current year addition depreciation.  */  
   "Rpt2CurrDepreciation":number,
      /**  Reporting currency value of the addition book value.  */  
   "Rpt2BookValue":number,
      /**  Grant Book Value of the addition is a calculated field. It is Grant Amount minus previous years Addition Grant Depreciation minus current year Addition Grant Depreciation.  */  
   "Rpt2GrantBookValue":number,
      /**  Reporting currency value of the previous years addition grant depreciation.  */  
   "Rpt2PrevGrantDep":number,
      /**  Reporting currency value of the current year addition grant depreciation.  */  
   "Rpt2CurrGrantDep":number,
      /**  Reporting currency value of the previous years addition depreciation.  */  
   "Rpt3PrevDepreciation":number,
      /**  Reporting currency value of the current year addition depreciation.  */  
   "Rpt3CurrDepreciation":number,
      /**  Reporting currency value of the addition book value.  */  
   "Rpt3BookValue":number,
      /**  Grant Book Value of the addition is a calculated field. It is Grant Amount minus previous years Addition Grant Depreciation minus current year Addition Grant Depreciation.  */  
   "Rpt3GrantBookValue":number,
      /**  Reporting currency value of the previous years addtion grant depreciation.  */  
   "Rpt3PrevGrantDep":number,
      /**  Reporting currency value of the current year addition grant depreciation.  */  
   "Rpt3CurrGrantDep":number,
      /**  The cost added to the asset.  */  
   "AdditionCost":number,
      /**  The Grant Amount awarded to an asset to reduce the depreciation charge.  */  
   "GrantAmt":number,
      /**  The cost added to the asset in the currency specified.  */  
   "DocAdditionCost":number,
      /**  The Grant Amount awarded to an asset to reduce the depreciation charge in the currency specified.  */  
   "DocGrantAmt":number,
      /**  Reporting currency value of the Addition Cost.  */  
   "Rpt1AdditionCost":number,
      /**  Reporting currency value of the Grant Amount.  */  
   "Rpt1GrantAmt":number,
      /**  Reporting currency value of the Addition Cost.  */  
   "Rpt2AdditionCost":number,
      /**  Reporting currency value of the Grant Amount.  */  
   "Rpt2GrantAmt":number,
      /**  Reporting currency value of the Addition Cost.  */  
   "Rpt3AdditionCost":number,
      /**  Reporting currency value of the Grant Amount.  */  
   "Rpt3GrantAmt":number,
      /**  The cost added to the asset.  */  
   "AdditionCostLimit":number,
      /**  The cost added to the asset in the currency specified.  */  
   "DocAdditionCostLimit":number,
      /**  Reporting currency value of the Addition Cost.  */  
   "Rpt1AdditionCostLimit":number,
      /**  Reporting currency value of the Addition Cost.  */  
   "Rpt2AdditionCostLimit":number,
      /**  Reporting currency value of the Addition Cost.  */  
   "Rpt3AdditionCostLimit":number,
      /**  The cost added to the asset.  */  
   "CostVariance":number,
      /**  The cost added to the asset in the currency specified.  */  
   "DocCostVariance":number,
      /**  Reporting currency value of the Addition Cost.  */  
   "Rpt1CostVariance":number,
      /**  Reporting currency value of the Addition Cost.  */  
   "Rpt2CostVariance":number,
      /**  Reporting currency value of the Addition Cost.  */  
   "Rpt3CostVariance":number,
      /**  The cost added to the asset.  */  
   "GrantVariance":number,
      /**  The cost added to the asset in the currency specified.  */  
   "DocGrantVariance":number,
      /**  Reporting currency value of the Addition Cost.  */  
   "Rpt1GrantVariance":number,
      /**  Reporting currency value of the Addition Cost.  */  
   "Rpt2GrantVariance":number,
      /**  Reporting currency value of the Addition Cost.  */  
   "Rpt3GrantVariance":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  InclCurrPerDepn  */  
   "InclCurrPerDepn":boolean,
      /**  Affects Asset Life  */  
   "AffectsAssetLife":boolean,
      /**  New Asset Estimated Life  */  
   "NewAssetLife":number,
      /**  New Life Modifier. Available Values (PERIODS or YEARS)  */  
   "NewLifeModifier":string,
   "DisableInclCurrPerDepn":boolean,
   "RateGrpCode":string,
      /**  Currency Code  */  
   "CurrCode":string,
      /**  Current Asset Estimated Life  */  
   "CurrAssetLife":number,
      /**  Current Life Modifier  */  
   "CurrLifeModifier":string,
      /**  Current Asset Estimated Life  */  
   "CurrAssetLifeDisplay":string,
   "BitFlag":number,
   "FAssetAssetDescription":string,
   "FAssetRegDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_FAAdditionAttchRow{
   "Company":string,
   "AssetNum":string,
   "AdditionNum":number,
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

export interface Erp_Tablesets_FAAdditionListRow{
      /**  Company of the Addition.  */  
   "Company":string,
      /**  Asset number of the Addition.  */  
   "AssetNum":string,
      /**  Unique number to identify the Addition of an asset.  */  
   "AdditionNum":number,
      /**  The date of Addition  */  
   "Added":string,
      /**  The cost added to the asset.  */  
   "AdditionCost":number,
      /**  Description of the Addition.  */  
   "Description":string,
      /**  The vendor of the Addition. Defaulted from the asset.  */  
   "VendorNum":number,
      /**  The Vendorname of the vendor of the addtion. The Vendor name can be entered without entering a vendor. Defaulted from the asset.  */  
   "VendorName":string,
      /**  The Vendors invoice number. Defaulted from the Asset.  */  
   "InvoiceNum":string,
      /**  The vendors PO number of the Addition. Defaulted from the asset.  */  
   "PONum":number,
      /**  The jobnumber that created the Addition. Defaulted from the asset.  */  
   "JobNum":string,
      /**  The warehouse where the addition is stored. This is for information purposes only. In the warehouse tracker no assets can be tracked.  */  
   "WarehouseCode":string,
      /**  The bin where the addition is stored. This is for information purposes only. In the bin tracker no assets can be tracked.  */  
   "BinNum":string,
      /**  A freeform field to indicate the location of the addition.  */  
   "Location":string,
      /**  The original manufacturer of the addition.  */  
   "Manufacturer":string,
      /**  The model number of addition.  */  
   "Model":string,
      /**  The serial number of the addition.  */  
   "Serialno":string,
      /**  Indicator to express if this addition is bought new.  */  
   "NewAsset":boolean,
      /**  Flag to indicate that the addition is posted to the GL. After posting modification of the addition is not allowed.  */  
   "Posted":boolean,
      /**  Posting date of the addition to the GL.  */  
   "PostDate":string,
      /**  The addition is posted by the user.  */  
   "PostedBy":string,
      /**  The GL journal to which the addition is posted.  */  
   "JournalCode":string,
      /**  The GL journal number to which the addition is posted.  */  
   "JournalNum":number,
      /**  The fiscal year of posting of the addition to the GL.  */  
   "FiscalYear":number,
      /**  The fiscal period of posting of the addition to the GL.  */  
   "FiscalPeriod":number,
      /**  Flag to indicat that the addition is allowed to be posted to the GL.  */  
   "ReadyToPost":boolean,
      /**  Fiscal year suffix  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  The Grant Amount awarded to an asset to reduce the depreciation charge.  */  
   "GrantAmt":number,
      /**  Indicates the type of asset addition activity.  Valid values are: "PURCHASE", "TRANSFER" or "MISC".  */  
   "AdditionType":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Unique identifier of the currency rate group.  */  
   "RateGrpCode":string,
      /**  The Invoice Line of the related or linked AP Invoice.  */  
   "InvoiceLine":number,
      /**  Identifies the part number transferred from stock to asset.  This field is only required if the Addition Type is "Transfer".  */  
   "PartNum":string,
      /**  Transferred Quantity reported for this addition transfer.  */  
   "TransferQty":number,
      /**  Unit of Measure for the transferred quantity.  */  
   "TransferUOM":string,
      /**  Lot Number of the transferred part.  */  
   "LotNum":string,
      /**  The cost added to the asset in the currency specified.  */  
   "DocAdditionCost":number,
      /**  The Grant Amount awarded to an asset to reduce the depreciation charge in the currency specified.  */  
   "DocGrantAmt":number,
      /**  Reporting currency value of the Addition Cost.  */  
   "Rpt1AdditionCost":number,
      /**  Reporting currency value of the Grant Amount.  */  
   "Rpt1GrantAmt":number,
      /**  Reporting currency value of the Addition Cost.  */  
   "Rpt2AdditionCost":number,
      /**  Reporting currency value of the Grant Amount.  */  
   "Rpt2GrantAmt":number,
      /**  Reporting currency value of the Addition Cost.  */  
   "Rpt3AdditionCost":number,
      /**  Reporting currency value of the Grant Amount.  */  
   "Rpt3GrantAmt":number,
      /**  Indicates if the miscellaneous addition is for an Inter-Group addition.  */  
   "InterGroup":boolean,
      /**  Location ID.  */  
   "LocID":string,
      /**  Descriptive code to uniquely identify the Equipment.  */  
   "EquipID":string,
      /**  Brand of equipment  */  
   "Brand":string,
      /**  This is the equivalent number of units for the transferred qty for this asset addition.  There is no unit of measure conversion involved during update of this field.  The user is responsible for the "conversion" of transferred qty to asset units.  */  
   "TransferUnits":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  AssetSeq - used to setup relationship with FAsset table  */  
   "AssetSeq":number,
      /**  shows if is this addition transaction is blocked in RvLock.  */  
   "IsLcked":boolean,
      /**  Locked means can not be updated or deleted: the addition activity is already in review journal or in posting process.  */  
   "LockStatus":string,
      /**  Review Journal UID  */  
   "RvnJrnUID":number,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "BaseCurrDocumentDesc":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "BaseCurrCurrencyID":string,
      /**  Description of the currency  */  
   "BaseCurrCurrDesc":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "BaseCurrCurrSymbol":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "BaseCurrCurrName":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "CurrencyCurrName":string,
      /**  Description of the currency  */  
   "CurrencyCurrDesc":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "CurrencyCurrSymbol":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "CurrencyCurrencyID":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "CurrencyDocumentDesc":string,
      /**  Describes the Part.  */  
   "PartPartDescription":string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   "PartTrackLots":boolean,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "PartSellingFactor":number,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   "PartIUM":string,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   "PartPricePerCode":string,
      /**  Indicates if this part is serial number tracked  */  
   "PartTrackSerialNum":boolean,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   "PartTrackDimension":boolean,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   "PartSalesUM":string,
      /**  Long Description of a unit of measure. Mandatory.  */  
   "UOMUOMDesc":string,
      /**  Description.  */  
   "WhseDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_FAAdditionRow{
      /**  Company of the Addition.  */  
   "Company":string,
      /**  Asset number of the Addition.  */  
   "AssetNum":string,
      /**  Unique number to identify the Addition of an asset.  */  
   "AdditionNum":number,
      /**  The date of Addition  */  
   "Added":string,
      /**  The cost added to the asset.  */  
   "AdditionCost":number,
      /**  Description of the Addition.  */  
   "Description":string,
      /**  The vendor of the Addition. Defaulted from the asset.  */  
   "VendorNum":number,
      /**  The Vendorname of the vendor of the addtion. The Vendor name can be entered without entering a vendor. Defaulted from the asset.  */  
   "VendorName":string,
      /**  The Vendors invoice number. Defaulted from the Asset.  */  
   "InvoiceNum":string,
      /**  The vendors PO number of the Addition. Defaulted from the asset.  */  
   "PONum":number,
      /**  The jobnumber that created the Addition. Defaulted from the asset.  */  
   "JobNum":string,
      /**  The warehouse where the addition is stored. This is for information purposes only. In the warehouse tracker no assets can be tracked.  */  
   "WarehouseCode":string,
      /**  The bin where the addition is stored. This is for information purposes only. In the bin tracker no assets can be tracked.  */  
   "BinNum":string,
      /**  A freeform field to indicate the location of the addition.  */  
   "Location":string,
      /**  The original manufacturer of the addition.  */  
   "Manufacturer":string,
      /**  The model number of addition.  */  
   "Model":string,
      /**  The serial number of the addition.  */  
   "Serialno":string,
      /**  Indicator to express if this addition is bought new.  */  
   "NewAsset":boolean,
      /**  Flag to indicate that the addition is posted to the GL. After posting modification of the addition is not allowed.  */  
   "Posted":boolean,
      /**  Posting date of the addition to the GL.  */  
   "PostDate":string,
      /**  The addition is posted by the user.  */  
   "PostedBy":string,
      /**  The GL journal to which the addition is posted.  */  
   "JournalCode":string,
      /**  The GL journal number to which the addition is posted.  */  
   "JournalNum":number,
      /**  The fiscal year of posting of the addition to the GL.  */  
   "FiscalYear":number,
      /**  The fiscal period of posting of the addition to the GL.  */  
   "FiscalPeriod":number,
      /**  Flag to indicat that the addition is allowed to be posted to the GL.  */  
   "ReadyToPost":boolean,
      /**  Fiscal year suffix  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  The Grant Amount awarded to an asset to reduce the depreciation charge.  */  
   "GrantAmt":number,
      /**  Indicates the type of asset addition activity.  Valid values are: "PURCHASE", "TRANSFER" or "MISC".  */  
   "AdditionType":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Unique identifier of the currency rate group.  */  
   "RateGrpCode":string,
      /**  The Invoice Line of the related or linked AP Invoice.  */  
   "InvoiceLine":number,
      /**  Identifies the part number transferred from stock to asset.  This field is only required if the Addition Type is "Transfer".  */  
   "PartNum":string,
      /**  Transferred Quantity reported for this addition transfer.  */  
   "TransferQty":number,
      /**  Unit of Measure for the transferred quantity.  */  
   "TransferUOM":string,
      /**  Lot Number of the transferred part.  */  
   "LotNum":string,
      /**  The cost added to the asset in the currency specified.  */  
   "DocAdditionCost":number,
      /**  The Grant Amount awarded to an asset to reduce the depreciation charge in the currency specified.  */  
   "DocGrantAmt":number,
      /**  Reporting currency value of the Addition Cost.  */  
   "Rpt1AdditionCost":number,
      /**  Reporting currency value of the Grant Amount.  */  
   "Rpt1GrantAmt":number,
      /**  Reporting currency value of the Addition Cost.  */  
   "Rpt2AdditionCost":number,
      /**  Reporting currency value of the Grant Amount.  */  
   "Rpt2GrantAmt":number,
      /**  Reporting currency value of the Addition Cost.  */  
   "Rpt3AdditionCost":number,
      /**  Reporting currency value of the Grant Amount.  */  
   "Rpt3GrantAmt":number,
      /**  Indicates if the miscellaneous addition is for an Inter-Group addition.  */  
   "InterGroup":boolean,
      /**  Location ID.  */  
   "LocID":string,
      /**  Descriptive code to uniquely identify the Equipment.  */  
   "EquipID":string,
      /**  Brand of equipment  */  
   "Brand":string,
      /**  This is the equivalent number of units for the transferred qty for this asset addition.  There is no unit of measure conversion involved during update of this field.  The user is responsible for the "conversion" of transferred qty to asset units.  */  
   "TransferUnits":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Indicates that the transaction is reflected in FAsset costs.  */  
   "HdrCostRecorded":boolean,
      /**  List of Asset Registers in which the transaction is reflected.  */  
   "RecordedRegList":string,
      /**  ChangedBy  */  
   "ChangedBy":string,
      /**  ChangeDate  */  
   "ChangeDate":string,
      /**  COIsOneTime  */  
   "COIsOneTime":boolean,
      /**  COOneTimeID  */  
   "COOneTimeID":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  AssetSeq - used to setup relationship with FAsset table  */  
   "AssetSeq":number,
   "BaseCurrCurrencyID":string,
      /**  Indicates whether the serial numbers are required in AssetAddEntry  */  
   "EnableSN":boolean,
      /**  shows if is this addition transaction is blocked in RvLock.  */  
   "IsLcked":boolean,
   "SuppressDateWarning":boolean,
      /**  Locked means can not be updated or deleted: the addition activity is already in review journal or in posting process.  */  
   "LockStatus":string,
      /**  Review Journal UID  */  
   "RvnJrnUID":number,
   "BitFlag":number,
   "CurrencyCurrName":string,
   "CurrencyDocumentDesc":string,
   "CurrencyCurrDesc":string,
   "CurrencyCurrSymbol":string,
   "CurrencyCurrencyID":string,
   "PartPartDescription":string,
   "PartTrackSerialNum":boolean,
   "PartTrackLots":boolean,
   "PartTrackDimension":boolean,
   "PartSellingFactor":number,
   "PartIUM":string,
   "PartSalesUM":string,
   "PartPricePerCode":string,
   "UOMUOMDesc":string,
   "VendorNumAddress2":string,
   "VendorNumCity":string,
   "VendorNumVendorID":string,
   "VendorNumState":string,
   "VendorNumAddress1":string,
   "VendorNumTermsCode":string,
   "VendorNumName":string,
   "VendorNumDefaultFOB":string,
   "VendorNumCountry":string,
   "VendorNumCurrencyCode":string,
   "VendorNumAddress3":string,
   "VendorNumZIP":string,
   "WhseDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_SNFormatRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Site Identifier. This field cannot be blank.  */  
   "Plant":string,
      /**  The PartNum field identifies the Part and is used in the primary key.  */  
   "PartNum":string,
      /**  Number of digits in the serial number  */  
   "NumberOfDigits":number,
      /**  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  */  
   "SNMask":string,
      /**   Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer, Mask
Code/desc required:
CHARACTER`Alphanumeric
INTEGER`NumericOnly
MASK`Serial Mask
This field should be flagged as Include = true in Object Designer.  */  
   "SNBaseDataType":string,
   "SNFormat1":string,
      /**  Whether or not to have leading zeroes  */  
   "LeadingZeroes":boolean,
      /**   Current setting for the prefix that will be attached to all new Serial Numbers as they are generated for Character and Integer format types.
This field should be flagged as Include = true in Object Designer.  */  
   "SNPrefix":string,
      /**  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  */  
   "SNMaskSuffix":string,
      /**  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  */  
   "SNMaskPrefix":string,
      /**  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  */  
   "SNLastUsedSeq":string,
   "HasSerialNumbers":boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "PartPricePerCode":string,
   "PartTrackLots":boolean,
   "PartTrackSerialNum":boolean,
   "PartTrackDimension":boolean,
   "PartSalesUM":string,
   "PartIUM":string,
   "PartSellingFactor":number,
   "PartPartDescription":string,
   "SerialMaskMaskType":number,
   "SerialMaskMask":string,
   "SerialMaskExample":string,
   "SerialMaskDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_SelectedSerialNumbersRow{
      /**  Company  */  
   "Company":string,
      /**  SerialNumber  */  
   "SerialNumber":string,
      /**  Scrapped flag  */  
   "Scrapped":boolean,
      /**  Scrapped reason code  */  
   "ScrappedReasonCode":string,
      /**  Voided flag  */  
   "Voided":boolean,
      /**  Reference field  */  
   "Reference":string,
      /**  Reason code type = s  */  
   "ReasonCodeType":string,
      /**  Reason code description  */  
   "ReasonCodeDesc":string,
      /**  PartNumber  */  
   "PartNum":string,
      /**  Serial number prefix  */  
   "SNPrefix":string,
      /**  Base number used to create the serial number  */  
   "SNBaseNumber":string,
      /**  RowID of the source record for this serial number  */  
   "SourceRowID":string,
      /**  TransType of the record that created this serial number  */  
   "TransType":string,
      /**  True if this serial numbered part passed inspection  */  
   "PassedInspection":boolean,
      /**  Used to flag previously selected serial numbers as deselected  */  
   "Deselected":boolean,
   "KitWhseList":string,
      /**  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a validate type mask was being used where characters were stripped (using ~ in the mask).  */  
   "RawSerialNum":string,
      /**  Action type field used for Kanban receipts to indicate if the new serial number status is Inventory, Scrapped or NonConf.  This requires Code/desc:  1 ` inventory 2 ` Scrapped 3 ` Nonconformance  */  
   "KBLbrAction":number,
      /**  Description field for KBLbrAction ? holds the translated description for the KBLbrAction code for UI display and combo box.  */  
   "KBLbrActionDesc":string,
      /**  If true, then users can not deselect this serial number.  This is used by applications that allow maintenance to the Selected Serial Numbers after update.  */  
   "PreventDeselect":boolean,
      /**  Used only by SN Assignment  */  
   "XRefPartNum":string,
      /**  Used only by SN Assignment: C = Customer Part / I = Internal Part XRef  */  
   "XRefPartType":string,
   "PreDeselected":boolean,
      /**  temporary field used to link the packout lines to ship detail lines  */  
   "poLinkValues":string,
      /**  The mask the was used to generate the serial number  */  
   "SNMask":string,
      /**  Flag to indicate that the SelectedSerialNumbers entry has not yet been saved to the DB for the related transaction. Used to keep track of which deselected serial numbers need to be passed to the transaction update logic.  */  
   "NotSavedToDB":boolean,
   "RowSelected":boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param dateKind
      @param ds
   */  
export interface ChangePlaceInServDate_input{
      /**  Acquired date of Place In Service date  */  
   dateKind:string,
   ds:Erp_Tablesets_AssetAddEntryTableset[],
}

export interface ChangePlaceInServDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AssetAddEntryTableset[],
}
}

   /** Required : 
      @param assetNum
      @param sysRowID
   */  
export interface CheckAssetTransactions_input{
      /**  Asset ID  */  
   assetNum:string,
      /**  SysRowID to be excluded from search  */  
   sysRowID:string,
}

export interface CheckAssetTransactions_output{
      /**  If transaction found: Warning message offering to clear Ready To Post flag; otherwise: an empty string  */  
   returnObj:string,
}

   /** Required : 
      @param assetNum
      @param sysRowID
   */  
export interface ClearReadyToPost_input{
      /**  Asset ID  */  
   assetNum:string,
      /**  SysRowID to be excluded from search  */  
   sysRowID:string,
}

export interface ClearReadyToPost_output{
}

   /** Required : 
      @param assetNum
      @param additionNum
   */  
export interface DeleteByID_input{
   assetNum:string,
   additionNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_AssetAddEntryTableset{
   FAAddition:Erp_Tablesets_FAAdditionRow[],
   FAAdditionAttch:Erp_Tablesets_FAAdditionAttchRow[],
   FAAddReg:Erp_Tablesets_FAAddRegRow[],
   SelectedSerialNumbers:Erp_Tablesets_SelectedSerialNumbersRow[],
   SNFormat:Erp_Tablesets_SNFormatRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_FAAddRegRow{
      /**  Company of the Addition.  */  
   Company:string,
      /**  Asset number of the Addition.  */  
   AssetNum:string,
      /**  Unique number to identify the Addition of an asset.  */  
   AdditionNum:number,
      /**  Identifier of the Asset Register.  */  
   AssetRegID:string,
      /**  The depreciation already applied to this addition in another system in previous years. Applies to inter-group transfers only.  */  
   PrevDepreciation:number,
      /**  The depreciation already applied to this addition in another system within the same holding company for this year. This amount is only posted to the balance sheet and not as charge to the P&L, because the the charge has already been charged in a sister company.  */  
   CurrDepreciation:number,
      /**  Book Value of the addition is a calculated field. It is Addition Cost minus previous years Addition Depreciation minus current year Addition Depreciation.  */  
   BookValue:number,
      /**  Grant Book Value of the addition is a calculated field. It is Grant Amount minus previous years Addition Grant Depreciation minus current year Addition Grant Depreciation.  */  
   GrantBookValue:number,
      /**  The Grant Depreciation already applied to the grant addition from another system for previous years. Applies to inter-group transfers only.  */  
   PrevGrantDep:number,
      /**  The Grant Depreciation already applied to the grant addition from another system for the current year. Applies to inter-group transfers only.  */  
   CurrGrantDep:number,
      /**  The depreciation already applied to this addition in another system in previous years in the specified currency. Applies to inter-group transfers only.  */  
   DocPrevDepreciation:number,
      /**  The depreciation already applied to this addition in another system within the same holding company for this year in the specified currency.  */  
   DocCurrDepreciation:number,
      /**  This is the Addition Book Value in the specified currency.  */  
   DocBookValue:number,
      /**  Grant Book Value of the addition is a calculated field. It is Grant Amount minus previous years Addition Grant Depreciation minus current year Addition Grant Depreciation.  */  
   DocGrantBookValue:number,
      /**  The previous years grant depreciation for this addition in the specified currency.  */  
   DocPrevGrantDep:number,
      /**  The current year grant depreciation for this addition in the specified currency.  */  
   DocCurrGrantDep:number,
      /**  Reporting currency value of the previous years addition depreciation.  */  
   Rpt1PrevDepreciation:number,
      /**  Reporting currency value of the current year addition depreciation.  */  
   Rpt1CurrDepreciation:number,
      /**  Reporting currency value of the addition book value.  */  
   Rpt1BookValue:number,
      /**  Grant Book Value of the addition is a calculated field. It is Grant Amount minus previous years Addition Grant Depreciation minus current year Addition Grant Depreciation.  */  
   Rpt1GrantBookValue:number,
      /**  Reporting currency value of the previous years addition grant depreciation.  */  
   Rpt1PrevGrantDep:number,
      /**  Reporting currency value of the current year addition grant depreciation.  */  
   Rpt1CurrGrantDep:number,
      /**  Reporting currency value of the previous years addition depreciation.  */  
   Rpt2PrevDepreciation:number,
      /**  Reporting currency value of the current year addition depreciation.  */  
   Rpt2CurrDepreciation:number,
      /**  Reporting currency value of the addition book value.  */  
   Rpt2BookValue:number,
      /**  Grant Book Value of the addition is a calculated field. It is Grant Amount minus previous years Addition Grant Depreciation minus current year Addition Grant Depreciation.  */  
   Rpt2GrantBookValue:number,
      /**  Reporting currency value of the previous years addition grant depreciation.  */  
   Rpt2PrevGrantDep:number,
      /**  Reporting currency value of the current year addition grant depreciation.  */  
   Rpt2CurrGrantDep:number,
      /**  Reporting currency value of the previous years addition depreciation.  */  
   Rpt3PrevDepreciation:number,
      /**  Reporting currency value of the current year addition depreciation.  */  
   Rpt3CurrDepreciation:number,
      /**  Reporting currency value of the addition book value.  */  
   Rpt3BookValue:number,
      /**  Grant Book Value of the addition is a calculated field. It is Grant Amount minus previous years Addition Grant Depreciation minus current year Addition Grant Depreciation.  */  
   Rpt3GrantBookValue:number,
      /**  Reporting currency value of the previous years addtion grant depreciation.  */  
   Rpt3PrevGrantDep:number,
      /**  Reporting currency value of the current year addition grant depreciation.  */  
   Rpt3CurrGrantDep:number,
      /**  The cost added to the asset.  */  
   AdditionCost:number,
      /**  The Grant Amount awarded to an asset to reduce the depreciation charge.  */  
   GrantAmt:number,
      /**  The cost added to the asset in the currency specified.  */  
   DocAdditionCost:number,
      /**  The Grant Amount awarded to an asset to reduce the depreciation charge in the currency specified.  */  
   DocGrantAmt:number,
      /**  Reporting currency value of the Addition Cost.  */  
   Rpt1AdditionCost:number,
      /**  Reporting currency value of the Grant Amount.  */  
   Rpt1GrantAmt:number,
      /**  Reporting currency value of the Addition Cost.  */  
   Rpt2AdditionCost:number,
      /**  Reporting currency value of the Grant Amount.  */  
   Rpt2GrantAmt:number,
      /**  Reporting currency value of the Addition Cost.  */  
   Rpt3AdditionCost:number,
      /**  Reporting currency value of the Grant Amount.  */  
   Rpt3GrantAmt:number,
      /**  The cost added to the asset.  */  
   AdditionCostLimit:number,
      /**  The cost added to the asset in the currency specified.  */  
   DocAdditionCostLimit:number,
      /**  Reporting currency value of the Addition Cost.  */  
   Rpt1AdditionCostLimit:number,
      /**  Reporting currency value of the Addition Cost.  */  
   Rpt2AdditionCostLimit:number,
      /**  Reporting currency value of the Addition Cost.  */  
   Rpt3AdditionCostLimit:number,
      /**  The cost added to the asset.  */  
   CostVariance:number,
      /**  The cost added to the asset in the currency specified.  */  
   DocCostVariance:number,
      /**  Reporting currency value of the Addition Cost.  */  
   Rpt1CostVariance:number,
      /**  Reporting currency value of the Addition Cost.  */  
   Rpt2CostVariance:number,
      /**  Reporting currency value of the Addition Cost.  */  
   Rpt3CostVariance:number,
      /**  The cost added to the asset.  */  
   GrantVariance:number,
      /**  The cost added to the asset in the currency specified.  */  
   DocGrantVariance:number,
      /**  Reporting currency value of the Addition Cost.  */  
   Rpt1GrantVariance:number,
      /**  Reporting currency value of the Addition Cost.  */  
   Rpt2GrantVariance:number,
      /**  Reporting currency value of the Addition Cost.  */  
   Rpt3GrantVariance:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  InclCurrPerDepn  */  
   InclCurrPerDepn:boolean,
      /**  Affects Asset Life  */  
   AffectsAssetLife:boolean,
      /**  New Asset Estimated Life  */  
   NewAssetLife:number,
      /**  New Life Modifier. Available Values (PERIODS or YEARS)  */  
   NewLifeModifier:string,
   DisableInclCurrPerDepn:boolean,
   RateGrpCode:string,
      /**  Currency Code  */  
   CurrCode:string,
      /**  Current Asset Estimated Life  */  
   CurrAssetLife:number,
      /**  Current Life Modifier  */  
   CurrLifeModifier:string,
      /**  Current Asset Estimated Life  */  
   CurrAssetLifeDisplay:string,
   BitFlag:number,
   FAssetAssetDescription:string,
   FAssetRegDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FAAdditionAttchRow{
   Company:string,
   AssetNum:string,
   AdditionNum:number,
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

export interface Erp_Tablesets_FAAdditionListRow{
      /**  Company of the Addition.  */  
   Company:string,
      /**  Asset number of the Addition.  */  
   AssetNum:string,
      /**  Unique number to identify the Addition of an asset.  */  
   AdditionNum:number,
      /**  The date of Addition  */  
   Added:string,
      /**  The cost added to the asset.  */  
   AdditionCost:number,
      /**  Description of the Addition.  */  
   Description:string,
      /**  The vendor of the Addition. Defaulted from the asset.  */  
   VendorNum:number,
      /**  The Vendorname of the vendor of the addtion. The Vendor name can be entered without entering a vendor. Defaulted from the asset.  */  
   VendorName:string,
      /**  The Vendors invoice number. Defaulted from the Asset.  */  
   InvoiceNum:string,
      /**  The vendors PO number of the Addition. Defaulted from the asset.  */  
   PONum:number,
      /**  The jobnumber that created the Addition. Defaulted from the asset.  */  
   JobNum:string,
      /**  The warehouse where the addition is stored. This is for information purposes only. In the warehouse tracker no assets can be tracked.  */  
   WarehouseCode:string,
      /**  The bin where the addition is stored. This is for information purposes only. In the bin tracker no assets can be tracked.  */  
   BinNum:string,
      /**  A freeform field to indicate the location of the addition.  */  
   Location:string,
      /**  The original manufacturer of the addition.  */  
   Manufacturer:string,
      /**  The model number of addition.  */  
   Model:string,
      /**  The serial number of the addition.  */  
   Serialno:string,
      /**  Indicator to express if this addition is bought new.  */  
   NewAsset:boolean,
      /**  Flag to indicate that the addition is posted to the GL. After posting modification of the addition is not allowed.  */  
   Posted:boolean,
      /**  Posting date of the addition to the GL.  */  
   PostDate:string,
      /**  The addition is posted by the user.  */  
   PostedBy:string,
      /**  The GL journal to which the addition is posted.  */  
   JournalCode:string,
      /**  The GL journal number to which the addition is posted.  */  
   JournalNum:number,
      /**  The fiscal year of posting of the addition to the GL.  */  
   FiscalYear:number,
      /**  The fiscal period of posting of the addition to the GL.  */  
   FiscalPeriod:number,
      /**  Flag to indicat that the addition is allowed to be posted to the GL.  */  
   ReadyToPost:boolean,
      /**  Fiscal year suffix  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  The Grant Amount awarded to an asset to reduce the depreciation charge.  */  
   GrantAmt:number,
      /**  Indicates the type of asset addition activity.  Valid values are: "PURCHASE", "TRANSFER" or "MISC".  */  
   AdditionType:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Unique identifier of the currency rate group.  */  
   RateGrpCode:string,
      /**  The Invoice Line of the related or linked AP Invoice.  */  
   InvoiceLine:number,
      /**  Identifies the part number transferred from stock to asset.  This field is only required if the Addition Type is "Transfer".  */  
   PartNum:string,
      /**  Transferred Quantity reported for this addition transfer.  */  
   TransferQty:number,
      /**  Unit of Measure for the transferred quantity.  */  
   TransferUOM:string,
      /**  Lot Number of the transferred part.  */  
   LotNum:string,
      /**  The cost added to the asset in the currency specified.  */  
   DocAdditionCost:number,
      /**  The Grant Amount awarded to an asset to reduce the depreciation charge in the currency specified.  */  
   DocGrantAmt:number,
      /**  Reporting currency value of the Addition Cost.  */  
   Rpt1AdditionCost:number,
      /**  Reporting currency value of the Grant Amount.  */  
   Rpt1GrantAmt:number,
      /**  Reporting currency value of the Addition Cost.  */  
   Rpt2AdditionCost:number,
      /**  Reporting currency value of the Grant Amount.  */  
   Rpt2GrantAmt:number,
      /**  Reporting currency value of the Addition Cost.  */  
   Rpt3AdditionCost:number,
      /**  Reporting currency value of the Grant Amount.  */  
   Rpt3GrantAmt:number,
      /**  Indicates if the miscellaneous addition is for an Inter-Group addition.  */  
   InterGroup:boolean,
      /**  Location ID.  */  
   LocID:string,
      /**  Descriptive code to uniquely identify the Equipment.  */  
   EquipID:string,
      /**  Brand of equipment  */  
   Brand:string,
      /**  This is the equivalent number of units for the transferred qty for this asset addition.  There is no unit of measure conversion involved during update of this field.  The user is responsible for the "conversion" of transferred qty to asset units.  */  
   TransferUnits:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  AssetSeq - used to setup relationship with FAsset table  */  
   AssetSeq:number,
      /**  shows if is this addition transaction is blocked in RvLock.  */  
   IsLcked:boolean,
      /**  Locked means can not be updated or deleted: the addition activity is already in review journal or in posting process.  */  
   LockStatus:string,
      /**  Review Journal UID  */  
   RvnJrnUID:number,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   BaseCurrDocumentDesc:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   BaseCurrCurrencyID:string,
      /**  Description of the currency  */  
   BaseCurrCurrDesc:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   BaseCurrCurrSymbol:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   BaseCurrCurrName:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   CurrencyCurrName:string,
      /**  Description of the currency  */  
   CurrencyCurrDesc:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   CurrencyCurrSymbol:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   CurrencyCurrencyID:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   CurrencyDocumentDesc:string,
      /**  Describes the Part.  */  
   PartPartDescription:string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   PartTrackLots:boolean,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   PartSellingFactor:number,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   PartIUM:string,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   PartPricePerCode:string,
      /**  Indicates if this part is serial number tracked  */  
   PartTrackSerialNum:boolean,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   PartTrackDimension:boolean,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   PartSalesUM:string,
      /**  Long Description of a unit of measure. Mandatory.  */  
   UOMUOMDesc:string,
      /**  Description.  */  
   WhseDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FAAdditionListTableset{
   FAAdditionList:Erp_Tablesets_FAAdditionListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_FAAdditionRow{
      /**  Company of the Addition.  */  
   Company:string,
      /**  Asset number of the Addition.  */  
   AssetNum:string,
      /**  Unique number to identify the Addition of an asset.  */  
   AdditionNum:number,
      /**  The date of Addition  */  
   Added:string,
      /**  The cost added to the asset.  */  
   AdditionCost:number,
      /**  Description of the Addition.  */  
   Description:string,
      /**  The vendor of the Addition. Defaulted from the asset.  */  
   VendorNum:number,
      /**  The Vendorname of the vendor of the addtion. The Vendor name can be entered without entering a vendor. Defaulted from the asset.  */  
   VendorName:string,
      /**  The Vendors invoice number. Defaulted from the Asset.  */  
   InvoiceNum:string,
      /**  The vendors PO number of the Addition. Defaulted from the asset.  */  
   PONum:number,
      /**  The jobnumber that created the Addition. Defaulted from the asset.  */  
   JobNum:string,
      /**  The warehouse where the addition is stored. This is for information purposes only. In the warehouse tracker no assets can be tracked.  */  
   WarehouseCode:string,
      /**  The bin where the addition is stored. This is for information purposes only. In the bin tracker no assets can be tracked.  */  
   BinNum:string,
      /**  A freeform field to indicate the location of the addition.  */  
   Location:string,
      /**  The original manufacturer of the addition.  */  
   Manufacturer:string,
      /**  The model number of addition.  */  
   Model:string,
      /**  The serial number of the addition.  */  
   Serialno:string,
      /**  Indicator to express if this addition is bought new.  */  
   NewAsset:boolean,
      /**  Flag to indicate that the addition is posted to the GL. After posting modification of the addition is not allowed.  */  
   Posted:boolean,
      /**  Posting date of the addition to the GL.  */  
   PostDate:string,
      /**  The addition is posted by the user.  */  
   PostedBy:string,
      /**  The GL journal to which the addition is posted.  */  
   JournalCode:string,
      /**  The GL journal number to which the addition is posted.  */  
   JournalNum:number,
      /**  The fiscal year of posting of the addition to the GL.  */  
   FiscalYear:number,
      /**  The fiscal period of posting of the addition to the GL.  */  
   FiscalPeriod:number,
      /**  Flag to indicat that the addition is allowed to be posted to the GL.  */  
   ReadyToPost:boolean,
      /**  Fiscal year suffix  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  The Grant Amount awarded to an asset to reduce the depreciation charge.  */  
   GrantAmt:number,
      /**  Indicates the type of asset addition activity.  Valid values are: "PURCHASE", "TRANSFER" or "MISC".  */  
   AdditionType:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Unique identifier of the currency rate group.  */  
   RateGrpCode:string,
      /**  The Invoice Line of the related or linked AP Invoice.  */  
   InvoiceLine:number,
      /**  Identifies the part number transferred from stock to asset.  This field is only required if the Addition Type is "Transfer".  */  
   PartNum:string,
      /**  Transferred Quantity reported for this addition transfer.  */  
   TransferQty:number,
      /**  Unit of Measure for the transferred quantity.  */  
   TransferUOM:string,
      /**  Lot Number of the transferred part.  */  
   LotNum:string,
      /**  The cost added to the asset in the currency specified.  */  
   DocAdditionCost:number,
      /**  The Grant Amount awarded to an asset to reduce the depreciation charge in the currency specified.  */  
   DocGrantAmt:number,
      /**  Reporting currency value of the Addition Cost.  */  
   Rpt1AdditionCost:number,
      /**  Reporting currency value of the Grant Amount.  */  
   Rpt1GrantAmt:number,
      /**  Reporting currency value of the Addition Cost.  */  
   Rpt2AdditionCost:number,
      /**  Reporting currency value of the Grant Amount.  */  
   Rpt2GrantAmt:number,
      /**  Reporting currency value of the Addition Cost.  */  
   Rpt3AdditionCost:number,
      /**  Reporting currency value of the Grant Amount.  */  
   Rpt3GrantAmt:number,
      /**  Indicates if the miscellaneous addition is for an Inter-Group addition.  */  
   InterGroup:boolean,
      /**  Location ID.  */  
   LocID:string,
      /**  Descriptive code to uniquely identify the Equipment.  */  
   EquipID:string,
      /**  Brand of equipment  */  
   Brand:string,
      /**  This is the equivalent number of units for the transferred qty for this asset addition.  There is no unit of measure conversion involved during update of this field.  The user is responsible for the "conversion" of transferred qty to asset units.  */  
   TransferUnits:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates that the transaction is reflected in FAsset costs.  */  
   HdrCostRecorded:boolean,
      /**  List of Asset Registers in which the transaction is reflected.  */  
   RecordedRegList:string,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  ChangeDate  */  
   ChangeDate:string,
      /**  COIsOneTime  */  
   COIsOneTime:boolean,
      /**  COOneTimeID  */  
   COOneTimeID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  AssetSeq - used to setup relationship with FAsset table  */  
   AssetSeq:number,
   BaseCurrCurrencyID:string,
      /**  Indicates whether the serial numbers are required in AssetAddEntry  */  
   EnableSN:boolean,
      /**  shows if is this addition transaction is blocked in RvLock.  */  
   IsLcked:boolean,
   SuppressDateWarning:boolean,
      /**  Locked means can not be updated or deleted: the addition activity is already in review journal or in posting process.  */  
   LockStatus:string,
      /**  Review Journal UID  */  
   RvnJrnUID:number,
   BitFlag:number,
   CurrencyCurrName:string,
   CurrencyDocumentDesc:string,
   CurrencyCurrDesc:string,
   CurrencyCurrSymbol:string,
   CurrencyCurrencyID:string,
   PartPartDescription:string,
   PartTrackSerialNum:boolean,
   PartTrackLots:boolean,
   PartTrackDimension:boolean,
   PartSellingFactor:number,
   PartIUM:string,
   PartSalesUM:string,
   PartPricePerCode:string,
   UOMUOMDesc:string,
   VendorNumAddress2:string,
   VendorNumCity:string,
   VendorNumVendorID:string,
   VendorNumState:string,
   VendorNumAddress1:string,
   VendorNumTermsCode:string,
   VendorNumName:string,
   VendorNumDefaultFOB:string,
   VendorNumCountry:string,
   VendorNumCurrencyCode:string,
   VendorNumAddress3:string,
   VendorNumZIP:string,
   WhseDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SNFormatRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Site Identifier. This field cannot be blank.  */  
   Plant:string,
      /**  The PartNum field identifies the Part and is used in the primary key.  */  
   PartNum:string,
      /**  Number of digits in the serial number  */  
   NumberOfDigits:number,
      /**  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  */  
   SNMask:string,
      /**   Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer, Mask
Code/desc required:
CHARACTER`Alphanumeric
INTEGER`NumericOnly
MASK`Serial Mask
This field should be flagged as Include = true in Object Designer.  */  
   SNBaseDataType:string,
      /**   Current setting for Format of the Base serial number that will be used as new serial numbers are generated. Expressed in progress syntax. Ex: X(30), 99999999 for Character or Integer, or as a Serial Mask defined in SerialMask table.
This field should be flagged as ReadOnly and Include = true in Object Designer.  */  
   SNFormat:string,
      /**  Whether or not to have leading zeroes  */  
   LeadingZeroes:boolean,
      /**   Current setting for the prefix that will be attached to all new Serial Numbers as they are generated for Character and Integer format types.
This field should be flagged as Include = true in Object Designer.  */  
   SNPrefix:string,
      /**  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  */  
   SNMaskSuffix:string,
      /**  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  */  
   SNMaskPrefix:string,
      /**  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  */  
   SNLastUsedSeq:string,
   HasSerialNumbers:boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   PartPricePerCode:string,
   PartTrackLots:boolean,
   PartTrackSerialNum:boolean,
   PartTrackDimension:boolean,
   PartSalesUM:string,
   PartIUM:string,
   PartSellingFactor:number,
   PartPartDescription:string,
   SerialMaskMaskType:number,
   SerialMaskMask:string,
   SerialMaskExample:string,
   SerialMaskDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SelectSerialNumbersParamsRow{
      /**  The part number to which the serial numbers have been assigned.  */  
   partNum:string,
      /**  The quantity of serial numbers that need to be selected.  */  
   quantity:number,
      /**  whereClause for filtering available serial numbers  */  
   whereClause:string,
      /**  transType of this transaction  */  
   transType:string,
      /**  Include when filtering a set of SN's for BL processing is necessary.  It may be null if not needed.  */  
   sourceRowID:string,
      /**  Determines if serial numbers can be created.  */  
   enableCreate:boolean,
      /**  Determines if serial numbers can be selected.  */  
   enableSelect:boolean,
      /**  Determines if serial numbers can be retrieved.  */  
   enableRetrieve:boolean,
      /**  Specifies whether Voided serial numbers can be manually selected.  */  
   allowVoided:boolean,
      /**  The Plant associated with this transaction  */  
   plant:string,
   xrefPartNum:string,
   xrefPartType:string,
   xrefCustNum:number,
      /**  temporary field used to link the packout lines to ship detail lines  */  
   poLinkValues:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   attributeSetID:number,
      /**  The Short Description of the Attribute Set.  */  
   attributeSetShortDescription:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   revisionNum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SelectSerialNumbersParamsTableset{
   SelectSerialNumbersParams:Erp_Tablesets_SelectSerialNumbersParamsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_SelectedSerialNumbersRow{
      /**  Company  */  
   Company:string,
      /**  SerialNumber  */  
   SerialNumber:string,
      /**  Scrapped flag  */  
   Scrapped:boolean,
      /**  Scrapped reason code  */  
   ScrappedReasonCode:string,
      /**  Voided flag  */  
   Voided:boolean,
      /**  Reference field  */  
   Reference:string,
      /**  Reason code type = s  */  
   ReasonCodeType:string,
      /**  Reason code description  */  
   ReasonCodeDesc:string,
      /**  PartNumber  */  
   PartNum:string,
      /**  Serial number prefix  */  
   SNPrefix:string,
      /**  Base number used to create the serial number  */  
   SNBaseNumber:string,
      /**  RowID of the source record for this serial number  */  
   SourceRowID:string,
      /**  TransType of the record that created this serial number  */  
   TransType:string,
      /**  True if this serial numbered part passed inspection  */  
   PassedInspection:boolean,
      /**  Used to flag previously selected serial numbers as deselected  */  
   Deselected:boolean,
   KitWhseList:string,
      /**  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a validate type mask was being used where characters were stripped (using ~ in the mask).  */  
   RawSerialNum:string,
      /**  Action type field used for Kanban receipts to indicate if the new serial number status is Inventory, Scrapped or NonConf.  This requires Code/desc:  1 ` inventory 2 ` Scrapped 3 ` Nonconformance  */  
   KBLbrAction:number,
      /**  Description field for KBLbrAction ? holds the translated description for the KBLbrAction code for UI display and combo box.  */  
   KBLbrActionDesc:string,
      /**  If true, then users can not deselect this serial number.  This is used by applications that allow maintenance to the Selected Serial Numbers after update.  */  
   PreventDeselect:boolean,
      /**  Used only by SN Assignment  */  
   XRefPartNum:string,
      /**  Used only by SN Assignment: C = Customer Part / I = Internal Part XRef  */  
   XRefPartType:string,
   PreDeselected:boolean,
      /**  temporary field used to link the packout lines to ship detail lines  */  
   poLinkValues:string,
      /**  The mask the was used to generate the serial number  */  
   SNMask:string,
      /**  Flag to indicate that the SelectedSerialNumbers entry has not yet been saved to the DB for the related transaction. Used to keep track of which deselected serial numbers need to be passed to the transaction update logic.  */  
   NotSavedToDB:boolean,
   RowSelected:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtAssetAddEntryTableset{
   FAAddition:Erp_Tablesets_FAAdditionRow[],
   FAAdditionAttch:Erp_Tablesets_FAAdditionAttchRow[],
   FAAddReg:Erp_Tablesets_FAAddRegRow[],
   SelectedSerialNumbers:Erp_Tablesets_SelectedSerialNumbersRow[],
   SNFormat:Erp_Tablesets_SNFormatRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param assetNum
      @param additionNum
   */  
export interface GetByID_input{
   assetNum:string,
   additionNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_AssetAddEntryTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_AssetAddEntryTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_AssetAddEntryTableset[],
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
   returnObj:Erp_Tablesets_FAAdditionListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param assetNum
      @param additionNum
   */  
export interface GetNewFAAddReg_input{
   ds:Erp_Tablesets_AssetAddEntryTableset[],
   assetNum:string,
   additionNum:number,
}

export interface GetNewFAAddReg_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AssetAddEntryTableset[],
}
}

   /** Required : 
      @param ds
      @param assetNum
      @param additionNum
   */  
export interface GetNewFAAdditionAttch_input{
   ds:Erp_Tablesets_AssetAddEntryTableset[],
   assetNum:string,
   additionNum:number,
}

export interface GetNewFAAdditionAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AssetAddEntryTableset[],
}
}

   /** Required : 
      @param ds
      @param assetNum
   */  
export interface GetNewFAAddition_input{
   ds:Erp_Tablesets_AssetAddEntryTableset[],
   assetNum:string,
}

export interface GetNewFAAddition_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AssetAddEntryTableset[],
}
}

   /** Required : 
      @param whereClauseFAAddition
      @param whereClauseFAAdditionAttch
      @param whereClauseFAAddReg
      @param whereClauseSelectedSerialNumbers
      @param whereClauseSNFormat
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseFAAddition:string,
   whereClauseFAAdditionAttch:string,
   whereClauseFAAddReg:string,
   whereClauseSelectedSerialNumbers:string,
   whereClauseSNFormat:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_AssetAddEntryTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetSelectSerialNumbersParams_input{
   ds:Erp_Tablesets_AssetAddEntryTableset[],
}

export interface GetSelectSerialNumbersParams_output{
   returnObj:Erp_Tablesets_SelectSerialNumbersParamsTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AssetAddEntryTableset[],
}
}

   /** Required : 
      @param company
      @param assetNum
      @param additionNum
      @param ds
   */  
export interface GetSelectedSerialNumbers_input{
      /**  The Asset Number  */  
   company:string,
      /**  The Asset Number  */  
   assetNum:string,
      /**  The Addition number  */  
   additionNum:number,
   ds:Erp_Tablesets_AssetAddEntryTableset[],
}

export interface GetSelectedSerialNumbers_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AssetAddEntryTableset[],
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
      @param ipAdded
      @param ds
   */  
export interface LeaveAdded_input{
      /**  Added Date that was entered.  */  
   ipAdded:string,
   ds:Erp_Tablesets_AssetAddEntryTableset[],
}

export interface LeaveAdded_output{
parameters : {
      /**  output parameters  */  
   warning:string,
   ds:Erp_Tablesets_AssetAddEntryTableset[],
}
}

   /** Required : 
      @param ipAdditionCost
      @param ipbaseordoc
      @param ds
   */  
export interface LeaveAdditionCost_input{
      /**  AdditionCost that was entered.  */  
   ipAdditionCost:number,
      /**  The field type - base or doc  */  
   ipbaseordoc:string,
   ds:Erp_Tablesets_AssetAddEntryTableset[],
}

export interface LeaveAdditionCost_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AssetAddEntryTableset[],
   errorMessage:string,
}
}

   /** Required : 
      @param ipAdditionType
      @param ds
   */  
export interface LeaveAdditionType_input{
      /**  addition type that was selected.  */  
   ipAdditionType:string,
   ds:Erp_Tablesets_AssetAddEntryTableset[],
}

export interface LeaveAdditionType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AssetAddEntryTableset[],
   oSerialWarning:string,
}
}

   /** Required : 
      @param ipGrantAmt
      @param ipbaseordoc
      @param ds
   */  
export interface LeaveGrantAmt_input{
      /**  GrantAmt that was entered.  */  
   ipGrantAmt:number,
      /**  The field type - base or doc  */  
   ipbaseordoc:string,
   ds:Erp_Tablesets_AssetAddEntryTableset[],
}

export interface LeaveGrantAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AssetAddEntryTableset[],
}
}

   /** Required : 
      @param ipInvoiceLine
      @param ds
   */  
export interface LeaveInvoiceLine_input{
      /**  Invoice Line Number that was entered.  */  
   ipInvoiceLine:number,
   ds:Erp_Tablesets_AssetAddEntryTableset[],
}

export interface LeaveInvoiceLine_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AssetAddEntryTableset[],
}
}

   /** Required : 
      @param ipInvoiceNum
      @param ds
   */  
export interface LeaveInvoiceNum_input{
      /**  Invoice Number that was entered.  */  
   ipInvoiceNum:string,
   ds:Erp_Tablesets_AssetAddEntryTableset[],
}

export interface LeaveInvoiceNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AssetAddEntryTableset[],
}
}

   /** Required : 
      @param IP_JobNum
      @param ds
   */  
export interface LeaveJobNum_input{
      /**  Job Number that was entered.  */  
   IP_JobNum:string,
   ds:Erp_Tablesets_AssetAddEntryTableset[],
}

export interface LeaveJobNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AssetAddEntryTableset[],
}
}

   /** Required : 
      @param ipLotNum
      @param ds
   */  
export interface LeaveLotNum_input{
      /**  Lot Number that was entered.  */  
   ipLotNum:string,
   ds:Erp_Tablesets_AssetAddEntryTableset[],
}

export interface LeaveLotNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AssetAddEntryTableset[],
}
}

   /** Required : 
      @param IP_PONum
      @param ds
   */  
export interface LeavePONum_input{
      /**  PO Number that was entered.  */  
   IP_PONum:number,
   ds:Erp_Tablesets_AssetAddEntryTableset[],
}

export interface LeavePONum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AssetAddEntryTableset[],
}
}

   /** Required : 
      @param ipPartNum
      @param ds
   */  
export interface LeavePartNum_input{
      /**  partnum that was entered.  */  
   ipPartNum:string,
   ds:Erp_Tablesets_AssetAddEntryTableset[],
}

export interface LeavePartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AssetAddEntryTableset[],
   oSerialWarning:string,
}
}

   /** Required : 
      @param ipAssetNum
      @param ipAdditionNum
      @param ipAssetRegID
      @param ipCurrDepreciation
      @param ipAdditionCost
      @param ipGrantAmt
      @param ipBaseOrDoc
      @param ds
   */  
export interface LeaveRegCurrDepreciation_input{
      /**  asset number  */  
   ipAssetNum:string,
      /**  asset addition number  */  
   ipAdditionNum:number,
      /**  asset register ID  */  
   ipAssetRegID:string,
      /**  current depreciation that was entered.  */  
   ipCurrDepreciation:number,
      /**  addition cost  */  
   ipAdditionCost:number,
      /**  grant amount  */  
   ipGrantAmt:number,
      /**  The field type - base or doc  */  
   ipBaseOrDoc:string,
   ds:Erp_Tablesets_AssetAddEntryTableset[],
}

export interface LeaveRegCurrDepreciation_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AssetAddEntryTableset[],
}
}

   /** Required : 
      @param ipAssetNum
      @param ipAdditionNum
      @param ipAssetRegID
      @param ipCurrGrantDep
      @param ipGrantAmt
      @param ipBaseOrDoc
      @param ds
   */  
export interface LeaveRegCurrGrantDep_input{
      /**  asset number  */  
   ipAssetNum:string,
      /**  asset addition number  */  
   ipAdditionNum:number,
      /**  asset register ID  */  
   ipAssetRegID:string,
      /**  current depreciation that was entered.  */  
   ipCurrGrantDep:number,
      /**  grant amount  */  
   ipGrantAmt:number,
      /**  The field type - base or doc  */  
   ipBaseOrDoc:string,
   ds:Erp_Tablesets_AssetAddEntryTableset[],
}

export interface LeaveRegCurrGrantDep_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AssetAddEntryTableset[],
}
}

   /** Required : 
      @param ipAssetNum
      @param ipAdditionNum
      @param ipAssetRegID
      @param ipPrevDepreciation
      @param ipAdditionCost
      @param ipGrantAmt
      @param ipBaseOrDoc
      @param ds
   */  
export interface LeaveRegPrevDepreciation_input{
      /**  asset number  */  
   ipAssetNum:string,
      /**  asset addition number  */  
   ipAdditionNum:number,
      /**  asset register ID  */  
   ipAssetRegID:string,
      /**  previous years depreciation that was entered.  */  
   ipPrevDepreciation:number,
      /**  addition cost  */  
   ipAdditionCost:number,
      /**  grant amount  */  
   ipGrantAmt:number,
      /**  The field type - base or doc  */  
   ipBaseOrDoc:string,
   ds:Erp_Tablesets_AssetAddEntryTableset[],
}

export interface LeaveRegPrevDepreciation_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AssetAddEntryTableset[],
}
}

   /** Required : 
      @param ipAssetNum
      @param ipAdditionNum
      @param ipAssetRegID
      @param ipPrevGrantDep
      @param ipGrantAmt
      @param ipBaseOrDoc
      @param ds
   */  
export interface LeaveRegPrevGrantDep_input{
      /**  asset number  */  
   ipAssetNum:string,
      /**  asset addition number  */  
   ipAdditionNum:number,
      /**  asset register ID  */  
   ipAssetRegID:string,
      /**  current depreciation that was entered.  */  
   ipPrevGrantDep:number,
      /**  grant amount  */  
   ipGrantAmt:number,
      /**  The field type - base or doc  */  
   ipBaseOrDoc:string,
   ds:Erp_Tablesets_AssetAddEntryTableset[],
}

export interface LeaveRegPrevGrantDep_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AssetAddEntryTableset[],
}
}

   /** Required : 
      @param ipTransferQty
      @param ds
   */  
export interface LeaveTransferQty_input{
      /**  Transfer Qty that was entered.  */  
   ipTransferQty:number,
   ds:Erp_Tablesets_AssetAddEntryTableset[],
}

export interface LeaveTransferQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AssetAddEntryTableset[],
   errorMessage:string,
}
}

   /** Required : 
      @param IP_VendorID
      @param ds
   */  
export interface LeaveVendorID_input{
      /**  VendorID or SupplierID that was entered.  */  
   IP_VendorID:string,
   ds:Erp_Tablesets_AssetAddEntryTableset[],
}

export interface LeaveVendorID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AssetAddEntryTableset[],
}
}

   /** Required : 
      @param ipWarehouseCode
      @param ds
   */  
export interface LeaveWarehouse_input{
      /**  Warehouse Code that was entered.  */  
   ipWarehouseCode:string,
   ds:Erp_Tablesets_AssetAddEntryTableset[],
}

export interface LeaveWarehouse_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AssetAddEntryTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface PreUpdate_input{
   ds:Erp_Tablesets_AssetAddEntryTableset[],
}

export interface PreUpdate_output{
parameters : {
      /**  output parameters  */  
   returnMessage:string,
   ds:Erp_Tablesets_AssetAddEntryTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtAssetAddEntryTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtAssetAddEntryTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_AssetAddEntryTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AssetAddEntryTableset[],
}
}

   /** Required : 
      @param ds
      @param serialNumber
   */  
export interface ValidateSN_input{
   ds:Erp_Tablesets_AssetAddEntryTableset[],
      /**  Serial number to validate.  */  
   serialNumber:string,
}

export interface ValidateSN_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AssetAddEntryTableset[],
   isVoided:boolean,
}
}

