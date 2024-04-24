import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.AssetDispEntrySvc
// Description: FA disposal entry
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/$metadata", {
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
   Description: Get AssetDispEntries items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AssetDispEntries
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FADisposalRow
   */  
export function get_AssetDispEntries(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FADisposalRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/AssetDispEntries", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FADisposalRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AssetDispEntries
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FADisposalRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FADisposalRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AssetDispEntries(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/AssetDispEntries", {
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
   Summary: Calls GetByID to retrieve the AssetDispEntry item
   Description: Calls GetByID to retrieve the AssetDispEntry item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AssetDispEntry
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param DisposalNum Desc: DisposalNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FADisposalRow
   */  
export function get_AssetDispEntries_Company_AssetNum_DisposalNum(Company:string, AssetNum:string, DisposalNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FADisposalRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/AssetDispEntries(" + Company + "," + AssetNum + "," + DisposalNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FADisposalRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update AssetDispEntry for the service
   Description: Calls UpdateExt to update AssetDispEntry. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AssetDispEntry
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param DisposalNum Desc: DisposalNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FADisposalRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_AssetDispEntries_Company_AssetNum_DisposalNum(Company:string, AssetNum:string, DisposalNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/AssetDispEntries(" + Company + "," + AssetNum + "," + DisposalNum + ")", {
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
   Summary: Call UpdateExt to delete AssetDispEntry item
   Description: Call UpdateExt to delete AssetDispEntry item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AssetDispEntry
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param DisposalNum Desc: DisposalNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_AssetDispEntries_Company_AssetNum_DisposalNum(Company:string, AssetNum:string, DisposalNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/AssetDispEntries(" + Company + "," + AssetNum + "," + DisposalNum + ")", {
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
   Description: Get FADispRegs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FADispRegs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param DisposalNum Desc: DisposalNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FADispRegRow
   */  
export function get_AssetDispEntries_Company_AssetNum_DisposalNum_FADispRegs(Company:string, AssetNum:string, DisposalNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FADispRegRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/AssetDispEntries(" + Company + "," + AssetNum + "," + DisposalNum + ")/FADispRegs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FADispRegRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the FADispReg item
   Description: Calls GetByID to retrieve the FADispReg item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FADispReg1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param DisposalNum Desc: DisposalNum   Required: True
      @param AssetRegID Desc: AssetRegID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FADispRegRow
   */  
export function get_AssetDispEntries_Company_AssetNum_DisposalNum_FADispRegs_Company_AssetNum_DisposalNum_AssetRegID(Company:string, AssetNum:string, DisposalNum:string, AssetRegID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FADispRegRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/AssetDispEntries(" + Company + "," + AssetNum + "," + DisposalNum + ")/FADispRegs(" + Company + "," + AssetNum + "," + DisposalNum + "," + AssetRegID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FADispRegRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get FADisposalAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FADisposalAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param DisposalNum Desc: DisposalNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FADisposalAttchRow
   */  
export function get_AssetDispEntries_Company_AssetNum_DisposalNum_FADisposalAttches(Company:string, AssetNum:string, DisposalNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FADisposalAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/AssetDispEntries(" + Company + "," + AssetNum + "," + DisposalNum + ")/FADisposalAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FADisposalAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the FADisposalAttch item
   Description: Calls GetByID to retrieve the FADisposalAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FADisposalAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param DisposalNum Desc: DisposalNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FADisposalAttchRow
   */  
export function get_AssetDispEntries_Company_AssetNum_DisposalNum_FADisposalAttches_Company_AssetNum_DisposalNum_DrawingSeq(Company:string, AssetNum:string, DisposalNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FADisposalAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/AssetDispEntries(" + Company + "," + AssetNum + "," + DisposalNum + ")/FADisposalAttches(" + Company + "," + AssetNum + "," + DisposalNum + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FADisposalAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get FADispRegs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FADispRegs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FADispRegRow
   */  
export function get_FADispRegs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FADispRegRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/FADispRegs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FADispRegRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FADispRegs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FADispRegRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FADispRegRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FADispRegs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/FADispRegs", {
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
   Summary: Calls GetByID to retrieve the FADispReg item
   Description: Calls GetByID to retrieve the FADispReg item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FADispReg
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param DisposalNum Desc: DisposalNum   Required: True
      @param AssetRegID Desc: AssetRegID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FADispRegRow
   */  
export function get_FADispRegs_Company_AssetNum_DisposalNum_AssetRegID(Company:string, AssetNum:string, DisposalNum:string, AssetRegID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FADispRegRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/FADispRegs(" + Company + "," + AssetNum + "," + DisposalNum + "," + AssetRegID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FADispRegRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update FADispReg for the service
   Description: Calls UpdateExt to update FADispReg. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FADispReg
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param DisposalNum Desc: DisposalNum   Required: True
      @param AssetRegID Desc: AssetRegID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FADispRegRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_FADispRegs_Company_AssetNum_DisposalNum_AssetRegID(Company:string, AssetNum:string, DisposalNum:string, AssetRegID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/FADispRegs(" + Company + "," + AssetNum + "," + DisposalNum + "," + AssetRegID + ")", {
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
   Summary: Call UpdateExt to delete FADispReg item
   Description: Call UpdateExt to delete FADispReg item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FADispReg
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param DisposalNum Desc: DisposalNum   Required: True
      @param AssetRegID Desc: AssetRegID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_FADispRegs_Company_AssetNum_DisposalNum_AssetRegID(Company:string, AssetNum:string, DisposalNum:string, AssetRegID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/FADispRegs(" + Company + "," + AssetNum + "," + DisposalNum + "," + AssetRegID + ")", {
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
   Description: Get FADisposalAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FADisposalAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FADisposalAttchRow
   */  
export function get_FADisposalAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FADisposalAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/FADisposalAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FADisposalAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FADisposalAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FADisposalAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FADisposalAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FADisposalAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/FADisposalAttches", {
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
   Summary: Calls GetByID to retrieve the FADisposalAttch item
   Description: Calls GetByID to retrieve the FADisposalAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FADisposalAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param DisposalNum Desc: DisposalNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FADisposalAttchRow
   */  
export function get_FADisposalAttches_Company_AssetNum_DisposalNum_DrawingSeq(Company:string, AssetNum:string, DisposalNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FADisposalAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/FADisposalAttches(" + Company + "," + AssetNum + "," + DisposalNum + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FADisposalAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update FADisposalAttch for the service
   Description: Calls UpdateExt to update FADisposalAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FADisposalAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param DisposalNum Desc: DisposalNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FADisposalAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_FADisposalAttches_Company_AssetNum_DisposalNum_DrawingSeq(Company:string, AssetNum:string, DisposalNum:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/FADisposalAttches(" + Company + "," + AssetNum + "," + DisposalNum + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete FADisposalAttch item
   Description: Call UpdateExt to delete FADisposalAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FADisposalAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param DisposalNum Desc: DisposalNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_FADisposalAttches_Company_AssetNum_DisposalNum_DrawingSeq(Company:string, AssetNum:string, DisposalNum:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/FADisposalAttches(" + Company + "," + AssetNum + "," + DisposalNum + "," + DrawingSeq + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/SelectedSerialNumbers", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/SelectedSerialNumbers", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/SNFormats", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/SNFormats", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FADisposalListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FADisposalListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FADisposalListRow)
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
export function get_GetRows(whereClauseFADisposal:string, whereClauseFADisposalAttch:string, whereClauseFADispReg:string, whereClauseSelectedSerialNumbers:string, whereClauseSNFormat:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseFADisposal!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseFADisposal=" + whereClauseFADisposal
   }
   if(typeof whereClauseFADisposalAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseFADisposalAttch=" + whereClauseFADisposalAttch
   }
   if(typeof whereClauseFADispReg!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseFADispReg=" + whereClauseFADispReg
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/GetRows" + params, {
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
export function get_GetByID(assetNum:string, disposalNum:string, epicorHeaders?:Headers){
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
   if(typeof disposalNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "disposalNum=" + disposalNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/GetList" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/CheckAssetTransactions", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/ClearReadyToPost", {
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
   Summary: Invoke method CheckDeprCalculated
   Description: Checks whether depreciation schedule was calculated for Fiscal Period of Disposal date
   OperationID: CheckDeprCalculated
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckDeprCalculated_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDeprCalculated_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckDeprCalculated(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/CheckDeprCalculated", {
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
   Summary: Invoke method LeaveCustID
   Description: To be called on leave of custid field
   OperationID: LeaveCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LeaveCustID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/LeaveCustID", {
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
   Summary: Invoke method LeaveDisposalCost
   Description: To be called on leave of DisposalCost field
   OperationID: LeaveDisposalCost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveDisposalCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveDisposalCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LeaveDisposalCost(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/LeaveDisposalCost", {
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
   Summary: Invoke method LeaveDisposalType
   Description: To be called on leave of DisposalType field
   OperationID: LeaveDisposalType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveDisposalType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveDisposalType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LeaveDisposalType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/LeaveDisposalType", {
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
   Summary: Invoke method LeaveDisposed
   Description: To be called on leave of Disposed field
   OperationID: LeaveDisposed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveDisposed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveDisposed_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LeaveDisposed(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/LeaveDisposed", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/LeaveJobNum", {
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
   Summary: Invoke method LeaveOrderNum
   Description: To be called on leave of ordernum field
   OperationID: LeaveOrderNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveOrderNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveOrderNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LeaveOrderNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/LeaveOrderNum", {
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
   Description: To be called on leave of partnum field
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/LeavePartNum", {
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
   Summary: Invoke method LeaveProceed
   Description: To be called on leave of Proceed field
   OperationID: LeaveProceed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveProceed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveProceed_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LeaveProceed(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/LeaveProceed", {
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
   Summary: Invoke method LeaveWarehouseCode
   Description: To be called on leave of WarehouseCode field
   OperationID: LeaveWarehouseCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveWarehouseCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveWarehouseCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LeaveWarehouseCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/LeaveWarehouseCode", {
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
   Summary: Invoke method LeaveBinNum
   Description: To be called on leave of Bin field
   OperationID: LeaveBinNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveBinNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveBinNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LeaveBinNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/LeaveBinNum", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/CheckAssetDepRecalcNeeded", {
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
   Summary: Invoke method OnSetReadyToPost
   Description: To be called on leave of ReadyToPost field with value 'true'
   OperationID: OnSetReadyToPost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnSetReadyToPost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnSetReadyToPost_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnSetReadyToPost(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/OnSetReadyToPost", {
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
<param name="ds">Asset Disposal DataSet</param><returns>The SelectSerialNumbersParams dataset</returns>
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/GetSelectSerialNumbersParams", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/ValidateSN", {
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
   Description: This method will retrieve the serial numbers for FAdisposal record and
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/GetSelectedSerialNumbers", {
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
   Summary: Invoke method GetNewFADisposal
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFADisposal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFADisposal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFADisposal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewFADisposal(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/GetNewFADisposal", {
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
   Summary: Invoke method GetNewFADisposalAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFADisposalAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFADisposalAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFADisposalAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewFADisposalAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/GetNewFADisposalAttch", {
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
   Summary: Invoke method GetNewFADispReg
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFADispReg
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFADispReg_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFADispReg_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewFADispReg(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/GetNewFADispReg", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetDispEntrySvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FADispRegRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FADispRegRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FADisposalAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FADisposalAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FADisposalListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FADisposalListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FADisposalRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FADisposalRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SNFormatRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SNFormatRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SelectedSerialNumbersRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SelectedSerialNumbersRow[],
}

export interface Erp_Tablesets_FADispRegRow{
      /**  Company of the Disposal.  */  
   "Company":string,
      /**  Asset number of the Disposal.  */  
   "AssetNum":string,
      /**  Unique number to identify the Disposal of an asset.  */  
   "DisposalNum":number,
      /**  Identifier of the Asset Register.  */  
   "AssetRegID":string,
      /**  The depreciation amount that is substracted from the Asset depreciation cost account for the posted depreciations of previous years.  */  
   "PrevDepreciation":number,
      /**  The depreciation amount that is substracted from the Asset depreciation cost account for the posted depreciations of current year.  */  
   "CurrDepreciation":number,
      /**  The Book Value of a disposal is calculated as the disposal cost minus disposal depreciation minus disposal current year depreciation.  */  
   "BookValue":number,
      /**  The depreciation amount that is substracted from the Asset depreciation cost account for the posted depreciations of previous years in the specified currency.  */  
   "DocPrevDepreciation":number,
      /**  The depreciation already applied to this addition in another system within the same holding company for this year in the specified currency.  */  
   "DocCurrDepreciation":number,
      /**  This is the Book Value of a disposal in the specified currency.  */  
   "DocBookValue":number,
      /**  Reporting currency of the previous years disposal depreciation.  */  
   "Rpt1PrevDepreciation":number,
      /**  Reporting currency value of the current year disposal depreciation.  */  
   "Rpt1CurrDepreciation":number,
      /**  Reporting currency value of the disposal book value.  */  
   "Rpt1BookValue":number,
      /**  Reporting currency value of the previous years disposal depreciation.  */  
   "Rpt2PrevDepreciation":number,
      /**  Reporting currency value of the current year disposal depreciation.  */  
   "Rpt2CurrDepreciation":number,
      /**  Reporting currency value of the disposal book value.  */  
   "Rpt2BookValue":number,
      /**  Reporting currency value of the previous years disposal depreciation.  */  
   "Rpt3PrevDepreciation":number,
      /**  Reporting currency value of the current year disposal depreciation.  */  
   "Rpt3CurrDepreciation":number,
      /**  Reporting currency value of the disposal book value.  */  
   "Rpt3BookValue":number,
      /**  Grant Book Value of the disposal is a calculated field. It is Grant Amount minus previous years disposal Grant Depreciation minus current year disposal Grant Depreciation.  */  
   "GrantBookValue":number,
      /**  The disposed portion of the total Grant Depreciation already posted for previous years.  */  
   "PrevGrantDep":number,
      /**  The disposed portion of the total Grant Depreciation already posted for the current year.  */  
   "CurrGrantDep":number,
      /**  Grant Book Value of the disposal is a calculated field. It is Grant Amount minus previous years disposal Grant Depreciation minus current year disposal Grant Depreciation.  */  
   "DocGrantBookValue":number,
      /**  The disposed portion of the total Grant Depreciation already posted for previous years.  */  
   "DocPrevGrantDep":number,
      /**  The disposed portion of the total Grant Depreciation already posted for the current year.  */  
   "DocCurrGrantDep":number,
      /**  Grant Book Value of the disposal is a calculated field. It is Grant Amount minus previous years disposal Grant Depreciation minus current year disposal Grant Depreciation.  */  
   "Rpt1GrantBookValue":number,
      /**  The disposed portion of the total Grant Depreciation already posted for previous years.  */  
   "Rpt1PrevGrantDep":number,
      /**  The disposed portion of the total Grant Depreciation already posted for the current year.  */  
   "Rpt1CurrGrantDep":number,
      /**  Grant Book Value of the disposal is a calculated field. It is Grant Amount minus previous years disposal Grant Depreciation minus current year disposal Grant Depreciation.  */  
   "Rpt2GrantBookValue":number,
      /**  The disposed portion of the total Grant Depreciation already posted for previous years.  */  
   "Rpt2PrevGrantDep":number,
      /**  The disposed portion of the total Grant Depreciation already posted for the current year.  */  
   "Rpt2CurrGrantDep":number,
      /**  Grant Book Value of the disposal is a calculated field. It is Grant Amount minus previous years disposal Grant Depreciation minus current year disposal Grant Depreciation.  */  
   "Rpt3GrantBookValue":number,
      /**  The disposed portion of the total Grant Depreciation already posted for previous years.  */  
   "Rpt3PrevGrantDep":number,
      /**  The disposed portion of the total Grant Depreciation already posted for the current year.  */  
   "Rpt3CurrGrantDep":number,
      /**  The Grant Amount awarded to an asset to reduce the depreciation charge.  */  
   "GrantAmt":number,
      /**  The Grant Amount awarded to an asset to reduce the depreciation charge in the currency specified.  */  
   "DocGrantAmt":number,
      /**  Reporting currency value of the Grant Amount.  */  
   "Rpt1GrantAmt":number,
      /**  Reporting currency value of the Grant Amount.  */  
   "Rpt2GrantAmt":number,
      /**  Reporting currency value of the Grant Amount.  */  
   "Rpt3GrantAmt":number,
      /**  The cost disposed from the asset.  */  
   "DisposalCost":number,
      /**  The cost disposed from the asset in the currency specified.  */  
   "DocDisposalCost":number,
      /**  Reporting currency value of the cost disposed from the asset.  */  
   "Rpt1DisposalCost":number,
      /**  Reporting currency value of the cost disposed from the asset.  */  
   "Rpt2DisposalCost":number,
      /**  Reporting currency value of the cost disposed from the asset.  */  
   "Rpt3DisposalCost":number,
      /**  The sales amount of the disposal.  */  
   "Proceed":number,
      /**  The sales amount of the disposal in the currency specified.  */  
   "DocProceed":number,
      /**  Reporting currency value of the proceed cost from the asset.  */  
   "Rpt1Proceed":number,
      /**  Reporting currency value of the proceed cost from the asset.  */  
   "Rpt2Proceed":number,
      /**  Reporting currency value of the proceed cost from the asset.  */  
   "Rpt3Proceed":number,
      /**  This is the current disposal proceed balance (in document currency) left to be consumed in the AR Invoice interface process.  An asset disposal can be linked to one or more AR Invoice lines and each asset disposal linking to this invoice line will reduce the balance of this DocProceedInvBal.  When this field reaches zero then this disposal line cannot be linked in the AR Invoice interface anymore.  */  
   "DocProceedInvBal":number,
      /**  This is the number of Asset Units left to be consumed in the AR Invoice Interface process.  An asset disposal can be linked to one or more invoice lines and each asset disposal linking to this invoice line will reduce the balance qty of this AssetBalOurQty.  When this field reaches zero then this disposal cannot be linked in the AR Invoice interface anymore.  This qty is expressed in our unit of measure.  */  
   "AssetBalOurQty":number,
      /**  Unit of Measure code for asset invoiced quantity balance in our unit of measure.  */  
   "AssetQtyIUM":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Value of Depreciation on disposal setting of the asset, that was used to create the disposal.  */  
   "DepOnDisposal":number,
   "CurrCode":string,
   "RateGrpCode":string,
      /**  Disposal Profit/Loss in base currency. Calculated field.  */  
   "DisposalProfitLoss":number,
      /**  Disposal Profit/Loss in document currency. Calculated field.  */  
   "DocDisposalProfitLoss":number,
      /**  Disposal Profit/Loss in Rpt1 currency. Calculated field.  */  
   "Rpt1DisposalProfitLoss":number,
      /**  Disposal Profit/Loss in Rpt2 currency. Calculated field.  */  
   "Rpt2DisposalProfitLoss":number,
      /**  Disposal Profit/Loss in Rpt3 currency. Calculated field.  */  
   "Rpt3DisposalProfitLoss":number,
   "BitFlag":number,
   "FAssetRegDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_FADisposalAttchRow{
   "Company":string,
   "AssetNum":string,
   "DisposalNum":number,
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

export interface Erp_Tablesets_FADisposalListRow{
      /**  Company of the Disposal.  */  
   "Company":string,
      /**  Asset number of the Disposal.  */  
   "AssetNum":string,
      /**  Unique number to identify the Disposal of an asset.  */  
   "DisposalNum":number,
      /**  The date of Disposal.  */  
   "Disposed":string,
      /**  The cost disposed from the asset.  */  
   "DisposalCost":number,
      /**  Description of the disposal.  */  
   "Description":string,
      /**  Invoice number of the customer.  */  
   "InvoiceNum":number,
      /**  Internal customer number.  */  
   "CustNum":number,
      /**  The invoice line of the customer invoice.  */  
   "InvoiceLine":number,
      /**  The orignal manufacturer of the disposal.  */  
   "Manufacturer":string,
      /**  The model number of the disposal.  */  
   "Model":string,
      /**  The serial number of the disposal.  */  
   "Serialno":string,
      /**  Flag to indicate that the disposal is posted to the gL.  */  
   "Posted":boolean,
      /**  The post date of the posting to the GL.  */  
   "PostDate":string,
      /**  The user that posted the disposal to the GL.  */  
   "PostedBy":string,
      /**  The GL journal to which the disposal is posted.  */  
   "JournalCode":string,
      /**  The journal number to which the disposal is posted.  */  
   "JournalNum":number,
      /**  The fiscal year in which the disposal is posted.  */  
   "FiscalYear":number,
      /**  The fiscal period in which the disposal is posted.  */  
   "FiscalPeriod":number,
      /**  The name of the customer that bought the disposal. The customer name can be entered even when no customer is selected.  */  
   "CustName":string,
      /**  The sales order that is used to sell the disposal.  */  
   "OrderNum":number,
      /**  The job that built the disposal.  */  
   "JobNum":string,
      /**  flag to indicate that the disposal is allowed to be posted.  */  
   "ReadyToPost":boolean,
      /**  The sales amount of the disposal.  */  
   "Proceed":number,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  The warehouse where the disposal came from. This is for information purposes only. In the warehouse tracker no assets can be tracked.  */  
   "WarehouseCode":string,
      /**  The bin where the disposal came from. This is for information purposes only. In the bin tracker no assets can be tracked.  */  
   "BinNum":string,
      /**  Indicates the type of asset disposal activity.  Valid values are: "SALE", "TRANSFER" or "MISC".  */  
   "DisposalType":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Unique identifier of the currency rate group.  */  
   "RateGrpCode":string,
      /**  Identifies the part number transferred from asset to stock.  This field is only required if the Disposal Type is "Transfer".  */  
   "PartNum":string,
      /**  Transferred Quantity reported for this disposal transfer.  */  
   "TransferQty":number,
      /**  Unit of Measure for the transferred quantity.  */  
   "TransferUOM":string,
      /**  Lot Number of the transferred part.  */  
   "LotNum":string,
      /**  Description of the transferred asset to stock.  */  
   "PartDescription":string,
      /**  The cost disposed from the asset in the currency specified.  */  
   "DocDisposalCost":number,
      /**  Reporting currency value of the cost disposed from the asset.  */  
   "Rpt1DisposalCost":number,
      /**  Reporting currency value of the cost disposed from the asset.  */  
   "Rpt2DisposalCost":number,
      /**  Reporting currency value of the cost disposed from the asset.  */  
   "Rpt3DisposalCost":number,
      /**  The sales amount of the disposal in the currency specified.  */  
   "DocProceed":number,
      /**  Reporting currency value of the proceed cost from the asset.  */  
   "Rpt1Proceed":number,
      /**  Reporting currency value of the proceed cost from the asset.  */  
   "Rpt2Proceed":number,
      /**  Reporting currency value of the proceed cost from the asset.  */  
   "Rpt3Proceed":number,
      /**  Location ID.  */  
   "LocID":string,
      /**  Descriptive code to uniquely identify the Equipment.  */  
   "EquipID":string,
      /**  Brand of equipment  */  
   "Brand":string,
      /**  This is the equivalent number of units for the transferred qty for this asset disposal.  There is no unit of measure conversion involved during update of this field.  The user is responsible for the "conversion" of transferred qty to asset units.  */  
   "TransferUnits":number,
      /**  This is the current disposal proceed balance (in document currency) left to be consumed in the AR Invoice interface process.  An asset disposal can be linked to one or more AR Invoice lines and each asset disposal linking to this invoice line will reduce the balance of this DocProceedInvBal.  When this field reaches zero then this disposal line cannot be linked in the AR Invoice interface anymore.  */  
   "DocProceedInvBal":number,
      /**  This is the number of Asset Units left to be consumed in the AR Invoice Interface process.  An asset disposal can be linked to one or more invoice lines and each asset disposal linking to this invoice line will reduce the balance qty of this AssetBalOurQty.  When this field reaches zero then this disposal cannot be linked in the AR Invoice interface anymore.  This qty is expressed in our unit of measure.  */  
   "AssetBalOurQty":number,
      /**  Unit of Measure code for asset invoiced quantity balance in our unit of measure.  */  
   "AssetQtyIUM":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "CustID":string,
   "PartLotTracked":boolean,
      /**  shows if is this addition transaction is blocked in RvLock.  */  
   "IsLcked":boolean,
      /**  Locked means can not be updated or deleted: the addition activity is already in review journal or in posting process.  */  
   "LockStatus":string,
      /**  Review Journal UID  */  
   "RvnJrnUID":number,
      /**  Description of the currency  */  
   "BaseCurrCurrDesc":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "BaseCurrCurrName":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "BaseCurrCurrencyID":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "BaseCurrCurrSymbol":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "BaseCurrDocumentDesc":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "CurrencyCurrName":string,
      /**  Description of the currency  */  
   "CurrencyCurrDesc":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "CurrencyDocumentDesc":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "CurrencyCurrencyID":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "CurrencyCurrSymbol":string,
      /**  Long Description of a unit of measure. Mandatory.  */  
   "UOMUOMDesc":string,
      /**  Description.  */  
   "WhseDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_FADisposalRow{
      /**  Company of the Disposal.  */  
   "Company":string,
      /**  Asset number of the Disposal.  */  
   "AssetNum":string,
      /**  Unique number to identify the Disposal of an asset.  */  
   "DisposalNum":number,
      /**  The date of Disposal.  */  
   "Disposed":string,
      /**  The cost disposed from the asset.  */  
   "DisposalCost":number,
      /**  Description of the disposal.  */  
   "Description":string,
      /**  Invoice number of the customer.  */  
   "InvoiceNum":number,
      /**  Internal customer number.  */  
   "CustNum":number,
      /**  The invoice line of the customer invoice.  */  
   "InvoiceLine":number,
      /**  The orignal manufacturer of the disposal.  */  
   "Manufacturer":string,
      /**  The model number of the disposal.  */  
   "Model":string,
      /**  The serial number of the disposal.  */  
   "Serialno":string,
      /**  Flag to indicate that the disposal is posted to the gL.  */  
   "Posted":boolean,
      /**  The post date of the posting to the GL.  */  
   "PostDate":string,
      /**  The user that posted the disposal to the GL.  */  
   "PostedBy":string,
      /**  The GL journal to which the disposal is posted.  */  
   "JournalCode":string,
      /**  The journal number to which the disposal is posted.  */  
   "JournalNum":number,
      /**  The fiscal year in which the disposal is posted.  */  
   "FiscalYear":number,
      /**  The fiscal period in which the disposal is posted.  */  
   "FiscalPeriod":number,
      /**  The name of the customer that bought the disposal. The customer name can be entered even when no customer is selected.  */  
   "CustName":string,
      /**  The sales order that is used to sell the disposal.  */  
   "OrderNum":number,
      /**  The job that built the disposal.  */  
   "JobNum":string,
      /**  flag to indicate that the disposal is allowed to be posted.  */  
   "ReadyToPost":boolean,
      /**  The sales amount of the disposal.  */  
   "Proceed":number,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  The warehouse where the disposal came from. This is for information purposes only. In the warehouse tracker no assets can be tracked.  */  
   "WarehouseCode":string,
      /**  The bin where the disposal came from. This is for information purposes only. In the bin tracker no assets can be tracked.  */  
   "BinNum":string,
      /**  Indicates the type of asset disposal activity.  Valid values are: "SALE", "TRANSFER" or "MISC".  */  
   "DisposalType":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Unique identifier of the currency rate group.  */  
   "RateGrpCode":string,
      /**  Identifies the part number transferred from asset to stock.  This field is only required if the Disposal Type is "Transfer".  */  
   "PartNum":string,
      /**  Transferred Quantity reported for this disposal transfer.  */  
   "TransferQty":number,
      /**  Unit of Measure for the transferred quantity.  */  
   "TransferUOM":string,
      /**  Lot Number of the transferred part.  */  
   "LotNum":string,
      /**  Description of the transferred asset to stock.  */  
   "PartDescription":string,
      /**  The cost disposed from the asset in the currency specified.  */  
   "DocDisposalCost":number,
      /**  Reporting currency value of the cost disposed from the asset.  */  
   "Rpt1DisposalCost":number,
      /**  Reporting currency value of the cost disposed from the asset.  */  
   "Rpt2DisposalCost":number,
      /**  Reporting currency value of the cost disposed from the asset.  */  
   "Rpt3DisposalCost":number,
      /**  The sales amount of the disposal in the currency specified.  */  
   "DocProceed":number,
      /**  Reporting currency value of the proceed cost from the asset.  */  
   "Rpt1Proceed":number,
      /**  Reporting currency value of the proceed cost from the asset.  */  
   "Rpt2Proceed":number,
      /**  Reporting currency value of the proceed cost from the asset.  */  
   "Rpt3Proceed":number,
      /**  Location ID.  */  
   "LocID":string,
      /**  Descriptive code to uniquely identify the Equipment.  */  
   "EquipID":string,
      /**  Brand of equipment  */  
   "Brand":string,
      /**  This is the equivalent number of units for the transferred qty for this asset disposal.  There is no unit of measure conversion involved during update of this field.  The user is responsible for the "conversion" of transferred qty to asset units.  */  
   "TransferUnits":number,
      /**  This is the current disposal proceed balance (in document currency) left to be consumed in the AR Invoice interface process.  An asset disposal can be linked to one or more AR Invoice lines and each asset disposal linking to this invoice line will reduce the balance of this DocProceedInvBal.  When this field reaches zero then this disposal line cannot be linked in the AR Invoice interface anymore.  */  
   "DocProceedInvBal":number,
      /**  This is the number of Asset Units left to be consumed in the AR Invoice Interface process.  An asset disposal can be linked to one or more invoice lines and each asset disposal linking to this invoice line will reduce the balance qty of this AssetBalOurQty.  When this field reaches zero then this disposal cannot be linked in the AR Invoice interface anymore.  This qty is expressed in our unit of measure.  */  
   "AssetBalOurQty":number,
      /**  Unit of Measure code for asset invoiced quantity balance in our unit of measure.  */  
   "AssetQtyIUM":string,
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
      /**  Determines Asset Register from which Book Value will be taken as Proceeds.  */  
   "TransferBVFrom":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
   "CustID":string,
      /**  Indicates whether the serial numbers are required in AssetDispEntry  */  
   "EnableSN":boolean,
      /**  shows if is this addition transaction is blocked in RvLock.  */  
   "IsLcked":boolean,
      /**  Locked means can not be updated or deleted: the addition activity is already in review journal or in posting process.  */  
   "LockStatus":string,
   "PartLotTracked":boolean,
      /**  Review Journal UID  */  
   "RvnJrnUID":number,
   "BitFlag":number,
   "BaseCurrCurrName":string,
   "BaseCurrCurrencyID":string,
   "BaseCurrCurrSymbol":string,
   "BaseCurrCurrDesc":string,
   "BaseCurrDocumentDesc":string,
   "CurrencyCurrencyID":string,
   "CurrencyCurrName":string,
   "CurrencyDocumentDesc":string,
   "CurrencyCurrDesc":string,
   "CurrencyCurrSymbol":string,
   "UOMUOMDesc":string,
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
      @param assetNum
   */  
export interface CheckAssetDepRecalcNeeded_input{
      /**  Asset ID  */  
   assetNum:string,
}

export interface CheckAssetDepRecalcNeeded_output{
      /**  true if depreciation calculation is required  */  
   returnObj:boolean,
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
      @param disposed
   */  
export interface CheckDeprCalculated_input{
      /**  Asset ID  */  
   assetNum:string,
      /**  Disposal date  */  
   disposed:string,
}

export interface CheckDeprCalculated_output{
      /**  True if Depreciation was calculated, false - otherwise  */  
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   warning:string,
}
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
      @param disposalNum
   */  
export interface DeleteByID_input{
   assetNum:string,
   disposalNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_AssetDispEntryTableset{
   FADisposal:Erp_Tablesets_FADisposalRow[],
   FADisposalAttch:Erp_Tablesets_FADisposalAttchRow[],
   FADispReg:Erp_Tablesets_FADispRegRow[],
   SelectedSerialNumbers:Erp_Tablesets_SelectedSerialNumbersRow[],
   SNFormat:Erp_Tablesets_SNFormatRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_FADispRegRow{
      /**  Company of the Disposal.  */  
   Company:string,
      /**  Asset number of the Disposal.  */  
   AssetNum:string,
      /**  Unique number to identify the Disposal of an asset.  */  
   DisposalNum:number,
      /**  Identifier of the Asset Register.  */  
   AssetRegID:string,
      /**  The depreciation amount that is substracted from the Asset depreciation cost account for the posted depreciations of previous years.  */  
   PrevDepreciation:number,
      /**  The depreciation amount that is substracted from the Asset depreciation cost account for the posted depreciations of current year.  */  
   CurrDepreciation:number,
      /**  The Book Value of a disposal is calculated as the disposal cost minus disposal depreciation minus disposal current year depreciation.  */  
   BookValue:number,
      /**  The depreciation amount that is substracted from the Asset depreciation cost account for the posted depreciations of previous years in the specified currency.  */  
   DocPrevDepreciation:number,
      /**  The depreciation already applied to this addition in another system within the same holding company for this year in the specified currency.  */  
   DocCurrDepreciation:number,
      /**  This is the Book Value of a disposal in the specified currency.  */  
   DocBookValue:number,
      /**  Reporting currency of the previous years disposal depreciation.  */  
   Rpt1PrevDepreciation:number,
      /**  Reporting currency value of the current year disposal depreciation.  */  
   Rpt1CurrDepreciation:number,
      /**  Reporting currency value of the disposal book value.  */  
   Rpt1BookValue:number,
      /**  Reporting currency value of the previous years disposal depreciation.  */  
   Rpt2PrevDepreciation:number,
      /**  Reporting currency value of the current year disposal depreciation.  */  
   Rpt2CurrDepreciation:number,
      /**  Reporting currency value of the disposal book value.  */  
   Rpt2BookValue:number,
      /**  Reporting currency value of the previous years disposal depreciation.  */  
   Rpt3PrevDepreciation:number,
      /**  Reporting currency value of the current year disposal depreciation.  */  
   Rpt3CurrDepreciation:number,
      /**  Reporting currency value of the disposal book value.  */  
   Rpt3BookValue:number,
      /**  Grant Book Value of the disposal is a calculated field. It is Grant Amount minus previous years disposal Grant Depreciation minus current year disposal Grant Depreciation.  */  
   GrantBookValue:number,
      /**  The disposed portion of the total Grant Depreciation already posted for previous years.  */  
   PrevGrantDep:number,
      /**  The disposed portion of the total Grant Depreciation already posted for the current year.  */  
   CurrGrantDep:number,
      /**  Grant Book Value of the disposal is a calculated field. It is Grant Amount minus previous years disposal Grant Depreciation minus current year disposal Grant Depreciation.  */  
   DocGrantBookValue:number,
      /**  The disposed portion of the total Grant Depreciation already posted for previous years.  */  
   DocPrevGrantDep:number,
      /**  The disposed portion of the total Grant Depreciation already posted for the current year.  */  
   DocCurrGrantDep:number,
      /**  Grant Book Value of the disposal is a calculated field. It is Grant Amount minus previous years disposal Grant Depreciation minus current year disposal Grant Depreciation.  */  
   Rpt1GrantBookValue:number,
      /**  The disposed portion of the total Grant Depreciation already posted for previous years.  */  
   Rpt1PrevGrantDep:number,
      /**  The disposed portion of the total Grant Depreciation already posted for the current year.  */  
   Rpt1CurrGrantDep:number,
      /**  Grant Book Value of the disposal is a calculated field. It is Grant Amount minus previous years disposal Grant Depreciation minus current year disposal Grant Depreciation.  */  
   Rpt2GrantBookValue:number,
      /**  The disposed portion of the total Grant Depreciation already posted for previous years.  */  
   Rpt2PrevGrantDep:number,
      /**  The disposed portion of the total Grant Depreciation already posted for the current year.  */  
   Rpt2CurrGrantDep:number,
      /**  Grant Book Value of the disposal is a calculated field. It is Grant Amount minus previous years disposal Grant Depreciation minus current year disposal Grant Depreciation.  */  
   Rpt3GrantBookValue:number,
      /**  The disposed portion of the total Grant Depreciation already posted for previous years.  */  
   Rpt3PrevGrantDep:number,
      /**  The disposed portion of the total Grant Depreciation already posted for the current year.  */  
   Rpt3CurrGrantDep:number,
      /**  The Grant Amount awarded to an asset to reduce the depreciation charge.  */  
   GrantAmt:number,
      /**  The Grant Amount awarded to an asset to reduce the depreciation charge in the currency specified.  */  
   DocGrantAmt:number,
      /**  Reporting currency value of the Grant Amount.  */  
   Rpt1GrantAmt:number,
      /**  Reporting currency value of the Grant Amount.  */  
   Rpt2GrantAmt:number,
      /**  Reporting currency value of the Grant Amount.  */  
   Rpt3GrantAmt:number,
      /**  The cost disposed from the asset.  */  
   DisposalCost:number,
      /**  The cost disposed from the asset in the currency specified.  */  
   DocDisposalCost:number,
      /**  Reporting currency value of the cost disposed from the asset.  */  
   Rpt1DisposalCost:number,
      /**  Reporting currency value of the cost disposed from the asset.  */  
   Rpt2DisposalCost:number,
      /**  Reporting currency value of the cost disposed from the asset.  */  
   Rpt3DisposalCost:number,
      /**  The sales amount of the disposal.  */  
   Proceed:number,
      /**  The sales amount of the disposal in the currency specified.  */  
   DocProceed:number,
      /**  Reporting currency value of the proceed cost from the asset.  */  
   Rpt1Proceed:number,
      /**  Reporting currency value of the proceed cost from the asset.  */  
   Rpt2Proceed:number,
      /**  Reporting currency value of the proceed cost from the asset.  */  
   Rpt3Proceed:number,
      /**  This is the current disposal proceed balance (in document currency) left to be consumed in the AR Invoice interface process.  An asset disposal can be linked to one or more AR Invoice lines and each asset disposal linking to this invoice line will reduce the balance of this DocProceedInvBal.  When this field reaches zero then this disposal line cannot be linked in the AR Invoice interface anymore.  */  
   DocProceedInvBal:number,
      /**  This is the number of Asset Units left to be consumed in the AR Invoice Interface process.  An asset disposal can be linked to one or more invoice lines and each asset disposal linking to this invoice line will reduce the balance qty of this AssetBalOurQty.  When this field reaches zero then this disposal cannot be linked in the AR Invoice interface anymore.  This qty is expressed in our unit of measure.  */  
   AssetBalOurQty:number,
      /**  Unit of Measure code for asset invoiced quantity balance in our unit of measure.  */  
   AssetQtyIUM:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Value of Depreciation on disposal setting of the asset, that was used to create the disposal.  */  
   DepOnDisposal:number,
   CurrCode:string,
   RateGrpCode:string,
      /**  Disposal Profit/Loss in base currency. Calculated field.  */  
   DisposalProfitLoss:number,
      /**  Disposal Profit/Loss in document currency. Calculated field.  */  
   DocDisposalProfitLoss:number,
      /**  Disposal Profit/Loss in Rpt1 currency. Calculated field.  */  
   Rpt1DisposalProfitLoss:number,
      /**  Disposal Profit/Loss in Rpt2 currency. Calculated field.  */  
   Rpt2DisposalProfitLoss:number,
      /**  Disposal Profit/Loss in Rpt3 currency. Calculated field.  */  
   Rpt3DisposalProfitLoss:number,
   BitFlag:number,
   FAssetRegDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FADisposalAttchRow{
   Company:string,
   AssetNum:string,
   DisposalNum:number,
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

export interface Erp_Tablesets_FADisposalListRow{
      /**  Company of the Disposal.  */  
   Company:string,
      /**  Asset number of the Disposal.  */  
   AssetNum:string,
      /**  Unique number to identify the Disposal of an asset.  */  
   DisposalNum:number,
      /**  The date of Disposal.  */  
   Disposed:string,
      /**  The cost disposed from the asset.  */  
   DisposalCost:number,
      /**  Description of the disposal.  */  
   Description:string,
      /**  Invoice number of the customer.  */  
   InvoiceNum:number,
      /**  Internal customer number.  */  
   CustNum:number,
      /**  The invoice line of the customer invoice.  */  
   InvoiceLine:number,
      /**  The orignal manufacturer of the disposal.  */  
   Manufacturer:string,
      /**  The model number of the disposal.  */  
   Model:string,
      /**  The serial number of the disposal.  */  
   Serialno:string,
      /**  Flag to indicate that the disposal is posted to the gL.  */  
   Posted:boolean,
      /**  The post date of the posting to the GL.  */  
   PostDate:string,
      /**  The user that posted the disposal to the GL.  */  
   PostedBy:string,
      /**  The GL journal to which the disposal is posted.  */  
   JournalCode:string,
      /**  The journal number to which the disposal is posted.  */  
   JournalNum:number,
      /**  The fiscal year in which the disposal is posted.  */  
   FiscalYear:number,
      /**  The fiscal period in which the disposal is posted.  */  
   FiscalPeriod:number,
      /**  The name of the customer that bought the disposal. The customer name can be entered even when no customer is selected.  */  
   CustName:string,
      /**  The sales order that is used to sell the disposal.  */  
   OrderNum:number,
      /**  The job that built the disposal.  */  
   JobNum:string,
      /**  flag to indicate that the disposal is allowed to be posted.  */  
   ReadyToPost:boolean,
      /**  The sales amount of the disposal.  */  
   Proceed:number,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  The warehouse where the disposal came from. This is for information purposes only. In the warehouse tracker no assets can be tracked.  */  
   WarehouseCode:string,
      /**  The bin where the disposal came from. This is for information purposes only. In the bin tracker no assets can be tracked.  */  
   BinNum:string,
      /**  Indicates the type of asset disposal activity.  Valid values are: "SALE", "TRANSFER" or "MISC".  */  
   DisposalType:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Unique identifier of the currency rate group.  */  
   RateGrpCode:string,
      /**  Identifies the part number transferred from asset to stock.  This field is only required if the Disposal Type is "Transfer".  */  
   PartNum:string,
      /**  Transferred Quantity reported for this disposal transfer.  */  
   TransferQty:number,
      /**  Unit of Measure for the transferred quantity.  */  
   TransferUOM:string,
      /**  Lot Number of the transferred part.  */  
   LotNum:string,
      /**  Description of the transferred asset to stock.  */  
   PartDescription:string,
      /**  The cost disposed from the asset in the currency specified.  */  
   DocDisposalCost:number,
      /**  Reporting currency value of the cost disposed from the asset.  */  
   Rpt1DisposalCost:number,
      /**  Reporting currency value of the cost disposed from the asset.  */  
   Rpt2DisposalCost:number,
      /**  Reporting currency value of the cost disposed from the asset.  */  
   Rpt3DisposalCost:number,
      /**  The sales amount of the disposal in the currency specified.  */  
   DocProceed:number,
      /**  Reporting currency value of the proceed cost from the asset.  */  
   Rpt1Proceed:number,
      /**  Reporting currency value of the proceed cost from the asset.  */  
   Rpt2Proceed:number,
      /**  Reporting currency value of the proceed cost from the asset.  */  
   Rpt3Proceed:number,
      /**  Location ID.  */  
   LocID:string,
      /**  Descriptive code to uniquely identify the Equipment.  */  
   EquipID:string,
      /**  Brand of equipment  */  
   Brand:string,
      /**  This is the equivalent number of units for the transferred qty for this asset disposal.  There is no unit of measure conversion involved during update of this field.  The user is responsible for the "conversion" of transferred qty to asset units.  */  
   TransferUnits:number,
      /**  This is the current disposal proceed balance (in document currency) left to be consumed in the AR Invoice interface process.  An asset disposal can be linked to one or more AR Invoice lines and each asset disposal linking to this invoice line will reduce the balance of this DocProceedInvBal.  When this field reaches zero then this disposal line cannot be linked in the AR Invoice interface anymore.  */  
   DocProceedInvBal:number,
      /**  This is the number of Asset Units left to be consumed in the AR Invoice Interface process.  An asset disposal can be linked to one or more invoice lines and each asset disposal linking to this invoice line will reduce the balance qty of this AssetBalOurQty.  When this field reaches zero then this disposal cannot be linked in the AR Invoice interface anymore.  This qty is expressed in our unit of measure.  */  
   AssetBalOurQty:number,
      /**  Unit of Measure code for asset invoiced quantity balance in our unit of measure.  */  
   AssetQtyIUM:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   CustID:string,
   PartLotTracked:boolean,
      /**  shows if is this addition transaction is blocked in RvLock.  */  
   IsLcked:boolean,
      /**  Locked means can not be updated or deleted: the addition activity is already in review journal or in posting process.  */  
   LockStatus:string,
      /**  Review Journal UID  */  
   RvnJrnUID:number,
      /**  Description of the currency  */  
   BaseCurrCurrDesc:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   BaseCurrCurrName:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   BaseCurrCurrencyID:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   BaseCurrCurrSymbol:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   BaseCurrDocumentDesc:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   CurrencyCurrName:string,
      /**  Description of the currency  */  
   CurrencyCurrDesc:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   CurrencyDocumentDesc:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   CurrencyCurrencyID:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   CurrencyCurrSymbol:string,
      /**  Long Description of a unit of measure. Mandatory.  */  
   UOMUOMDesc:string,
      /**  Description.  */  
   WhseDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FADisposalListTableset{
   FADisposalList:Erp_Tablesets_FADisposalListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_FADisposalRow{
      /**  Company of the Disposal.  */  
   Company:string,
      /**  Asset number of the Disposal.  */  
   AssetNum:string,
      /**  Unique number to identify the Disposal of an asset.  */  
   DisposalNum:number,
      /**  The date of Disposal.  */  
   Disposed:string,
      /**  The cost disposed from the asset.  */  
   DisposalCost:number,
      /**  Description of the disposal.  */  
   Description:string,
      /**  Invoice number of the customer.  */  
   InvoiceNum:number,
      /**  Internal customer number.  */  
   CustNum:number,
      /**  The invoice line of the customer invoice.  */  
   InvoiceLine:number,
      /**  The orignal manufacturer of the disposal.  */  
   Manufacturer:string,
      /**  The model number of the disposal.  */  
   Model:string,
      /**  The serial number of the disposal.  */  
   Serialno:string,
      /**  Flag to indicate that the disposal is posted to the gL.  */  
   Posted:boolean,
      /**  The post date of the posting to the GL.  */  
   PostDate:string,
      /**  The user that posted the disposal to the GL.  */  
   PostedBy:string,
      /**  The GL journal to which the disposal is posted.  */  
   JournalCode:string,
      /**  The journal number to which the disposal is posted.  */  
   JournalNum:number,
      /**  The fiscal year in which the disposal is posted.  */  
   FiscalYear:number,
      /**  The fiscal period in which the disposal is posted.  */  
   FiscalPeriod:number,
      /**  The name of the customer that bought the disposal. The customer name can be entered even when no customer is selected.  */  
   CustName:string,
      /**  The sales order that is used to sell the disposal.  */  
   OrderNum:number,
      /**  The job that built the disposal.  */  
   JobNum:string,
      /**  flag to indicate that the disposal is allowed to be posted.  */  
   ReadyToPost:boolean,
      /**  The sales amount of the disposal.  */  
   Proceed:number,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  The warehouse where the disposal came from. This is for information purposes only. In the warehouse tracker no assets can be tracked.  */  
   WarehouseCode:string,
      /**  The bin where the disposal came from. This is for information purposes only. In the bin tracker no assets can be tracked.  */  
   BinNum:string,
      /**  Indicates the type of asset disposal activity.  Valid values are: "SALE", "TRANSFER" or "MISC".  */  
   DisposalType:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Unique identifier of the currency rate group.  */  
   RateGrpCode:string,
      /**  Identifies the part number transferred from asset to stock.  This field is only required if the Disposal Type is "Transfer".  */  
   PartNum:string,
      /**  Transferred Quantity reported for this disposal transfer.  */  
   TransferQty:number,
      /**  Unit of Measure for the transferred quantity.  */  
   TransferUOM:string,
      /**  Lot Number of the transferred part.  */  
   LotNum:string,
      /**  Description of the transferred asset to stock.  */  
   PartDescription:string,
      /**  The cost disposed from the asset in the currency specified.  */  
   DocDisposalCost:number,
      /**  Reporting currency value of the cost disposed from the asset.  */  
   Rpt1DisposalCost:number,
      /**  Reporting currency value of the cost disposed from the asset.  */  
   Rpt2DisposalCost:number,
      /**  Reporting currency value of the cost disposed from the asset.  */  
   Rpt3DisposalCost:number,
      /**  The sales amount of the disposal in the currency specified.  */  
   DocProceed:number,
      /**  Reporting currency value of the proceed cost from the asset.  */  
   Rpt1Proceed:number,
      /**  Reporting currency value of the proceed cost from the asset.  */  
   Rpt2Proceed:number,
      /**  Reporting currency value of the proceed cost from the asset.  */  
   Rpt3Proceed:number,
      /**  Location ID.  */  
   LocID:string,
      /**  Descriptive code to uniquely identify the Equipment.  */  
   EquipID:string,
      /**  Brand of equipment  */  
   Brand:string,
      /**  This is the equivalent number of units for the transferred qty for this asset disposal.  There is no unit of measure conversion involved during update of this field.  The user is responsible for the "conversion" of transferred qty to asset units.  */  
   TransferUnits:number,
      /**  This is the current disposal proceed balance (in document currency) left to be consumed in the AR Invoice interface process.  An asset disposal can be linked to one or more AR Invoice lines and each asset disposal linking to this invoice line will reduce the balance of this DocProceedInvBal.  When this field reaches zero then this disposal line cannot be linked in the AR Invoice interface anymore.  */  
   DocProceedInvBal:number,
      /**  This is the number of Asset Units left to be consumed in the AR Invoice Interface process.  An asset disposal can be linked to one or more invoice lines and each asset disposal linking to this invoice line will reduce the balance qty of this AssetBalOurQty.  When this field reaches zero then this disposal cannot be linked in the AR Invoice interface anymore.  This qty is expressed in our unit of measure.  */  
   AssetBalOurQty:number,
      /**  Unit of Measure code for asset invoiced quantity balance in our unit of measure.  */  
   AssetQtyIUM:string,
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
      /**  Determines Asset Register from which Book Value will be taken as Proceeds.  */  
   TransferBVFrom:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
   CustID:string,
      /**  Indicates whether the serial numbers are required in AssetDispEntry  */  
   EnableSN:boolean,
      /**  shows if is this addition transaction is blocked in RvLock.  */  
   IsLcked:boolean,
      /**  Locked means can not be updated or deleted: the addition activity is already in review journal or in posting process.  */  
   LockStatus:string,
   PartLotTracked:boolean,
      /**  Review Journal UID  */  
   RvnJrnUID:number,
   BitFlag:number,
   BaseCurrCurrName:string,
   BaseCurrCurrencyID:string,
   BaseCurrCurrSymbol:string,
   BaseCurrCurrDesc:string,
   BaseCurrDocumentDesc:string,
   CurrencyCurrencyID:string,
   CurrencyCurrName:string,
   CurrencyDocumentDesc:string,
   CurrencyCurrDesc:string,
   CurrencyCurrSymbol:string,
   UOMUOMDesc:string,
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

export interface Erp_Tablesets_UpdExtAssetDispEntryTableset{
   FADisposal:Erp_Tablesets_FADisposalRow[],
   FADisposalAttch:Erp_Tablesets_FADisposalAttchRow[],
   FADispReg:Erp_Tablesets_FADispRegRow[],
   SelectedSerialNumbers:Erp_Tablesets_SelectedSerialNumbersRow[],
   SNFormat:Erp_Tablesets_SNFormatRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param assetNum
      @param disposalNum
   */  
export interface GetByID_input{
   assetNum:string,
   disposalNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_AssetDispEntryTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_AssetDispEntryTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_AssetDispEntryTableset[],
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
   returnObj:Erp_Tablesets_FADisposalListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param assetNum
      @param disposalNum
   */  
export interface GetNewFADispReg_input{
   ds:Erp_Tablesets_AssetDispEntryTableset[],
   assetNum:string,
   disposalNum:number,
}

export interface GetNewFADispReg_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AssetDispEntryTableset[],
}
}

   /** Required : 
      @param ds
      @param assetNum
      @param disposalNum
   */  
export interface GetNewFADisposalAttch_input{
   ds:Erp_Tablesets_AssetDispEntryTableset[],
   assetNum:string,
   disposalNum:number,
}

export interface GetNewFADisposalAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AssetDispEntryTableset[],
}
}

   /** Required : 
      @param ds
      @param assetNum
   */  
export interface GetNewFADisposal_input{
   ds:Erp_Tablesets_AssetDispEntryTableset[],
   assetNum:string,
}

export interface GetNewFADisposal_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AssetDispEntryTableset[],
}
}

   /** Required : 
      @param whereClauseFADisposal
      @param whereClauseFADisposalAttch
      @param whereClauseFADispReg
      @param whereClauseSelectedSerialNumbers
      @param whereClauseSNFormat
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseFADisposal:string,
   whereClauseFADisposalAttch:string,
   whereClauseFADispReg:string,
   whereClauseSelectedSerialNumbers:string,
   whereClauseSNFormat:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_AssetDispEntryTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetSelectSerialNumbersParams_input{
   ds:Erp_Tablesets_AssetDispEntryTableset[],
}

export interface GetSelectSerialNumbersParams_output{
   returnObj:Erp_Tablesets_SelectSerialNumbersParamsTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AssetDispEntryTableset[],
}
}

   /** Required : 
      @param company
      @param assetNum
      @param disposalNum
      @param ds
   */  
export interface GetSelectedSerialNumbers_input{
      /**  The Asset Number  */  
   company:string,
      /**  The Asset Number  */  
   assetNum:string,
      /**  The Disposal number  */  
   disposalNum:number,
   ds:Erp_Tablesets_AssetDispEntryTableset[],
}

export interface GetSelectedSerialNumbers_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AssetDispEntryTableset[],
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
      @param ipBinNum
      @param ds
   */  
export interface LeaveBinNum_input{
      /**  bin that was entered.  */  
   ipBinNum:string,
   ds:Erp_Tablesets_AssetDispEntryTableset[],
}

export interface LeaveBinNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AssetDispEntryTableset[],
   oSerialWarning:string,
}
}

   /** Required : 
      @param ipcustid
      @param ds
   */  
export interface LeaveCustID_input{
      /**  custid that was entered.  */  
   ipcustid:string,
   ds:Erp_Tablesets_AssetDispEntryTableset[],
}

export interface LeaveCustID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AssetDispEntryTableset[],
}
}

   /** Required : 
      @param ipdisposalcost
      @param ds
   */  
export interface LeaveDisposalCost_input{
      /**  disposalcost that was entered.  */  
   ipdisposalcost:number,
   ds:Erp_Tablesets_AssetDispEntryTableset[],
}

export interface LeaveDisposalCost_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AssetDispEntryTableset[],
}
}

   /** Required : 
      @param ipdisposaltype
      @param ds
   */  
export interface LeaveDisposalType_input{
      /**  disposal type that was selected.  */  
   ipdisposaltype:string,
   ds:Erp_Tablesets_AssetDispEntryTableset[],
}

export interface LeaveDisposalType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AssetDispEntryTableset[],
   oSerialWarning:string,
}
}

   /** Required : 
      @param ipDisposed
      @param ds
   */  
export interface LeaveDisposed_input{
      /**  Disposal Date that was entered.  */  
   ipDisposed:string,
   ds:Erp_Tablesets_AssetDispEntryTableset[],
}

export interface LeaveDisposed_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AssetDispEntryTableset[],
}
}

   /** Required : 
      @param ipjobnum
      @param ds
   */  
export interface LeaveJobNum_input{
   ipjobnum:string,
   ds:Erp_Tablesets_AssetDispEntryTableset[],
}

export interface LeaveJobNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AssetDispEntryTableset[],
}
}

   /** Required : 
      @param ipordernum
      @param ds
   */  
export interface LeaveOrderNum_input{
      /**  ordernum that was entered.  */  
   ipordernum:number,
   ds:Erp_Tablesets_AssetDispEntryTableset[],
}

export interface LeaveOrderNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AssetDispEntryTableset[],
}
}

   /** Required : 
      @param ippartnum
      @param ds
   */  
export interface LeavePartNum_input{
      /**  partnum that was entered.  */  
   ippartnum:string,
   ds:Erp_Tablesets_AssetDispEntryTableset[],
}

export interface LeavePartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AssetDispEntryTableset[],
   oSerialWarning:string,
}
}

   /** Required : 
      @param ipproceed
      @param ipbaseordoc
      @param ds
   */  
export interface LeaveProceed_input{
      /**  disposalcost that was entered.  */  
   ipproceed:number,
      /**  The field type - base or doc  */  
   ipbaseordoc:string,
   ds:Erp_Tablesets_AssetDispEntryTableset[],
}

export interface LeaveProceed_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AssetDispEntryTableset[],
}
}

   /** Required : 
      @param ipWarehouseCode
      @param ds
   */  
export interface LeaveWarehouseCode_input{
      /**  warehouse code that was entered.  */  
   ipWarehouseCode:string,
   ds:Erp_Tablesets_AssetDispEntryTableset[],
}

export interface LeaveWarehouseCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AssetDispEntryTableset[],
   oSerialWarning:string,
}
}

   /** Required : 
      @param ds
   */  
export interface OnSetReadyToPost_input{
   ds:Erp_Tablesets_AssetDispEntryTableset[],
}

export interface OnSetReadyToPost_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AssetDispEntryTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtAssetDispEntryTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtAssetDispEntryTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_AssetDispEntryTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AssetDispEntryTableset[],
}
}

   /** Required : 
      @param ds
      @param serialNumber
   */  
export interface ValidateSN_input{
   ds:Erp_Tablesets_AssetDispEntryTableset[],
      /**  Serial number to validate.  */  
   serialNumber:string,
}

export interface ValidateSN_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AssetDispEntryTableset[],
   isVoided:boolean,
}
}

