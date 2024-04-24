import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.FARevalueSvc
// Description: 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/$metadata", {
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
   Description: Get FARevalues items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FARevalues
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FARevalueRow
   */  
export function get_FARevalues(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FARevalueRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/FARevalues", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FARevalueRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FARevalues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FARevalueRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FARevalueRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FARevalues(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/FARevalues", {
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
   Summary: Calls GetByID to retrieve the FARevalue item
   Description: Calls GetByID to retrieve the FARevalue item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FARevalue
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param RevalueNum Desc: RevalueNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FARevalueRow
   */  
export function get_FARevalues_Company_AssetNum_RevalueNum(Company:string, AssetNum:string, RevalueNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FARevalueRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/FARevalues(" + Company + "," + AssetNum + "," + RevalueNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FARevalueRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update FARevalue for the service
   Description: Calls UpdateExt to update FARevalue. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FARevalue
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param RevalueNum Desc: RevalueNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FARevalueRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_FARevalues_Company_AssetNum_RevalueNum(Company:string, AssetNum:string, RevalueNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/FARevalues(" + Company + "," + AssetNum + "," + RevalueNum + ")", {
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
   Summary: Call UpdateExt to delete FARevalue item
   Description: Call UpdateExt to delete FARevalue item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FARevalue
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param RevalueNum Desc: RevalueNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_FARevalues_Company_AssetNum_RevalueNum(Company:string, AssetNum:string, RevalueNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/FARevalues(" + Company + "," + AssetNum + "," + RevalueNum + ")", {
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
   Description: Get FARevalueRegs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FARevalueRegs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param RevalueNum Desc: RevalueNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FARevalueRegRow
   */  
export function get_FARevalues_Company_AssetNum_RevalueNum_FARevalueRegs(Company:string, AssetNum:string, RevalueNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FARevalueRegRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/FARevalues(" + Company + "," + AssetNum + "," + RevalueNum + ")/FARevalueRegs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FARevalueRegRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the FARevalueReg item
   Description: Calls GetByID to retrieve the FARevalueReg item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FARevalueReg1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param RevalueNum Desc: RevalueNum   Required: True
      @param AssetRegID Desc: AssetRegID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FARevalueRegRow
   */  
export function get_FARevalues_Company_AssetNum_RevalueNum_FARevalueRegs_Company_AssetNum_RevalueNum_AssetRegID(Company:string, AssetNum:string, RevalueNum:string, AssetRegID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FARevalueRegRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/FARevalues(" + Company + "," + AssetNum + "," + RevalueNum + ")/FARevalueRegs(" + Company + "," + AssetNum + "," + RevalueNum + "," + AssetRegID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FARevalueRegRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get FARevalueAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FARevalueAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param RevalueNum Desc: RevalueNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FARevalueAttchRow
   */  
export function get_FARevalues_Company_AssetNum_RevalueNum_FARevalueAttches(Company:string, AssetNum:string, RevalueNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FARevalueAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/FARevalues(" + Company + "," + AssetNum + "," + RevalueNum + ")/FARevalueAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FARevalueAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the FARevalueAttch item
   Description: Calls GetByID to retrieve the FARevalueAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FARevalueAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param RevalueNum Desc: RevalueNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FARevalueAttchRow
   */  
export function get_FARevalues_Company_AssetNum_RevalueNum_FARevalueAttches_Company_AssetNum_RevalueNum_DrawingSeq(Company:string, AssetNum:string, RevalueNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FARevalueAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/FARevalues(" + Company + "," + AssetNum + "," + RevalueNum + ")/FARevalueAttches(" + Company + "," + AssetNum + "," + RevalueNum + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FARevalueAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get FARevalueRegs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FARevalueRegs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FARevalueRegRow
   */  
export function get_FARevalueRegs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FARevalueRegRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/FARevalueRegs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FARevalueRegRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FARevalueRegs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FARevalueRegRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FARevalueRegRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FARevalueRegs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/FARevalueRegs", {
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
   Summary: Calls GetByID to retrieve the FARevalueReg item
   Description: Calls GetByID to retrieve the FARevalueReg item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FARevalueReg
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param RevalueNum Desc: RevalueNum   Required: True
      @param AssetRegID Desc: AssetRegID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FARevalueRegRow
   */  
export function get_FARevalueRegs_Company_AssetNum_RevalueNum_AssetRegID(Company:string, AssetNum:string, RevalueNum:string, AssetRegID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FARevalueRegRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/FARevalueRegs(" + Company + "," + AssetNum + "," + RevalueNum + "," + AssetRegID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FARevalueRegRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update FARevalueReg for the service
   Description: Calls UpdateExt to update FARevalueReg. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FARevalueReg
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param RevalueNum Desc: RevalueNum   Required: True
      @param AssetRegID Desc: AssetRegID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FARevalueRegRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_FARevalueRegs_Company_AssetNum_RevalueNum_AssetRegID(Company:string, AssetNum:string, RevalueNum:string, AssetRegID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/FARevalueRegs(" + Company + "," + AssetNum + "," + RevalueNum + "," + AssetRegID + ")", {
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
   Summary: Call UpdateExt to delete FARevalueReg item
   Description: Call UpdateExt to delete FARevalueReg item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FARevalueReg
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param RevalueNum Desc: RevalueNum   Required: True
      @param AssetRegID Desc: AssetRegID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_FARevalueRegs_Company_AssetNum_RevalueNum_AssetRegID(Company:string, AssetNum:string, RevalueNum:string, AssetRegID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/FARevalueRegs(" + Company + "," + AssetNum + "," + RevalueNum + "," + AssetRegID + ")", {
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
   Description: Get FARevalueAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FARevalueAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FARevalueAttchRow
   */  
export function get_FARevalueAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FARevalueAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/FARevalueAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FARevalueAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FARevalueAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FARevalueAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FARevalueAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FARevalueAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/FARevalueAttches", {
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
   Summary: Calls GetByID to retrieve the FARevalueAttch item
   Description: Calls GetByID to retrieve the FARevalueAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FARevalueAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param RevalueNum Desc: RevalueNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FARevalueAttchRow
   */  
export function get_FARevalueAttches_Company_AssetNum_RevalueNum_DrawingSeq(Company:string, AssetNum:string, RevalueNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FARevalueAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/FARevalueAttches(" + Company + "," + AssetNum + "," + RevalueNum + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FARevalueAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update FARevalueAttch for the service
   Description: Calls UpdateExt to update FARevalueAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FARevalueAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param RevalueNum Desc: RevalueNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FARevalueAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_FARevalueAttches_Company_AssetNum_RevalueNum_DrawingSeq(Company:string, AssetNum:string, RevalueNum:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/FARevalueAttches(" + Company + "," + AssetNum + "," + RevalueNum + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete FARevalueAttch item
   Description: Call UpdateExt to delete FARevalueAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FARevalueAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param RevalueNum Desc: RevalueNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_FARevalueAttches_Company_AssetNum_RevalueNum_DrawingSeq(Company:string, AssetNum:string, RevalueNum:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/FARevalueAttches(" + Company + "," + AssetNum + "," + RevalueNum + "," + DrawingSeq + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FARevalueListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FARevalueListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FARevalueListRow)
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
export function get_GetRows(whereClauseFARevalue:string, whereClauseFARevalueAttch:string, whereClauseFARevalueReg:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseFARevalue!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseFARevalue=" + whereClauseFARevalue
   }
   if(typeof whereClauseFARevalueAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseFARevalueAttch=" + whereClauseFARevalueAttch
   }
   if(typeof whereClauseFARevalueReg!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseFARevalueReg=" + whereClauseFARevalueReg
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/GetRows" + params, {
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
export function get_GetByID(assetNum:string, revalueNum:string, epicorHeaders?:Headers){
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
   if(typeof revalueNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "revalueNum=" + revalueNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/GetList" + params, {
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
   Summary: Invoke method GetNewRevaluation
   Description: Get New Revaluation (Substitute method for FARevalueGetNew)
It is required to put ValuationDate and ApplyDate here.
Standart FARevalueGetNew is generated with AssetNum input parameter only
   OperationID: GetNewRevaluation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRevaluation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRevaluation_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRevaluation(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/GetNewRevaluation", {
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
   Summary: Invoke method GetRevaluationsWithRecalc
   Description: Return asset's revaluations with registers recalculated
   OperationID: GetRevaluationsWithRecalc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRevaluationsWithRecalc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRevaluationsWithRecalc_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRevaluationsWithRecalc(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/GetRevaluationsWithRecalc", {
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
   Summary: Invoke method GetAvailableApplyDate
   OperationID: GetAvailableApplyDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAvailableApplyDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailableApplyDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAvailableApplyDate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/GetAvailableApplyDate", {
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
   Summary: Invoke method GetDefaultDates
   OperationID: GetDefaultDates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDefaultDates_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultDates_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDefaultDates(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/GetDefaultDates", {
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
   Summary: Invoke method CheckApplyDateInClosedPer
   OperationID: CheckApplyDateInClosedPer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckApplyDateInClosedPer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckApplyDateInClosedPer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckApplyDateInClosedPer(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/CheckApplyDateInClosedPer", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/CheckAssetTransactions", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/ClearReadyToPost", {
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
   Summary: Invoke method CheckAssetDepRecalcNeeded
   Description: Check if the asset or any of its registers requires depreciation calculation
   OperationID: CheckAssetDepRecalcNeeded
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckAssetDepRecalcNeeded_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckAssetDepRecalcNeeded_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckAssetDepRecalcNeeded(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/CheckAssetDepRecalcNeeded", {
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
   Summary: Invoke method OnChangeNewBookValue
   Description: Calculates the New Book Values amounts for Revaluation.
   OperationID: OnChangeNewBookValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeNewBookValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeNewBookValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeNewBookValue(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/OnChangeNewBookValue", {
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
   Summary: Invoke method OnChangeNewResidualValue
   Description: Calculates the New Residual Values amounts for Revaluation Register Details.
   OperationID: OnChangeNewResidualValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeNewResidualValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeNewResidualValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeNewResidualValue(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/OnChangeNewResidualValue", {
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
   Summary: Invoke method OnChangeReadyToPost
   OperationID: OnChangeReadyToPost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeReadyToPost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeReadyToPost_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeReadyToPost(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/OnChangeReadyToPost", {
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
   Summary: Invoke method OnChangeApplyDate
   OperationID: OnChangeApplyDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeApplyDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeApplyDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeApplyDate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/OnChangeApplyDate", {
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
   Summary: Invoke method OnChangeValuationDate
   OperationID: OnChangeValuationDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeValuationDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeValuationDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeValuationDate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/OnChangeValuationDate", {
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
   Summary: Invoke method GetNewRegistersInfo
   OperationID: GetNewRegistersInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRegistersInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRegistersInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRegistersInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/GetNewRegistersInfo", {
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
   Summary: Invoke method ParseDateValidationMessage
   Description: Parse warning Msg from date validation method.
   OperationID: ParseDateValidationMessage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ParseDateValidationMessage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ParseDateValidationMessage_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ParseDateValidationMessage(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/ParseDateValidationMessage", {
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
   Summary: Invoke method GetNewFARevalue
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFARevalue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFARevalue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFARevalue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewFARevalue(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/GetNewFARevalue", {
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
   Summary: Invoke method GetNewFARevalueAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFARevalueAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFARevalueAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFARevalueAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewFARevalueAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/GetNewFARevalueAttch", {
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
   Summary: Invoke method GetNewFARevalueReg
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFARevalueReg
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFARevalueReg_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFARevalueReg_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewFARevalueReg(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/GetNewFARevalueReg", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FARevalueAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FARevalueAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FARevalueListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FARevalueListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FARevalueRegRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FARevalueRegRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FARevalueRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FARevalueRow[],
}

export interface Erp_Tablesets_FARevalueAttchRow{
   "Company":string,
   "AssetNum":string,
   "RevalueNum":number,
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

export interface Erp_Tablesets_FARevalueListRow{
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_FARevalueRegRow{
      /**  Company  */  
   "Company":string,
      /**  Asset Number  */  
   "AssetNum":string,
      /**  Unique number to identify the Revaluation activity of an asset.  */  
   "RevalueNum":number,
      /**  Identifier of the Asset Register.  */  
   "AssetRegID":string,
      /**  The original Current Asset Cost in base currency before running the Asset Revaluation process.  */  
   "OrigCurrentCost":number,
      /**  The original Current Asset Cost in document currency before running the Asset Revaluation process.  */  
   "DocOrigCurrentCost":number,
      /**  The original Current Asset Cost in reporting currency before running the Asset Revaluation process.  */  
   "Rpt1OrigCurrentCost":number,
      /**  The original Current Asset Cost in reporting currency before running the Asset Revaluation process.  */  
   "Rpt2OrigCurrentCost":number,
      /**  The original Current Asset Cost in reporting currency before running the Asset Revaluation process.  */  
   "Rpt3OrigCurrentCost":number,
      /**  Book Value before revaluation in base currency.  */  
   "OrigBookValue":number,
      /**  Book Value before revaluation in document currency.  */  
   "DocOrigBookValue":number,
      /**  Book Value before revaluation in reporting currency.  */  
   "Rpt1OrigBookValue":number,
      /**  Book Value before revaluation in reporting currency.  */  
   "Rpt2OrigBookValue":number,
      /**  Book Value before revaluation in reporting currency.  */  
   "Rpt3OrigBookValue":number,
      /**  Accumulated depreciation before revaluation (up to revaluation date) in base curreny.  */  
   "OrigTotalDepn":number,
      /**  Accumulated depreciation before revaluation (up to revaluation date) in document curreny.  */  
   "DocOrigTotalDepn":number,
      /**  Accumulated depreciation before revaluation (up to revaluation date) in reporting curreny.  */  
   "Rpt1OrigTotalDepn":number,
      /**  Accumulated depreciation before revaluation (up to revaluation date) in reporting curreny.  */  
   "Rpt2OrigTotalDepn":number,
      /**  Accumulated depreciation before revaluation (up to revaluation date) in reporting curreny.  */  
   "Rpt3OrigTotalDepn":number,
      /**  Revaluation Gain or Loss in base currency. The difference between Original Book Value and New Book Value  */  
   "RevalueGainLoss":number,
      /**  Revaluation Gain or Loss in document currency. The difference between Original Book Value and New Book Value  */  
   "DocRevalueGainLoss":number,
      /**  Revaluation Gain or Loss in reporting currency. The difference between Original Book Value and New Book Value  */  
   "Rpt1RevalueGainLoss":number,
      /**  Revaluation Gain or Loss in reporting currency. The difference between Original Book Value and New Book Value  */  
   "Rpt2RevalueGainLoss":number,
      /**  Revaluation Gain or Loss in reporting currency. The difference between Original Book Value and New Book Value  */  
   "Rpt3RevalueGainLoss":number,
      /**  Revaluation Surplus in base currency. Increase of the asset value that remains after reversing of previous loss (if any).  */  
   "RevalueSurplus":number,
      /**  Revaluation Surplus in document currency. Increase of the asset value that remains after reversing of previous loss (if any).  */  
   "DocRevalueSurplus":number,
      /**  Revaluation Surplus in reporting currency. Increase of the asset value that remains after reversing of previous loss (if any).  */  
   "Rpt1RevalueSurplus":number,
      /**  Revaluation Surplus in reporting currency. Increase of the asset value that remains after reversing of previous loss (if any).  */  
   "Rpt2RevalueSurplus":number,
      /**  Revaluation Surplus in reporting currency. Increase of the asset value that remains after reversing of previous loss (if any).  */  
   "Rpt3RevalueSurplus":number,
      /**  The Grant Amount awarded to an asset to reduce the depreciation charge in base currency.  */  
   "GrantAmt":number,
      /**  The Grant Amount awarded to an asset to reduce the depreciation charge in document currency.  */  
   "DocGrantAmt":number,
      /**  The Grant Amount awarded to an asset to reduce the depreciation charge in reporting currency.  */  
   "Rpt1GrantAmt":number,
      /**  The Grant Amount awarded to an asset to reduce the depreciation charge in reporting currency.  */  
   "Rpt2GrantAmt":number,
      /**  The Grant Amount awarded to an asset to reduce the depreciation charge in reporting currency.  */  
   "Rpt3GrantAmt":number,
      /**  The Grant Depreciation Amount awarded to an asset to reduce the depreciation charge in base currency.  */  
   "GrantDepnAmt":number,
      /**  The Grant Depreciation Amount awarded to an asset to reduce the depreciation charge in document currency.  */  
   "DocGrantDepnAmt":number,
      /**  The Grant Depreciation Amount awarded to an asset to reduce the depreciation charge in reporting currency.  */  
   "Rpt1GrantDepnAmt":number,
      /**  The Grant Depreciation Amount awarded to an asset to reduce the depreciation charge in reporting currency.  */  
   "Rpt2GrantDepnAmt":number,
      /**  The Grant Depreciation Amount awarded to an asset to reduce the depreciation charge in reporting currency.  */  
   "Rpt3GrantDepnAmt":number,
      /**  Grant Book Value at the moment of revaluation in base currency.  */  
   "UnusedGrantAmt":number,
      /**  Grant Book Value at the moment of revaluation in document currency.  */  
   "DocUnusedGrantAmt":number,
      /**  Grant Book Value at the moment of revaluation in reporting currency.  */  
   "Rpt1UnusedGrantAmt":number,
      /**  Grant Book Value at the moment of revaluation in reporting currency.  */  
   "Rpt2UnusedGrantAmt":number,
      /**  Grant Book Value at the moment of revaluation in reporting currency.  */  
   "Rpt3UnusedGrantAmt":number,
      /**  The Depreciation value in the base currency posted to the GL after Revaluation Date.  */  
   "PostedFutrDepnAmt":number,
      /**  The Depreciation value in the documnet currency posted to the GL after Revaluation Date.  */  
   "DocPostedFutrDepnAmt":number,
      /**  The Depreciation value in the reporting currency posted to the GL after Revaluation Date.  */  
   "Rpt1PostedFutrDepnAmt":number,
      /**  The Depreciation value in the reporting currency posted to the GL after Revaluation Date.  */  
   "Rpt2PostedFutrDepnAmt":number,
      /**  The Depreciation value in the reporting currency posted to the GL after Revaluation Date.  */  
   "Rpt3PostedFutrDepnAmt":number,
      /**  The Grant Depreciation value in the base currency posted to the GL  after Revaluation Date.  */  
   "PostedFutrGrantDepnAmt":number,
      /**  The Grant Depreciation value in the document currency posted to the GL  after Revaluation Date.  */  
   "DocPostedFutrGrantDepnAmt":number,
      /**  The Grant Depreciation value in the reporting currency posted to the GL after Revaluation Date.  */  
   "Rpt1PostedFutrGrantDepnAmt":number,
      /**  The Grant Depreciation value in the reporting currency posted to the GL after Revaluation Date.  */  
   "Rpt2PostedFutrGrantDepnAmt":number,
      /**  The Grant Depreciation value in the reporting currency posted to the GL after Revaluation Date.  */  
   "Rpt3PostedFutrGrantDepnAmt":number,
      /**  New Estimated Life  */  
   "NewAssetLife":number,
      /**  New Life Modifier. Available Values (PERIODS or YEARS)  */  
   "NewLifeModifier":string,
      /**  New Residual value of the asset in base currency. By default it is equaled current value.  */  
   "NewResidualValue":number,
      /**  New Residual value of the asset in document currency. By default it is equaled current value.  */  
   "DocNewResidualValue":number,
      /**  New Residual value of the asset in reporting currency. By default it is equaled current value.  */  
   "Rpt1NewResidualValue":number,
      /**  New Residual value of the asset in reporting currency. By default it is equaled current value.  */  
   "Rpt2NewResidualValue":number,
      /**  New Residual value of the asset in reporting currency. By default it is equaled current value.  */  
   "Rpt3NewResidualValue":number,
      /**  Revision Identifier for this row. It is incremented upon oach write.  */  
   "SysRevID":number,
      /**  Uniquue identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Value of Depreciation on Disposal/Revaluation setting of the asset, that was used to create the Revaluation.  */  
   "DepOnDisposal":number,
      /**  Accumulated depreciation in the period of revaluation.  */  
   "OrigCurrPerDepn":number,
      /**  Accumulated depreciation in the period of revaluation in document currency.  */  
   "DocOrigCurrPerDepn":number,
      /**  Accumulated depreciation in the period of revaluation in reporting currency.  */  
   "Rpt1OrigCurrPerDepn":number,
      /**  Accumulated depreciation in the period of revaluation in reporting currency.  */  
   "Rpt2OrigCurrPerDepn":number,
      /**  Accumulated depreciation in the period of revaluation in reporting currency.  */  
   "Rpt3OrigCurrPerDepn":number,
      /**  Accumulated grant depreciation in the period of revaluation.  */  
   "OrigCurrPerGrantDepn":number,
      /**  Accumulated grant depreciation in the period of revaluation in document currency.  */  
   "DocOrigCurrPerGrantDepn":number,
      /**  Accumulated grant depreciation in the period of revaluation in reporting currency.  */  
   "Rpt1OrigCurrPerGrantDepn":number,
      /**  Accumulated grant depreciation in the period of revaluation in reporting currency.  */  
   "Rpt2OrigCurrPerGrantDepn":number,
      /**  Accumulated grant depreciation in the period of revaluation in reporting currency.  */  
   "Rpt3OrigCurrPerGrantDepn":number,
   "AssetRegDescription":string,
   "CurrAssetLife":number,
   "CurrencyCode":string,
   "CurrLifeModifier":string,
   "DocResidualValue":number,
   "ResidualValue":number,
   "Rpt1ResidualValue":number,
   "Rpt2ResidualValue":number,
   "Rpt3ResidualValue":number,
   "BitFlag":number,
   "FAssetDtlRpt1ResidualValue":number,
   "FAssetDtlDocResidualValue":number,
   "FAssetDtlRpt2ResidualValue":number,
   "FAssetDtlRpt3ResidualValue":number,
   "FAssetDtlLifeModifier":string,
   "FAssetDtlAssetLife":number,
   "FAssetDtlResidualValue":number,
   "FAssetRegDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_FARevalueRow{
      /**  Company of the Addition.  */  
   "Company":string,
      /**  Asset number of the Addition.  */  
   "AssetNum":string,
      /**  Unique number to identify the Revaluation activity of an asset.  */  
   "RevalueNum":number,
      /**  Description of the Revaluation.  */  
   "Description":string,
      /**  The Impairment Date that will be used to get the exchange rate.  */  
   "ApplyDate":string,
      /**  Flag to indicat that the impairment is allowed to be posted to the GL.  */  
   "ReadyToPost":boolean,
      /**  Flag to indicate that the impairment is posted to the GL. After posting modification of the impairment is not allowed.  */  
   "Posted":boolean,
      /**  Posting date of the impairment to the GL.  */  
   "PostDate":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Unique identifier of the currency rate group.  */  
   "RateGrpCode":string,
      /**  The addition is posted by the user.  */  
   "PostedBy":string,
      /**  The GL journal to which the addition is posted.  */  
   "JournalCode":string,
      /**  The GL journal number to which the addition is posted.  */  
   "JournalNum":number,
      /**  New Book Value in base currency.  */  
   "NewBookValue":number,
      /**  New Book Value in document currency.  */  
   "DocNewBookValue":number,
      /**  New Book Value in reporting currency.  */  
   "Rpt1NewBookValue":number,
      /**  New Book Value in reporting currency.  */  
   "Rpt2NewBookValue":number,
      /**  New Book Value in reporting currency.  */  
   "Rpt3NewBookValue":number,
      /**   Revaluation Method.  Possible values are:
NETVAL - Restate Net Value
GROSSVAL - Restate Gross Value and Depreciation  */  
   "RevalueMethod":string,
      /**  Flag to indicate if Cost Limit is applied.  */  
   "CostLimitApplied":boolean,
      /**  Indicates that the transaction is reflected in FAsset costs.  */  
   "HdrCostRecorded":boolean,
      /**  List of Asset Registers in which the transaction is reflected.  */  
   "RecordedRegList":string,
      /**  Valuation Date is an invormation field , but it is default for the Apply date.  */  
   "ValuationDate":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  ChangedBy  */  
   "ChangedBy":string,
      /**  ChangeDate  */  
   "ChangeDate":string,
   "IsLocked":boolean,
      /**  Locked means can not be updated or deleted: the addition activity is already in review journal or in posting process.  */  
   "LockStatus":string,
      /**  Review Journal UID  */  
   "RvJrnUID":number,
   "BitFlag":number,
   "CurrencyCodeCurrSymbol":string,
   "CurrencyCodeCurrName":string,
   "CurrencyCodeDocumentDesc":string,
   "CurrencyCodeCurrDesc":string,
   "CurrencyCodeCurrencyID":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param assetNum
      @param applyDate
   */  
export interface CheckApplyDateInClosedPer_input{
   assetNum:string,
   applyDate:string,
}

export interface CheckApplyDateInClosedPer_output{
   returnObj:boolean,
}

   /** Required : 
      @param assetNum
      @param applyDate
   */  
export interface CheckAssetDepRecalcNeeded_input{
      /**  Asset ID  */  
   assetNum:string,
      /**  Revaluation Apply Date  */  
   applyDate:string,
}

export interface CheckAssetDepRecalcNeeded_output{
      /**  true if depreciation calculation is required  */  
   returnObj:string,
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
      /**  If transaction found: Warning message offering to clear Ready To Post flag; otherwise: null  */  
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
      @param revalueNum
   */  
export interface DeleteByID_input{
   assetNum:string,
   revalueNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_FARevalueAttchRow{
   Company:string,
   AssetNum:string,
   RevalueNum:number,
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

export interface Erp_Tablesets_FARevalueListRow{
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FARevalueListTableset{
   FARevalueList:Erp_Tablesets_FARevalueListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_FARevalueRegRow{
      /**  Company  */  
   Company:string,
      /**  Asset Number  */  
   AssetNum:string,
      /**  Unique number to identify the Revaluation activity of an asset.  */  
   RevalueNum:number,
      /**  Identifier of the Asset Register.  */  
   AssetRegID:string,
      /**  The original Current Asset Cost in base currency before running the Asset Revaluation process.  */  
   OrigCurrentCost:number,
      /**  The original Current Asset Cost in document currency before running the Asset Revaluation process.  */  
   DocOrigCurrentCost:number,
      /**  The original Current Asset Cost in reporting currency before running the Asset Revaluation process.  */  
   Rpt1OrigCurrentCost:number,
      /**  The original Current Asset Cost in reporting currency before running the Asset Revaluation process.  */  
   Rpt2OrigCurrentCost:number,
      /**  The original Current Asset Cost in reporting currency before running the Asset Revaluation process.  */  
   Rpt3OrigCurrentCost:number,
      /**  Book Value before revaluation in base currency.  */  
   OrigBookValue:number,
      /**  Book Value before revaluation in document currency.  */  
   DocOrigBookValue:number,
      /**  Book Value before revaluation in reporting currency.  */  
   Rpt1OrigBookValue:number,
      /**  Book Value before revaluation in reporting currency.  */  
   Rpt2OrigBookValue:number,
      /**  Book Value before revaluation in reporting currency.  */  
   Rpt3OrigBookValue:number,
      /**  Accumulated depreciation before revaluation (up to revaluation date) in base curreny.  */  
   OrigTotalDepn:number,
      /**  Accumulated depreciation before revaluation (up to revaluation date) in document curreny.  */  
   DocOrigTotalDepn:number,
      /**  Accumulated depreciation before revaluation (up to revaluation date) in reporting curreny.  */  
   Rpt1OrigTotalDepn:number,
      /**  Accumulated depreciation before revaluation (up to revaluation date) in reporting curreny.  */  
   Rpt2OrigTotalDepn:number,
      /**  Accumulated depreciation before revaluation (up to revaluation date) in reporting curreny.  */  
   Rpt3OrigTotalDepn:number,
      /**  Revaluation Gain or Loss in base currency. The difference between Original Book Value and New Book Value  */  
   RevalueGainLoss:number,
      /**  Revaluation Gain or Loss in document currency. The difference between Original Book Value and New Book Value  */  
   DocRevalueGainLoss:number,
      /**  Revaluation Gain or Loss in reporting currency. The difference between Original Book Value and New Book Value  */  
   Rpt1RevalueGainLoss:number,
      /**  Revaluation Gain or Loss in reporting currency. The difference between Original Book Value and New Book Value  */  
   Rpt2RevalueGainLoss:number,
      /**  Revaluation Gain or Loss in reporting currency. The difference between Original Book Value and New Book Value  */  
   Rpt3RevalueGainLoss:number,
      /**  Revaluation Surplus in base currency. Increase of the asset value that remains after reversing of previous loss (if any).  */  
   RevalueSurplus:number,
      /**  Revaluation Surplus in document currency. Increase of the asset value that remains after reversing of previous loss (if any).  */  
   DocRevalueSurplus:number,
      /**  Revaluation Surplus in reporting currency. Increase of the asset value that remains after reversing of previous loss (if any).  */  
   Rpt1RevalueSurplus:number,
      /**  Revaluation Surplus in reporting currency. Increase of the asset value that remains after reversing of previous loss (if any).  */  
   Rpt2RevalueSurplus:number,
      /**  Revaluation Surplus in reporting currency. Increase of the asset value that remains after reversing of previous loss (if any).  */  
   Rpt3RevalueSurplus:number,
      /**  The Grant Amount awarded to an asset to reduce the depreciation charge in base currency.  */  
   GrantAmt:number,
      /**  The Grant Amount awarded to an asset to reduce the depreciation charge in document currency.  */  
   DocGrantAmt:number,
      /**  The Grant Amount awarded to an asset to reduce the depreciation charge in reporting currency.  */  
   Rpt1GrantAmt:number,
      /**  The Grant Amount awarded to an asset to reduce the depreciation charge in reporting currency.  */  
   Rpt2GrantAmt:number,
      /**  The Grant Amount awarded to an asset to reduce the depreciation charge in reporting currency.  */  
   Rpt3GrantAmt:number,
      /**  The Grant Depreciation Amount awarded to an asset to reduce the depreciation charge in base currency.  */  
   GrantDepnAmt:number,
      /**  The Grant Depreciation Amount awarded to an asset to reduce the depreciation charge in document currency.  */  
   DocGrantDepnAmt:number,
      /**  The Grant Depreciation Amount awarded to an asset to reduce the depreciation charge in reporting currency.  */  
   Rpt1GrantDepnAmt:number,
      /**  The Grant Depreciation Amount awarded to an asset to reduce the depreciation charge in reporting currency.  */  
   Rpt2GrantDepnAmt:number,
      /**  The Grant Depreciation Amount awarded to an asset to reduce the depreciation charge in reporting currency.  */  
   Rpt3GrantDepnAmt:number,
      /**  Grant Book Value at the moment of revaluation in base currency.  */  
   UnusedGrantAmt:number,
      /**  Grant Book Value at the moment of revaluation in document currency.  */  
   DocUnusedGrantAmt:number,
      /**  Grant Book Value at the moment of revaluation in reporting currency.  */  
   Rpt1UnusedGrantAmt:number,
      /**  Grant Book Value at the moment of revaluation in reporting currency.  */  
   Rpt2UnusedGrantAmt:number,
      /**  Grant Book Value at the moment of revaluation in reporting currency.  */  
   Rpt3UnusedGrantAmt:number,
      /**  The Depreciation value in the base currency posted to the GL after Revaluation Date.  */  
   PostedFutrDepnAmt:number,
      /**  The Depreciation value in the documnet currency posted to the GL after Revaluation Date.  */  
   DocPostedFutrDepnAmt:number,
      /**  The Depreciation value in the reporting currency posted to the GL after Revaluation Date.  */  
   Rpt1PostedFutrDepnAmt:number,
      /**  The Depreciation value in the reporting currency posted to the GL after Revaluation Date.  */  
   Rpt2PostedFutrDepnAmt:number,
      /**  The Depreciation value in the reporting currency posted to the GL after Revaluation Date.  */  
   Rpt3PostedFutrDepnAmt:number,
      /**  The Grant Depreciation value in the base currency posted to the GL  after Revaluation Date.  */  
   PostedFutrGrantDepnAmt:number,
      /**  The Grant Depreciation value in the document currency posted to the GL  after Revaluation Date.  */  
   DocPostedFutrGrantDepnAmt:number,
      /**  The Grant Depreciation value in the reporting currency posted to the GL after Revaluation Date.  */  
   Rpt1PostedFutrGrantDepnAmt:number,
      /**  The Grant Depreciation value in the reporting currency posted to the GL after Revaluation Date.  */  
   Rpt2PostedFutrGrantDepnAmt:number,
      /**  The Grant Depreciation value in the reporting currency posted to the GL after Revaluation Date.  */  
   Rpt3PostedFutrGrantDepnAmt:number,
      /**  New Estimated Life  */  
   NewAssetLife:number,
      /**  New Life Modifier. Available Values (PERIODS or YEARS)  */  
   NewLifeModifier:string,
      /**  New Residual value of the asset in base currency. By default it is equaled current value.  */  
   NewResidualValue:number,
      /**  New Residual value of the asset in document currency. By default it is equaled current value.  */  
   DocNewResidualValue:number,
      /**  New Residual value of the asset in reporting currency. By default it is equaled current value.  */  
   Rpt1NewResidualValue:number,
      /**  New Residual value of the asset in reporting currency. By default it is equaled current value.  */  
   Rpt2NewResidualValue:number,
      /**  New Residual value of the asset in reporting currency. By default it is equaled current value.  */  
   Rpt3NewResidualValue:number,
      /**  Revision Identifier for this row. It is incremented upon oach write.  */  
   SysRevID:number,
      /**  Uniquue identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Value of Depreciation on Disposal/Revaluation setting of the asset, that was used to create the Revaluation.  */  
   DepOnDisposal:number,
      /**  Accumulated depreciation in the period of revaluation.  */  
   OrigCurrPerDepn:number,
      /**  Accumulated depreciation in the period of revaluation in document currency.  */  
   DocOrigCurrPerDepn:number,
      /**  Accumulated depreciation in the period of revaluation in reporting currency.  */  
   Rpt1OrigCurrPerDepn:number,
      /**  Accumulated depreciation in the period of revaluation in reporting currency.  */  
   Rpt2OrigCurrPerDepn:number,
      /**  Accumulated depreciation in the period of revaluation in reporting currency.  */  
   Rpt3OrigCurrPerDepn:number,
      /**  Accumulated grant depreciation in the period of revaluation.  */  
   OrigCurrPerGrantDepn:number,
      /**  Accumulated grant depreciation in the period of revaluation in document currency.  */  
   DocOrigCurrPerGrantDepn:number,
      /**  Accumulated grant depreciation in the period of revaluation in reporting currency.  */  
   Rpt1OrigCurrPerGrantDepn:number,
      /**  Accumulated grant depreciation in the period of revaluation in reporting currency.  */  
   Rpt2OrigCurrPerGrantDepn:number,
      /**  Accumulated grant depreciation in the period of revaluation in reporting currency.  */  
   Rpt3OrigCurrPerGrantDepn:number,
   AssetRegDescription:string,
   CurrAssetLife:number,
   CurrencyCode:string,
   CurrLifeModifier:string,
   DocResidualValue:number,
   ResidualValue:number,
   Rpt1ResidualValue:number,
   Rpt2ResidualValue:number,
   Rpt3ResidualValue:number,
   BitFlag:number,
   FAssetDtlRpt1ResidualValue:number,
   FAssetDtlDocResidualValue:number,
   FAssetDtlRpt2ResidualValue:number,
   FAssetDtlRpt3ResidualValue:number,
   FAssetDtlLifeModifier:string,
   FAssetDtlAssetLife:number,
   FAssetDtlResidualValue:number,
   FAssetRegDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FARevalueRow{
      /**  Company of the Addition.  */  
   Company:string,
      /**  Asset number of the Addition.  */  
   AssetNum:string,
      /**  Unique number to identify the Revaluation activity of an asset.  */  
   RevalueNum:number,
      /**  Description of the Revaluation.  */  
   Description:string,
      /**  The Impairment Date that will be used to get the exchange rate.  */  
   ApplyDate:string,
      /**  Flag to indicat that the impairment is allowed to be posted to the GL.  */  
   ReadyToPost:boolean,
      /**  Flag to indicate that the impairment is posted to the GL. After posting modification of the impairment is not allowed.  */  
   Posted:boolean,
      /**  Posting date of the impairment to the GL.  */  
   PostDate:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Unique identifier of the currency rate group.  */  
   RateGrpCode:string,
      /**  The addition is posted by the user.  */  
   PostedBy:string,
      /**  The GL journal to which the addition is posted.  */  
   JournalCode:string,
      /**  The GL journal number to which the addition is posted.  */  
   JournalNum:number,
      /**  New Book Value in base currency.  */  
   NewBookValue:number,
      /**  New Book Value in document currency.  */  
   DocNewBookValue:number,
      /**  New Book Value in reporting currency.  */  
   Rpt1NewBookValue:number,
      /**  New Book Value in reporting currency.  */  
   Rpt2NewBookValue:number,
      /**  New Book Value in reporting currency.  */  
   Rpt3NewBookValue:number,
      /**   Revaluation Method.  Possible values are:
NETVAL - Restate Net Value
GROSSVAL - Restate Gross Value and Depreciation  */  
   RevalueMethod:string,
      /**  Flag to indicate if Cost Limit is applied.  */  
   CostLimitApplied:boolean,
      /**  Indicates that the transaction is reflected in FAsset costs.  */  
   HdrCostRecorded:boolean,
      /**  List of Asset Registers in which the transaction is reflected.  */  
   RecordedRegList:string,
      /**  Valuation Date is an invormation field , but it is default for the Apply date.  */  
   ValuationDate:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  ChangeDate  */  
   ChangeDate:string,
   IsLocked:boolean,
      /**  Locked means can not be updated or deleted: the addition activity is already in review journal or in posting process.  */  
   LockStatus:string,
      /**  Review Journal UID  */  
   RvJrnUID:number,
   BitFlag:number,
   CurrencyCodeCurrSymbol:string,
   CurrencyCodeCurrName:string,
   CurrencyCodeDocumentDesc:string,
   CurrencyCodeCurrDesc:string,
   CurrencyCodeCurrencyID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FARevalueTableset{
   FARevalue:Erp_Tablesets_FARevalueRow[],
   FARevalueAttch:Erp_Tablesets_FARevalueAttchRow[],
   FARevalueReg:Erp_Tablesets_FARevalueRegRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtFARevalueTableset{
   FARevalue:Erp_Tablesets_FARevalueRow[],
   FARevalueAttch:Erp_Tablesets_FARevalueAttchRow[],
   FARevalueReg:Erp_Tablesets_FARevalueRegRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ds
   */  
export interface GetAvailableApplyDate_input{
   ds:Erp_Tablesets_FARevalueTableset[],
}

export interface GetAvailableApplyDate_output{
   returnObj:string,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FARevalueTableset[],
}
}

   /** Required : 
      @param assetNum
      @param revalueNum
   */  
export interface GetByID_input{
   assetNum:string,
   revalueNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_FARevalueTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_FARevalueTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_FARevalueTableset[],
}

   /** Required : 
      @param assetNum
      @param valuationDate
      @param applyDate
   */  
export interface GetDefaultDates_input{
   assetNum:string,
   valuationDate:string,
   applyDate:string,
}

export interface GetDefaultDates_output{
parameters : {
      /**  output parameters  */  
   valuationDate:string,
   applyDate:string,
}
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
   returnObj:Erp_Tablesets_FARevalueListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param assetNum
      @param revalueNum
   */  
export interface GetNewFARevalueAttch_input{
   ds:Erp_Tablesets_FARevalueTableset[],
   assetNum:string,
   revalueNum:number,
}

export interface GetNewFARevalueAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FARevalueTableset[],
}
}

   /** Required : 
      @param ds
      @param assetNum
      @param revalueNum
   */  
export interface GetNewFARevalueReg_input{
   ds:Erp_Tablesets_FARevalueTableset[],
   assetNum:string,
   revalueNum:number,
}

export interface GetNewFARevalueReg_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FARevalueTableset[],
}
}

   /** Required : 
      @param ds
      @param assetNum
   */  
export interface GetNewFARevalue_input{
   ds:Erp_Tablesets_FARevalueTableset[],
   assetNum:string,
}

export interface GetNewFARevalue_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FARevalueTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewRegistersInfo_input{
   ds:Erp_Tablesets_FARevalueTableset[],
}

export interface GetNewRegistersInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FARevalueTableset[],
   warning:string,
}
}

   /** Required : 
      @param assetNum
      @param valuationDate
      @param applyDate
      @param ds
   */  
export interface GetNewRevaluation_input{
      /**  Asset Number  */  
   assetNum:string,
      /**  Valuation Date  */  
   valuationDate:string,
      /**  Apply Date  */  
   applyDate:string,
   ds:Erp_Tablesets_FARevalueTableset[],
}

export interface GetNewRevaluation_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FARevalueTableset[],
}
}

   /** Required : 
      @param assetNum
      @param ds
   */  
export interface GetRevaluationsWithRecalc_input{
   assetNum:string,
   ds:Erp_Tablesets_FARevalueTableset[],
}

export interface GetRevaluationsWithRecalc_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FARevalueTableset[],
}
}

   /** Required : 
      @param whereClauseFARevalue
      @param whereClauseFARevalueAttch
      @param whereClauseFARevalueReg
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseFARevalue:string,
   whereClauseFARevalueAttch:string,
   whereClauseFARevalueReg:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_FARevalueTableset[],
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
      @param applyDate
      @param ds
   */  
export interface OnChangeApplyDate_input{
   applyDate:string,
   ds:Erp_Tablesets_FARevalueTableset[],
}

export interface OnChangeApplyDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FARevalueTableset[],
   warning:string,
}
}

   /** Required : 
      @param newBookValue
      @param ds
   */  
export interface OnChangeNewBookValue_input{
      /**  new Book value  */  
   newBookValue:number,
   ds:Erp_Tablesets_FARevalueTableset[],
}

export interface OnChangeNewBookValue_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FARevalueTableset[],
}
}

   /** Required : 
      @param newResidualValue
      @param ds
   */  
export interface OnChangeNewResidualValue_input{
      /**  new Residual Value  */  
   newResidualValue:number,
   ds:Erp_Tablesets_FARevalueTableset[],
}

export interface OnChangeNewResidualValue_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FARevalueTableset[],
}
}

   /** Required : 
      @param readyToPost
      @param ds
   */  
export interface OnChangeReadyToPost_input{
   readyToPost:boolean,
   ds:Erp_Tablesets_FARevalueTableset[],
}

export interface OnChangeReadyToPost_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FARevalueTableset[],
   warning:string,
}
}

   /** Required : 
      @param valuationDate
      @param ds
   */  
export interface OnChangeValuationDate_input{
   valuationDate:string,
   ds:Erp_Tablesets_FARevalueTableset[],
}

export interface OnChangeValuationDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FARevalueTableset[],
   warning:string,
}
}

   /** Required : 
      @param warnMsg
   */  
export interface ParseDateValidationMessage_input{
   warnMsg:string,
}

export interface ParseDateValidationMessage_output{
parameters : {
      /**  output parameters  */  
   opDialogInfo1:string,
   opDialogInfo2:string,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtFARevalueTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtFARevalueTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_FARevalueTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FARevalueTableset[],
}
}

