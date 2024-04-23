import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.LogInvAprvVoidSvc
# Description: Add your summary for this object here
# Version: v1



#########################################################################
# OData methods:
#########################################################################
async def getServiceDocument(epicorHeaders = None):
   """  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => application/json
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/",headers=creds) as resp:
           return await resp.json()

async def get_metadata(epicorHeaders = None):
   """  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: Returns metadata document => content
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_LogInvAprvVoids(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LogInvAprvVoids items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LogInvAprvVoids
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LogAPInvRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LogInvAprvVoids",headers=creds) as resp:
           return await resp.json()

async def post_LogInvAprvVoids(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LogInvAprvVoids
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LogAPInvRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LogAPInvRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LogInvAprvVoids", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LogInvAprvVoids_Company_VendorNum_InvoiceNum(Company, VendorNum, InvoiceNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LogInvAprvVoid item
   Description: Calls GetByID to retrieve the LogInvAprvVoid item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LogInvAprvVoid
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LogAPInvRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LogInvAprvVoids(" + Company + "," + VendorNum + "," + InvoiceNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LogInvAprvVoids_Company_VendorNum_InvoiceNum(Company, VendorNum, InvoiceNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LogInvAprvVoid for the service
   Description: Calls UpdateExt to update LogInvAprvVoid. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LogInvAprvVoid
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LogAPInvRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LogInvAprvVoids(" + Company + "," + VendorNum + "," + InvoiceNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LogInvAprvVoids_Company_VendorNum_InvoiceNum(Company, VendorNum, InvoiceNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LogInvAprvVoid item
   Description: Call UpdateExt to delete LogInvAprvVoid item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LogInvAprvVoid
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LogInvAprvVoids(" + Company + "," + VendorNum + "," + InvoiceNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_LogInvAprvVoids_Company_VendorNum_InvoiceNum_LogAPInvTaxes(Company, VendorNum, InvoiceNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get LogAPInvTaxes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LogAPInvTaxes1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LogAPInvTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LogInvAprvVoids(" + Company + "," + VendorNum + "," + InvoiceNum + ")/LogAPInvTaxes",headers=creds) as resp:
           return await resp.json()

async def get_LogInvAprvVoids_Company_VendorNum_InvoiceNum_LogAPInvTaxes_Company_VendorNum_InvoiceNum_TaxCode_RateCode_ECAcquisitionSeq_Void(Company, VendorNum, InvoiceNum, TaxCode, RateCode, ECAcquisitionSeq, Void, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LogAPInvTax item
   Description: Calls GetByID to retrieve the LogAPInvTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LogAPInvTax1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param Void: Desc: Void   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LogAPInvTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LogInvAprvVoids(" + Company + "," + VendorNum + "," + InvoiceNum + ")/LogAPInvTaxes(" + Company + "," + VendorNum + "," + InvoiceNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + "," + Void + ")",headers=creds) as resp:
           return await resp.json()

async def get_LogInvAprvVoids_Company_VendorNum_InvoiceNum_EntityGLCs(Company, VendorNum, InvoiceNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get EntityGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EntityGLCs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LogInvAprvVoids(" + Company + "," + VendorNum + "," + InvoiceNum + ")/EntityGLCs",headers=creds) as resp:
           return await resp.json()

async def get_LogInvAprvVoids_Company_VendorNum_InvoiceNum_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, VendorNum, InvoiceNum, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EntityGLC item
   Description: Calls GetByID to retrieve the EntityGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EntityGLC1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param Key6: Desc: Key6   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LogInvAprvVoids(" + Company + "," + VendorNum + "," + InvoiceNum + ")/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def get_LogInvAprvVoids_Company_VendorNum_InvoiceNum_LogAPInvAttches(Company, VendorNum, InvoiceNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get LogAPInvAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LogAPInvAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LogAPInvAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LogInvAprvVoids(" + Company + "," + VendorNum + "," + InvoiceNum + ")/LogAPInvAttches",headers=creds) as resp:
           return await resp.json()

async def get_LogInvAprvVoids_Company_VendorNum_InvoiceNum_LogAPInvAttches_Company_VendorNum_InvoiceNum_DrawingSeq(Company, VendorNum, InvoiceNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LogAPInvAttch item
   Description: Calls GetByID to retrieve the LogAPInvAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LogAPInvAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LogAPInvAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LogInvAprvVoids(" + Company + "," + VendorNum + "," + InvoiceNum + ")/LogAPInvAttches(" + Company + "," + VendorNum + "," + InvoiceNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_LogAPInvTaxes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LogAPInvTaxes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LogAPInvTaxes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LogAPInvTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LogAPInvTaxes",headers=creds) as resp:
           return await resp.json()

async def post_LogAPInvTaxes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LogAPInvTaxes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LogAPInvTaxRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LogAPInvTaxRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LogAPInvTaxes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LogAPInvTaxes_Company_VendorNum_InvoiceNum_TaxCode_RateCode_ECAcquisitionSeq_Void(Company, VendorNum, InvoiceNum, TaxCode, RateCode, ECAcquisitionSeq, Void, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LogAPInvTax item
   Description: Calls GetByID to retrieve the LogAPInvTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LogAPInvTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param Void: Desc: Void   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LogAPInvTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LogAPInvTaxes(" + Company + "," + VendorNum + "," + InvoiceNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + "," + Void + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LogAPInvTaxes_Company_VendorNum_InvoiceNum_TaxCode_RateCode_ECAcquisitionSeq_Void(Company, VendorNum, InvoiceNum, TaxCode, RateCode, ECAcquisitionSeq, Void, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LogAPInvTax for the service
   Description: Calls UpdateExt to update LogAPInvTax. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LogAPInvTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param Void: Desc: Void   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LogAPInvTaxRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LogAPInvTaxes(" + Company + "," + VendorNum + "," + InvoiceNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + "," + Void + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LogAPInvTaxes_Company_VendorNum_InvoiceNum_TaxCode_RateCode_ECAcquisitionSeq_Void(Company, VendorNum, InvoiceNum, TaxCode, RateCode, ECAcquisitionSeq, Void, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LogAPInvTax item
   Description: Call UpdateExt to delete LogAPInvTax item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LogAPInvTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param Void: Desc: Void   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LogAPInvTaxes(" + Company + "," + VendorNum + "," + InvoiceNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + "," + Void + ")",headers=creds) as resp:
           return await resp.json()

async def get_EntityGLCs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get EntityGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EntityGLCs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/EntityGLCs",headers=creds) as resp:
           return await resp.json()

async def post_EntityGLCs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EntityGLCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/EntityGLCs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EntityGLC item
   Description: Calls GetByID to retrieve the EntityGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EntityGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param Key6: Desc: Key6   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def patch_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update EntityGLC for the service
   Description: Calls UpdateExt to update EntityGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EntityGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param Key6: Desc: Key6   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete EntityGLC item
   Description: Call UpdateExt to delete EntityGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EntityGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param Key6: Desc: Key6   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def get_LogAPInvAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LogAPInvAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LogAPInvAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LogAPInvAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LogAPInvAttches",headers=creds) as resp:
           return await resp.json()

async def post_LogAPInvAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LogAPInvAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LogAPInvAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LogAPInvAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LogAPInvAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LogAPInvAttches_Company_VendorNum_InvoiceNum_DrawingSeq(Company, VendorNum, InvoiceNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LogAPInvAttch item
   Description: Calls GetByID to retrieve the LogAPInvAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LogAPInvAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LogAPInvAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LogAPInvAttches(" + Company + "," + VendorNum + "," + InvoiceNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LogAPInvAttches_Company_VendorNum_InvoiceNum_DrawingSeq(Company, VendorNum, InvoiceNum, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LogAPInvAttch for the service
   Description: Calls UpdateExt to update LogAPInvAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LogAPInvAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LogAPInvAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LogAPInvAttches(" + Company + "," + VendorNum + "," + InvoiceNum + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LogAPInvAttches_Company_VendorNum_InvoiceNum_DrawingSeq(Company, VendorNum, InvoiceNum, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LogAPInvAttch item
   Description: Call UpdateExt to delete LogAPInvAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LogAPInvAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LogAPInvAttches(" + Company + "," + VendorNum + "," + InvoiceNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_LegalNumberGenerates(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LegalNumberGenerates items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LegalNumberGenerates
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LegalNumberGenerateRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LegalNumberGenerates",headers=creds) as resp:
           return await resp.json()

async def post_LegalNumberGenerates(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LegalNumberGenerates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LegalNumberGenerateRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LegalNumberGenerateRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LegalNumberGenerates", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LegalNumberGenerates_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LegalNumberGenerate item
   Description: Calls GetByID to retrieve the LegalNumberGenerate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LegalNumberGenerate
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LegalNumberGenerateRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LegalNumberGenerates(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LegalNumberGenerates_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LegalNumberGenerate for the service
   Description: Calls UpdateExt to update LegalNumberGenerate. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LegalNumberGenerate
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LegalNumberGenerateRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LegalNumberGenerates(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LegalNumberGenerates_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LegalNumberGenerate item
   Description: Call UpdateExt to delete LegalNumberGenerate item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LegalNumberGenerate
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/LegalNumberGenerates(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_List(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LogAPInvListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseLogAPInv, whereClauseLogAPInvAttch, whereClauseLogAPInvTax, whereClauseEntityGLC, whereClauseLegalNumberGenerate, pageSize, absolutePage, epicorHeaders = None):
   """  
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
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseLogAPInv=" + whereClauseLogAPInv
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseLogAPInvAttch=" + whereClauseLogAPInvAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseLogAPInvTax=" + whereClauseLogAPInvTax
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseEntityGLC=" + whereClauseEntityGLC
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseLegalNumberGenerate=" + whereClauseLegalNumberGenerate
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(vendorNum, invoiceNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "vendorNum=" + vendorNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "invoiceNum=" + invoiceNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetList(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      :param whereClause: Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      :param pageSize: Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      :param absolutePage: Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClause=" + whereClause
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_CanUserVoid(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CanUserVoid
   Description: Purpose:
Parameters:
<param name="ipInvoiceNum">Invoice Number user wants to void</param><param name="ipVendorNum">Vendor assigned to ipInvoiceNum</param><param name="opCanVoid"> indicates if the user can void the logged invoice</param><param name="opMessage">text indicating why a user cannot void</param>
Notes:
   OperationID: CanUserVoid
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CanUserVoid_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CanUserVoid_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeApproved(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeApproved
   Description: Method to call when changing the approved flag on the invoice.
   OperationID: ChangeApproved
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeApproved_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeApproved_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckDocumentIsLocked(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckDocumentIsLocked
   Description: Method to call when it is necessary to check if document is lock, before doing smth.
   OperationID: CheckDocumentIsLocked
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckDocumentIsLocked_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDocumentIsLocked_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_VoidLoggedInvoice(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method VoidLoggedInvoice
   Description: Purpose:
Parameters:
<param name="ds">The Logged Invoice Approval/Void data set</param>
Notes:
   OperationID: VoidLoggedInvoice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VoidLoggedInvoice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidLoggedInvoice_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CalcTaxes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CalcTaxes
   OperationID: CalcTaxes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalcTaxes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalcTaxes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewLogAPInv(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLogAPInv
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLogAPInv
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLogAPInv_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLogAPInv_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewLogAPInvAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLogAPInvAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLogAPInvAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLogAPInvAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLogAPInvAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewLogAPInvTax(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLogAPInvTax
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLogAPInvTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLogAPInvTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLogAPInvTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewEntityGLC(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewEntityGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEntityGLC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEntityGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEntityGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewLegalNumberGenerate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLegalNumberGenerate
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLegalNumberGenerate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLegalNumberGenerate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLegalNumberGenerate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowID(id, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "id=" + id

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowIDs(ids, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ids=" + ids

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_Update(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LogInvAprvVoidSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_EntityGLCRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumberGenerateRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LegalNumberGenerateRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LogAPInvAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LogAPInvAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LogAPInvListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LogAPInvListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LogAPInvRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LogAPInvRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LogAPInvTaxRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LogAPInvTaxRow] = obj["value"]
      pass

class Erp_Tablesets_EntityGLCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "Part"  control this field would contain the related Part Number,  for a "Customer"  it contains the Customer.CustNum.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.
The usage of this field is dependent on the type of record.  """  
      self.Key3:str = obj["Key3"]
      """   3rd component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key4:str = obj["Key4"]
      """   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key5:str = obj["Key5"]
      """   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key6:str = obj["Key6"]
      """   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.GLControlType:str = obj["GLControlType"]
      """  Identifier of the GL Control Type.  """  
      self.GLControlCode:str = obj["GLControlCode"]
      """  GL Control Identifier.  """  
      self.BusinessEntity:str = obj["BusinessEntity"]
      """  Identifies the entity.  Reference only.  Used for integrity validation when deleting a GLCTEntity record.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.IsExternalCompany:bool = obj["IsExternalCompany"]
      """  Flag to indicate the account in this record is for an external company.  """  
      self.GlobalEntityGLC:bool = obj["GlobalEntityGLC"]
      """  Marks this EntityGLC as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID of the related BankAcct record.  """  
      self.BankFeeID:str = obj["BankFeeID"]
      self.CallCode:str = obj["CallCode"]
      """  CallCode of the related FSCallCd record.  """  
      self.ChargeCode:str = obj["ChargeCode"]
      self.ClassCode:str = obj["ClassCode"]
      """  ClassCode of the related FAClass record.  """  
      self.ClassID:str = obj["ClassID"]
      """  ClassID.  This can be ClassID of PartClass, PRClsDed, or PRClsTax  """  
      self.ContractCode:str = obj["ContractCode"]
      """  ContractCode of the related FSContCd record.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  CurrencyCode of the related Currency record.  """  
      self.CustNum:int = obj["CustNum"]
      """  CustNum of the related Customer record  """  
      self.DeductionID:str = obj["DeductionID"]
      """  DeductionID of PRClsDed or PRDeduct.  """  
      self.EmpID:str = obj["EmpID"]
      """  EmpID of the related PREmpMas record.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  ExpenseCode of PayTLbr, LabExpCd  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  ExtSystemID of ExtCompany table  """  
      self.FromPlant:str = obj["FromPlant"]
      """  FromPlant value of the related PlntTranDef record.  """  
      self.GroupCode:str = obj["GroupCode"]
      """  GroupCode of the related FAGroup record.  """  
      self.GroupID:str = obj["GroupID"]
      self.HeadNum:int = obj["HeadNum"]
      self.InvoiceNum:str = obj["InvoiceNum"]
      self.JCDept:str = obj["JCDept"]
      """  JCDept of the related JCDept record.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  MiscCode of the related MiscChrg or PurMisc record.  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum of the related Part record.  """  
      self.PayTypeID:str = obj["PayTypeID"]
      """  PayTypeID of PayType  """  
      self.PerConName:str = obj["PerConName"]
      self.PIStatus:str = obj["PIStatus"]
      """  PI Status  """  
      self.Plant:str = obj["Plant"]
      """  Plant of the related PlantConfCtrl record.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  ProdCode of the related ProdGrup record.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  ProjectID of the related Project record.  """  
      self.PurchCode:str = obj["PurchCode"]
      """  PurchCode of the related GLPurch record.  """  
      self.RateCode:str = obj["RateCode"]
      """  RateCode of the related GLRate record.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  ReasonCode of the related Reason record.  """  
      self.ReasonType:str = obj["ReasonType"]
      """  ReasonType of the related Reason record.  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  SalesCatID of the related SalesCat record.  """  
      self.Shift:int = obj["Shift"]
      """  Shift value of the related JCShift record.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  TaxCode of the related SalesTax record.  """  
      self.TaxTblID:str = obj["TaxTblID"]
      """  TaxTblID of PRTaxMas or PRClsTax.  """  
      self.ToPlant:str = obj["ToPlant"]
      """  ToPlant value of the related PlntTranDef record.  """  
      self.TransferMethod:str = obj["TransferMethod"]
      """  TransferMethod of ExtCompany table  """  
      self.TypeID:str = obj["TypeID"]
      """  Type ID  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum of the related Vendor record.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  WarehouseCode of the related Warehse record.  """  
      self.ExpenseTypeCode:str = obj["ExpenseTypeCode"]
      self.IsFiltered:bool = obj["IsFiltered"]
      self.OprTypeCode:str = obj["OprTypeCode"]
      self.CashDeskID:str = obj["CashDeskID"]
      self.TIN:str = obj["TIN"]
      self.ReclassCodeID:str = obj["ReclassCodeID"]
      self.BitFlag:int = obj["BitFlag"]
      self.GLCntrlDescription:str = obj["GLCntrlDescription"]
      self.GLCntrlTypeDescription:str = obj["GLCntrlTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LegalNumberGenerateRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.NumberType:str = obj["NumberType"]
      self.NumberYear:int = obj["NumberYear"]
      self.NumberPrefix:str = obj["NumberPrefix"]
      """  The legal number prefix  """  
      self.NumberSuffix:str = obj["NumberSuffix"]
      self.PrefixList:str = obj["PrefixList"]
      self.GenerationType:str = obj["GenerationType"]
      self.EnableNumberPrefix:bool = obj["EnableNumberPrefix"]
      self.EnableNumberSuffix:bool = obj["EnableNumberSuffix"]
      self.NumberOption:str = obj["NumberOption"]
      self.LegalNumberNum:int = obj["LegalNumberNum"]
      """  Unique identifier of the Legal Number record  """  
      self.DocumentDate:str = obj["DocumentDate"]
      self.AdditionalParams:str = obj["AdditionalParams"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LogAPInvAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.VendorNum:int = obj["VendorNum"]
      self.InvoiceNum:str = obj["InvoiceNum"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LogAPInvListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead it is assigned from the Vendor.VendorNum using VendorID to find the Vendor record.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Vendor's invoice number.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group that the invoice was associated with  during the data entry process. This field is not directly maintainable, it is assigned by the invoice entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  """  
      self.DebitMemo:bool = obj["DebitMemo"]
      """   Indicates the type of document. Yes = Debit Memo,  No= Invoice. This value can't be changed after the record has been created.
Debit memos affect the way detail quantities and amounts are stored in the database. They will always be stored with a negative sign, but are entered as a positive.
The system uses this field to test for Debit Memos,  indicated by "DM" following the invoice number.  """  
      self.Approved:bool = obj["Approved"]
      """  Yes indicates all necessary approvals have been received.  No indicates approvals are pending.  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  Date the Logged Invoice was approved.  """  
      self.Matched:bool = obj["Matched"]
      """  Yes indicates this logged invoice has been matched to an AP Invoice.  No indicates it has not been matched.  """  
      self.MatchedDate:str = obj["MatchedDate"]
      """  Date the logged invoice was matched to an AP Invoice.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates whether or not this logged invoice has been posted to the GL.  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice date.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Contains the foreign key to the PurTerms master file.  Defaulted from Vendor.TermsCode.  This is MANDATORY ENTRY. User maintainable via a combo-box for terms description.  """  
      self.Void:bool = obj["Void"]
      """  Indicates if this logged invoice has been voided.  """  
      self.VoidedBy:str = obj["VoidedBy"]
      """  User ID that voided the invoice. This is not maintainable by the user.  """  
      self.VoidReason:str = obj["VoidReason"]
      """  Text that explains why the logged invoice was voided.  """  
      self.VoidDate:str = obj["VoidDate"]
      """  Date the Logged Invoice was voided.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Total sales tax amount for this invoice. Totals the TaxAmt from the APInvTax records of this invoice.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Total sales tax amount for this invoice. Totals the DocTaxAmt from the LogAPInvTax records of this invoice.  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.DueDate:str = obj["DueDate"]
      """  The due date of the earliest unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  Apply Date  """  
      self.Description:str = obj["Description"]
      """  A short description that can be used to explain what this invoice is for. Ex: Rent, Auto Lease Payment.  """  
      self.REFPONum:int = obj["REFPONum"]
      """  Reference PO number(optional when CM is present). Used to identify the PO that this Invoice is for.  If the Reference PO has a lock exchange rate then that is the rate that will be used on this AP  invoice,  """  
      self.InvoiceVendorAmt:int = obj["InvoiceVendorAmt"]
      """  For use by external G/L interfacing.  This field is sign flipped for debit memos.  """  
      self.DocInvoiceVendorAmt:int = obj["DocInvoiceVendorAmt"]
      """  A user entered verification amount.  DOCUMENT CURRENCY ONLY, a corresponding base currency field exists but is only used for external G/L interfacing.  This field is sign flipped for debit memos.  The calculated Invoice Amount (DocInvoiceAmt) must match this amount before the invoice can be posted.  """  
      self.Rpt1InvoiceVendorAmt:int = obj["Rpt1InvoiceVendorAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2InvoiceVendorAmt:int = obj["Rpt2InvoiceVendorAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3InvoiceVendorAmt:int = obj["Rpt3InvoiceVendorAmt"]
      """  Reporting currency value of this field  """  
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      """  Total invoice Amount.   This field has a true sign. (debit memos are negative).  """  
      self.DocInvoiceAmt:int = obj["DocInvoiceAmt"]
      """  Total invoice Amount.(Vendors Currency) This field has a true sign. (debit memos are negative).  """  
      self.Rpt1InvoiceAmt:int = obj["Rpt1InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2InvoiceAmt:int = obj["Rpt2InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3InvoiceAmt:int = obj["Rpt3InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Region for this invoice.  """  
      self.TaxPoint:str = obj["TaxPoint"]
      """  Tax Point  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Date Used to calculate Tax Rates  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  User ID that entered the invoice. This is not maintainable by the user.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.AutoApproved:bool = obj["AutoApproved"]
      """   Reserved for future development.
Indicates if the approval process is required.  If yes, an approval code is not required and the invoice is automatically approved.  If no, an approval code is required.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year. This is defaulted based on the finding the Fiscal master for the corresponding InvoiceDate.  User can override this. This value is used as one of the defaults to the InvHead records. (see InvHead for usage).  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  A Fiscal period which provides one of the defaults to be used when creating invoices within this group. This field is defaulted based on finding the Fiscal master which contains the corresponding  InvoiceDate period. (See InvcHead.FiscalPeriod for usage)  """  
      self.Rounding:int = obj["Rounding"]
      """  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  """  
      self.DocRounding:int = obj["DocRounding"]
      """  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  """  
      self.Rpt1Rounding:int = obj["Rpt1Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt2Rounding:int = obj["Rpt2Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt3Rounding:int = obj["Rpt3Rounding"]
      """  Reporting currency value of this field  """  
      self.DiscountDate:str = obj["DiscountDate"]
      """  Reserved for Future Development.  Prompt payment discount due date. The date according to the terms when you are allowed to take the prompt payment discount (if any) given by the vendor. This date is NOT directly maintainable. It is calculated using the InvoiceDate + PurTerms.DiscountDays. If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then this is not applicable and is set to ? (null value).  """  
      self.DiscountAmt:int = obj["DiscountAmt"]
      """  Reserved for Future development. Discount amount that can be taken if paid by the DiscountDate.  This is calculated by the System via APInvHed write trigger. Formula ((PurTerms.DiscountPercent/100)*APInvHed.InvoiceBal on AIn.  If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then it is not applicable and is set to zero.  """  
      self.DocDiscountAmt:int = obj["DocDiscountAmt"]
      """  Reserved for future development. Discount amount(Vendors Currency) that can be taken if paid by the DiscountDate.  This is calculated by the System via APInvHed write trigger. Formula ((PurTerms.DiscountPercent/100)*APInvHed.InvoiceBal on AIn.  If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then it is not applicable and is set to zero.  """  
      self.InvoiceRef:str = obj["InvoiceRef"]
      """   Reserved for future development. This field is maintainable/viewable only for Debit Memos. It represents the invoice # that this debit memo relates to. It can be left blank. If entered it must be a valid APInvHed record where the InvcHead.DebitMemo = No. This field is also used to order the invoices when printing aging reports. The idea is to be able to print the debit memos next to their corresponding invoice. Therefore, this field will always have a value.
For Invoices it is equal to the InvoiceNum.
For Debit memos where they are not related to an invoice it is also set equal to the Debit memo's InvoiceNum. In this later case when InvcHead.DebitMemo = Yes and InvcHead.InvoiceNum = InvcHead.InvoiceRef the InvoiceRef is reset to zero before being displayed, then when written back to the database it is set = to the InvoiceNum if the user did not enter a related invoice.  """  
      self.AuthorizedBy:str = obj["AuthorizedBy"]
      """  User ID that authorized the invoice. This is not maintainable by the user.  """  
      self.Rpt1DiscountAmt:int = obj["Rpt1DiscountAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DiscountAmt:int = obj["Rpt2DiscountAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DiscountAmt:int = obj["Rpt3DiscountAmt"]
      """  Reporting currency value of this field  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.InvExpense:int = obj["InvExpense"]
      """  Invoice Expense Amount. This is the Gross Invoice Amount minus the taxes.  """  
      self.DocInvExpense:int = obj["DocInvExpense"]
      """  Invoice Expense Amount. This is the Gross Invoice Amount minus the taxes.  """  
      self.Rpt1InvExpense:int = obj["Rpt1InvExpense"]
      """  Invoice Expense Amount. This is the Gross Invoice Amount minus the taxes.  """  
      self.Rpt2InvExpense:int = obj["Rpt2InvExpense"]
      """  Invoice Expense Amount. This is the Gross Invoice Amount minus the taxes.  """  
      self.Rpt3InvExpense:int = obj["Rpt3InvExpense"]
      """  Invoice Expense Amount. This is the Gross Invoice Amount minus the taxes.  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the invoice is ready for calculations.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.TaxRateGrpCode:str = obj["TaxRateGrpCode"]
      """  Tax Rate Group Code  """  
      self.LockTaxRate:bool = obj["LockTaxRate"]
      """  Locks Tax Rate and allows user to edit the tax exchange rate  """  
      self.SEBankRef:str = obj["SEBankRef"]
      """  Sweden and Finland Localization Field - Banking Reference  """  
      self.SEPayCode:str = obj["SEPayCode"]
      """  Sweden and Finland Localization Field - Payment Code  """  
      self.SEPMUID:int = obj["SEPMUID"]
      """  Sweden and Finland Localization field, Payment Method code  """  
      self.BankID:str = obj["BankID"]
      """  Unique ID of the vendor's bank.  """  
      self.VoidLegalNumber:str = obj["VoidLegalNumber"]
      """  Legal Number for the voiding.  """  
      self.VoidTranDocTypeID:str = obj["VoidTranDocTypeID"]
      """  Transaction Document Type for the voiding.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type for the record.  """  
      self.CardCode:str = obj["CardCode"]
      """   Denmark Localization
Card (payment) code  """  
      self.BankGiroAcctNbr:str = obj["BankGiroAcctNbr"]
      """   Denmark Localization
Account Number  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TranType:str = obj["TranType"]
      """  TranType  """  
      self.PLInvoiceReference:str = obj["PLInvoiceReference"]
      """  PLInvoiceReference  """  
      self.ScrInvVendorAmt:int = obj["ScrInvVendorAmt"]
      self.MatchInvoicePosted:bool = obj["MatchInvoicePosted"]
      """  When the APInvHed record is created from this logged invoice and the APInvHed record is posted, this flag is set to true.  This is used by the UI.  """  
      self.ScrTotDedTaxAmt:int = obj["ScrTotDedTaxAmt"]
      self.ScrDocTotSelfAmt:int = obj["ScrDocTotSelfAmt"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.Rpt3ScrTotSelfAmt:int = obj["Rpt3ScrTotSelfAmt"]
      self.EnableExchangeRate:bool = obj["EnableExchangeRate"]
      self.EnableLockRate:bool = obj["EnableLockRate"]
      self.XRateLabel:str = obj["XRateLabel"]
      self.VendorInactive:bool = obj["VendorInactive"]
      """  Indicates if the vendor is active  """  
      self.ScrTaxAmt:int = obj["ScrTaxAmt"]
      self.Rpt1ScrTaxAmt:int = obj["Rpt1ScrTaxAmt"]
      self.Rpt2ScrTaxAmt:int = obj["Rpt2ScrTaxAmt"]
      self.Rpt3ScrTaxAmt:int = obj["Rpt3ScrTaxAmt"]
      self.Rpt1ScrInvVendorAmt:int = obj["Rpt1ScrInvVendorAmt"]
      self.Rpt2ScrInvVendorAmt:int = obj["Rpt2ScrInvVendorAmt"]
      self.Rpt3ScrInvVendorAmt:int = obj["Rpt3ScrInvVendorAmt"]
      self.Rpt1ScrInvoiceAmt:int = obj["Rpt1ScrInvoiceAmt"]
      self.Rpt2ScrInvoiceAmt:int = obj["Rpt2ScrInvoiceAmt"]
      self.Rpt3ScrInvoiceAmt:int = obj["Rpt3ScrInvoiceAmt"]
      self.ScrInvoiceAmt:int = obj["ScrInvoiceAmt"]
      self.ScrDocTaxAmt:int = obj["ScrDocTaxAmt"]
      self.ScrDocInvVendorAmt:int = obj["ScrDocInvVendorAmt"]
      self.ScrDocInvoiceAmt:int = obj["ScrDocInvoiceAmt"]
      self.ScrTotTaxableAmt:int = obj["ScrTotTaxableAmt"]
      self.ScrDocTotTaxableAmt:int = obj["ScrDocTotTaxableAmt"]
      self.Rpt1ScrTotTaxableAmt:int = obj["Rpt1ScrTotTaxableAmt"]
      self.Rpt2ScrTotTaxableAmt:int = obj["Rpt2ScrTotTaxableAmt"]
      self.Rpt3ScrTotTaxableAmt:int = obj["Rpt3ScrTotTaxableAmt"]
      self.ScrTotReportableAmt:int = obj["ScrTotReportableAmt"]
      self.ScrDocTotReportableAmt:int = obj["ScrDocTotReportableAmt"]
      self.Rpt1ScrTotReportableAmt:int = obj["Rpt1ScrTotReportableAmt"]
      self.Rpt2ScrTotReportableAmt:int = obj["Rpt2ScrTotReportableAmt"]
      self.Rpt3ScrTotReportableAmt:int = obj["Rpt3ScrTotReportableAmt"]
      self.ScrDocTotDedTaxAmt:int = obj["ScrDocTotDedTaxAmt"]
      self.Rpt1ScrTotDedTaxAmt:int = obj["Rpt1ScrTotDedTaxAmt"]
      self.Rpt2ScrTotDedTaxAmt:int = obj["Rpt2ScrTotDedTaxAmt"]
      self.Rpt3ScrTotDedTaxAmt:int = obj["Rpt3ScrTotDedTaxAmt"]
      self.ScrTotWithholdingAmt:int = obj["ScrTotWithholdingAmt"]
      self.ScrDocTotWithholdingAmt:int = obj["ScrDocTotWithholdingAmt"]
      self.Rpt1ScrTotWithholdingAmt:int = obj["Rpt1ScrTotWithholdingAmt"]
      self.Rpt2ScrTotWithholdingAmt:int = obj["Rpt2ScrTotWithholdingAmt"]
      self.Rpt3ScrTotWithholdingAmt:int = obj["Rpt3ScrTotWithholdingAmt"]
      self.ScrTotSelfAmt:int = obj["ScrTotSelfAmt"]
      self.Rpt1ScrTotSelfAmt:int = obj["Rpt1ScrTotSelfAmt"]
      self.Rpt2ScrTotSelfAmt:int = obj["Rpt2ScrTotSelfAmt"]
      self.ScrDocRounding:int = obj["ScrDocRounding"]
      self.Rpt2ScrRounding:int = obj["Rpt2ScrRounding"]
      self.Rpt3ScrRounding:int = obj["Rpt3ScrRounding"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.TaxLinesExist:bool = obj["TaxLinesExist"]
      self.EnableDueDate:bool = obj["EnableDueDate"]
      self.InvoiceVariance:int = obj["InvoiceVariance"]
      self.Rpt1InvoiceVariance:int = obj["Rpt1InvoiceVariance"]
      self.Rpt2InvoiceVariance:int = obj["Rpt2InvoiceVariance"]
      self.Rpt3InvoiceVariance:int = obj["Rpt3InvoiceVariance"]
      self.BillAddressList:str = obj["BillAddressList"]
      self.ScrRounding:int = obj["ScrRounding"]
      self.DocInvoiceVariance:int = obj["DocInvoiceVariance"]
      self.Rpt1ScrRounding:int = obj["Rpt1ScrRounding"]
      self.TotalInvAmt:int = obj["TotalInvAmt"]
      self.ScrDiscountAmt:int = obj["ScrDiscountAmt"]
      self.ScrDocDiscountAmt:int = obj["ScrDocDiscountAmt"]
      self.ScrInvoiceRef:str = obj["ScrInvoiceRef"]
      self.ScrTotInvoiceAmt:int = obj["ScrTotInvoiceAmt"]
      self.ScrDocTotInvoiceAmt:int = obj["ScrDocTotInvoiceAmt"]
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.AuthAdmins:str = obj["AuthAdmins"]
      """  Intended for internal use  """  
      self.AuthAdminNames:str = obj["AuthAdminNames"]
      """  Intended for Internal Use  """  
      self.EnableTaxesInTracker:bool = obj["EnableTaxesInTracker"]
      """  Logical indicating whether or not the Logged Invoice Tracker is to enable the GL Transaction Tb  """  
      self.Rpt1ScrDocInvoiceAmt:int = obj["Rpt1ScrDocInvoiceAmt"]
      self.Rpt2ScrDocInvoiceAmt:int = obj["Rpt2ScrDocInvoiceAmt"]
      self.Rpt3ScrDocInvoiceAmt:int = obj["Rpt3ScrDocInvoiceAmt"]
      self.UpdateEntity:bool = obj["UpdateEntity"]
      """  Not intended for external use.  Logical indicating that a default entity was created for the new logged invoice.  """  
      self.Rpt2ScrTotInvoiceAmt:int = obj["Rpt2ScrTotInvoiceAmt"]
      self.Rpt3ScrTotInvoiceAmt:int = obj["Rpt3ScrTotInvoiceAmt"]
      self.Rpt1ScrTotInvoiceAmt:int = obj["Rpt1ScrTotInvoiceAmt"]
      self.IsEligibleToVoid:bool = obj["IsEligibleToVoid"]
      """  Not intended for external use.  Indicates if the user has Void authority.  """  
      self.ScrInvExpense:int = obj["ScrInvExpense"]
      self.ScrDocInvExpense:int = obj["ScrDocInvExpense"]
      self.Rpt2ScrInvExpense:int = obj["Rpt2ScrInvExpense"]
      self.Rpt3ScrInvExpense:int = obj["Rpt3ScrInvExpense"]
      self.Rpt1ScrInvExpense:int = obj["Rpt1ScrInvExpense"]
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.TransApplyDate:str = obj["TransApplyDate"]
      """  This field is used when invoice is transferred form one Group to another and the user has a cance to change this invoice Apply Date.  """  
      self.DocDspInvVendorAmt:int = obj["DocDspInvVendorAmt"]
      """  Document Invoice Vendor Amout only for dispaly  """  
      self.DspInvVendorAmt:int = obj["DspInvVendorAmt"]
      """  DspInvVendorAmt  """  
      self.Rpt1DspInvVendorAmt:int = obj["Rpt1DspInvVendorAmt"]
      """  Invoice Vendor Amout only for dispaly in report currency  """  
      self.Rpt2DspInvVendorAmt:int = obj["Rpt2DspInvVendorAmt"]
      """  Invoice Vendor Amout only for dispaly in report currency  """  
      self.Rpt3DspInvVendorAmt:int = obj["Rpt3DspInvVendorAmt"]
      """  Invoice Vendor Amout only for dispaly in report currency  """  
      self.EnableTaxLock:bool = obj["EnableTaxLock"]
      self.UseTaxRate:bool = obj["UseTaxRate"]
      self.TaxExchangeRate:int = obj["TaxExchangeRate"]
      self.EnableTaxExRate:bool = obj["EnableTaxExRate"]
      self.TaxRateLinesExist:bool = obj["TaxRateLinesExist"]
      self.PayMethod:str = obj["PayMethod"]
      """  Pay Method Type  """  
      self.VendorBank:str = obj["VendorBank"]
      """  Vendor Bank  """  
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.RateGrpCodeDescription:str = obj["RateGrpCodeDescription"]
      """  Description  """  
      self.SEPayMethodType:int = obj["SEPayMethodType"]
      """  Indicated the type of payment with the following options:
 0 = Manual (default)
 1 = Electronic Interface
 2 = Check Printing
 3 = Payment Instrument Type 1
 4 = Payment Instrument Type 2  """  
      self.SEPayMethodName:str = obj["SEPayMethodName"]
      """  Name of the payment method  """  
      self.SEPayMethodSummarizePerCustomer:bool = obj["SEPayMethodSummarizePerCustomer"]
      """   Indicates that invoices for the customer is summarized and sent as a sum to the bank without specifying the individual invoices.
A single bank transaction is created for the payment but what?s actually sent to the bank will be determined by the electronic interface plug-in program.
Only enabled if type is set to ?Electronic Interface?  """  
      self.TaxRateGrpDescription:str = obj["TaxRateGrpDescription"]
      """  Description  """  
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      """  Full description for the Tax Region.  """  
      self.TermsCodeDescription:str = obj["TermsCodeDescription"]
      """  Full description of terms....this is printed on purchase orders. Can't be blank.  """  
      self.UserfileName:str = obj["UserfileName"]
      """  User Name  """  
      self.VendBankSwiftNum:str = obj["VendBankSwiftNum"]
      """  Swift number of the bank.  """  
      self.VendBankIBANCode:str = obj["VendBankIBANCode"]
      """  IBAN Code of the Supplier Bank  """  
      self.VendBankBankGiroAcctNbr:str = obj["VendBankBankGiroAcctNbr"]
      """   Denmark Localization          
Account Number  """  
      self.VendBankLocalBIC:str = obj["VendBankLocalBIC"]
      """  Local BIC of the Supplier Bank  """  
      self.VendBankBankAcctNumber:str = obj["VendBankBankAcctNumber"]
      """  The Bank account number for the Vendor.  Used with Electronic payments.  """  
      self.VendBankBankName:str = obj["VendBankBankName"]
      """  Supplier Bank Name  """  
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      """  Second address line of the Supplier  """  
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorNumState:str = obj["VendorNumState"]
      """  Can be blank.  """  
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.VoidedByName:str = obj["VoidedByName"]
      """  User Name  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LogAPInvRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead it is assigned from the Vendor.VendorNum using VendorID to find the Vendor record.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Vendor's invoice number.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group that the invoice was associated with  during the data entry process. This field is not directly maintainable, it is assigned by the invoice entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  """  
      self.DebitMemo:bool = obj["DebitMemo"]
      """   Indicates the type of document. Yes = Debit Memo,  No= Invoice. This value can't be changed after the record has been created.
Debit memos affect the way detail quantities and amounts are stored in the database. They will always be stored with a negative sign, but are entered as a positive.
The system uses this field to test for Debit Memos,  indicated by "DM" following the invoice number.  """  
      self.Approved:bool = obj["Approved"]
      """  Yes indicates all necessary approvals have been received.  No indicates approvals are pending.  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  Date the Logged Invoice was approved.  """  
      self.Matched:bool = obj["Matched"]
      """  Yes indicates this logged invoice has been matched to an AP Invoice.  No indicates it has not been matched.  """  
      self.MatchedDate:str = obj["MatchedDate"]
      """  Date the logged invoice was matched to an AP Invoice.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates whether or not this logged invoice has been posted to the GL.  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice date.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Contains the foreign key to the PurTerms master file.  Defaulted from Vendor.TermsCode.  This is MANDATORY ENTRY. User maintainable via a combo-box for terms description.  """  
      self.Void:bool = obj["Void"]
      """  Indicates if this logged invoice has been voided.  """  
      self.VoidedBy:str = obj["VoidedBy"]
      """  User ID that voided the invoice. This is not maintainable by the user.  """  
      self.VoidReason:str = obj["VoidReason"]
      """  Text that explains why the logged invoice was voided.  """  
      self.VoidDate:str = obj["VoidDate"]
      """  Date the Logged Invoice was voided.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Total sales tax amount for this invoice. Totals the TaxAmt from the APInvTax records of this invoice.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Total sales tax amount for this invoice. Totals the DocTaxAmt from the LogAPInvTax records of this invoice.  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.DueDate:str = obj["DueDate"]
      """  The due date of the earliest unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  Apply Date  """  
      self.Description:str = obj["Description"]
      """  A short description that can be used to explain what this invoice is for. Ex: Rent, Auto Lease Payment.  """  
      self.REFPONum:int = obj["REFPONum"]
      """  Reference PO number(optional when CM is present). Used to identify the PO that this Invoice is for.  If the Reference PO has a lock exchange rate then that is the rate that will be used on this AP  invoice,  """  
      self.InvoiceVendorAmt:int = obj["InvoiceVendorAmt"]
      """  For use by external G/L interfacing.  This field is sign flipped for debit memos.  """  
      self.DocInvoiceVendorAmt:int = obj["DocInvoiceVendorAmt"]
      """  A user entered verification amount.  DOCUMENT CURRENCY ONLY, a corresponding base currency field exists but is only used for external G/L interfacing.  This field is sign flipped for debit memos.  The calculated Invoice Amount (DocInvoiceAmt) must match this amount before the invoice can be posted.  """  
      self.Rpt1InvoiceVendorAmt:int = obj["Rpt1InvoiceVendorAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2InvoiceVendorAmt:int = obj["Rpt2InvoiceVendorAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3InvoiceVendorAmt:int = obj["Rpt3InvoiceVendorAmt"]
      """  Reporting currency value of this field  """  
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      """  Total invoice Amount.   This field has a true sign. (debit memos are negative).  """  
      self.DocInvoiceAmt:int = obj["DocInvoiceAmt"]
      """  Total invoice Amount.(Vendors Currency) This field has a true sign. (debit memos are negative).  """  
      self.Rpt1InvoiceAmt:int = obj["Rpt1InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2InvoiceAmt:int = obj["Rpt2InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3InvoiceAmt:int = obj["Rpt3InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Region for this invoice.  """  
      self.TaxPoint:str = obj["TaxPoint"]
      """  Tax Point  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Date Used to calculate Tax Rates  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  User ID that entered the invoice. This is not maintainable by the user.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.AutoApproved:bool = obj["AutoApproved"]
      """   Reserved for future development.
Indicates if the approval process is required.  If yes, an approval code is not required and the invoice is automatically approved.  If no, an approval code is required.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year. This is defaulted based on the finding the Fiscal master for the corresponding InvoiceDate.  User can override this. This value is used as one of the defaults to the InvHead records. (see InvHead for usage).  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  A Fiscal period which provides one of the defaults to be used when creating invoices within this group. This field is defaulted based on finding the Fiscal master which contains the corresponding  InvoiceDate period. (See InvcHead.FiscalPeriod for usage)  """  
      self.Rounding:int = obj["Rounding"]
      """  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  """  
      self.DocRounding:int = obj["DocRounding"]
      """  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  """  
      self.Rpt1Rounding:int = obj["Rpt1Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt2Rounding:int = obj["Rpt2Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt3Rounding:int = obj["Rpt3Rounding"]
      """  Reporting currency value of this field  """  
      self.DiscountDate:str = obj["DiscountDate"]
      """  Reserved for Future Development.  Prompt payment discount due date. The date according to the terms when you are allowed to take the prompt payment discount (if any) given by the vendor. This date is NOT directly maintainable. It is calculated using the InvoiceDate + PurTerms.DiscountDays. If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then this is not applicable and is set to ? (null value).  """  
      self.DiscountAmt:int = obj["DiscountAmt"]
      """  Reserved for Future development. Discount amount that can be taken if paid by the DiscountDate.  This is calculated by the System via APInvHed write trigger. Formula ((PurTerms.DiscountPercent/100)*APInvHed.InvoiceBal on AIn.  If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then it is not applicable and is set to zero.  """  
      self.DocDiscountAmt:int = obj["DocDiscountAmt"]
      """  Reserved for future development. Discount amount(Vendors Currency) that can be taken if paid by the DiscountDate.  This is calculated by the System via APInvHed write trigger. Formula ((PurTerms.DiscountPercent/100)*APInvHed.InvoiceBal on AIn.  If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then it is not applicable and is set to zero.  """  
      self.InvoiceRef:str = obj["InvoiceRef"]
      """   Reserved for future development. This field is maintainable/viewable only for Debit Memos. It represents the invoice # that this debit memo relates to. It can be left blank. If entered it must be a valid APInvHed record where the InvcHead.DebitMemo = No. This field is also used to order the invoices when printing aging reports. The idea is to be able to print the debit memos next to their corresponding invoice. Therefore, this field will always have a value.
For Invoices it is equal to the InvoiceNum.
For Debit memos where they are not related to an invoice it is also set equal to the Debit memo's InvoiceNum. In this later case when InvcHead.DebitMemo = Yes and InvcHead.InvoiceNum = InvcHead.InvoiceRef the InvoiceRef is reset to zero before being displayed, then when written back to the database it is set = to the InvoiceNum if the user did not enter a related invoice.  """  
      self.AuthorizedBy:str = obj["AuthorizedBy"]
      """  User ID that authorized the invoice. This is not maintainable by the user.  """  
      self.Rpt1DiscountAmt:int = obj["Rpt1DiscountAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DiscountAmt:int = obj["Rpt2DiscountAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DiscountAmt:int = obj["Rpt3DiscountAmt"]
      """  Reporting currency value of this field  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.InvExpense:int = obj["InvExpense"]
      """  Invoice Expense Amount. This is the Gross Invoice Amount minus the taxes.  """  
      self.DocInvExpense:int = obj["DocInvExpense"]
      """  Invoice Expense Amount. This is the Gross Invoice Amount minus the taxes.  """  
      self.Rpt1InvExpense:int = obj["Rpt1InvExpense"]
      """  Invoice Expense Amount. This is the Gross Invoice Amount minus the taxes.  """  
      self.Rpt2InvExpense:int = obj["Rpt2InvExpense"]
      """  Invoice Expense Amount. This is the Gross Invoice Amount minus the taxes.  """  
      self.Rpt3InvExpense:int = obj["Rpt3InvExpense"]
      """  Invoice Expense Amount. This is the Gross Invoice Amount minus the taxes.  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the invoice is ready for calculations.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.TaxRateGrpCode:str = obj["TaxRateGrpCode"]
      """  Tax Rate Group Code  """  
      self.LockTaxRate:bool = obj["LockTaxRate"]
      """  Locks Tax Rate and allows user to edit the tax exchange rate  """  
      self.SEBankRef:str = obj["SEBankRef"]
      """  Sweden and Finland Localization Field - Banking Reference  """  
      self.SEPayCode:str = obj["SEPayCode"]
      """  Sweden and Finland Localization Field - Payment Code  """  
      self.SEPMUID:int = obj["SEPMUID"]
      """  Sweden and Finland Localization field, Payment Method code  """  
      self.BankID:str = obj["BankID"]
      """  Unique ID of the vendor's bank.  """  
      self.VoidLegalNumber:str = obj["VoidLegalNumber"]
      """  Legal Number for the voiding.  """  
      self.VoidTranDocTypeID:str = obj["VoidTranDocTypeID"]
      """  Transaction Document Type for the voiding.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type for the record.  """  
      self.CardCode:str = obj["CardCode"]
      """   Denmark Localization
Card (payment) code  """  
      self.BankGiroAcctNbr:str = obj["BankGiroAcctNbr"]
      """   Denmark Localization
Account Number  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CHISRCodeLine:str = obj["CHISRCodeLine"]
      """  CHISRCodeLine  """  
      self.CustomsNumber:str = obj["CustomsNumber"]
      """  CustomsNumber  """  
      self.ReceivedDate:str = obj["ReceivedDate"]
      """  ReceivedDate  """  
      self.TranType:str = obj["TranType"]
      """  TranType  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID.  """  
      self.PLInvoiceReference:str = obj["PLInvoiceReference"]
      """  PLInvoiceReference  """  
      self.VoidDescription:str = obj["VoidDescription"]
      """  VoidDescription  """  
      self.APTaxRoundOption:int = obj["APTaxRoundOption"]
      """  APTaxRoundOption  """  
      self.AuthAdminNames:str = obj["AuthAdminNames"]
      """  Intended for Internal Use  """  
      self.AuthAdmins:str = obj["AuthAdmins"]
      """  Intended for internal use  """  
      self.BankName:str = obj["BankName"]
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.BillAddressList:str = obj["BillAddressList"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.DocDspInvVendorAmt:int = obj["DocDspInvVendorAmt"]
      """  Document Invoice Vendor Amout only for dispaly  """  
      self.DocInvoiceVariance:int = obj["DocInvoiceVariance"]
      self.DspInvVendorAmt:int = obj["DspInvVendorAmt"]
      """  DspInvVendorAmt  """  
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      self.EnableDueDate:bool = obj["EnableDueDate"]
      self.EnableExchangeRate:bool = obj["EnableExchangeRate"]
      self.EnableLockRate:bool = obj["EnableLockRate"]
      self.EnableTaxesInTracker:bool = obj["EnableTaxesInTracker"]
      """  Logical indicating whether or not the Logged Invoice Tracker is to enable the GL Transaction Tb  """  
      self.EnableTaxExRate:bool = obj["EnableTaxExRate"]
      self.EnableTaxLock:bool = obj["EnableTaxLock"]
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      """  Enable setting of Transaction Document Type  """  
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      self.InvoiceVariance:int = obj["InvoiceVariance"]
      self.IsDiscountforDebitM:bool = obj["IsDiscountforDebitM"]
      self.IsEligibleToVoid:bool = obj["IsEligibleToVoid"]
      """  Not intended for external use.  Indicates if the user has Void authority.  """  
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.MatchInvoicePosted:bool = obj["MatchInvoicePosted"]
      """  When the APInvHed record is created from this logged invoice and the APInvHed record is posted, this flag is set to true.  This is used by the UI.  """  
      self.PayMethod:str = obj["PayMethod"]
      """  Pay Method Type  """  
      self.PLVendorAutoInvoiceNum:bool = obj["PLVendorAutoInvoiceNum"]
      """  CSF Poland. Vendor uses Invoice reference number  """  
      self.Rpt1DspInvVendorAmt:int = obj["Rpt1DspInvVendorAmt"]
      """  Invoice Vendor Amout only for dispaly in report currency  """  
      self.Rpt1InvoiceVariance:int = obj["Rpt1InvoiceVariance"]
      self.Rpt1ScrDocInvoiceAmt:int = obj["Rpt1ScrDocInvoiceAmt"]
      self.Rpt1ScrInvExpense:int = obj["Rpt1ScrInvExpense"]
      self.Rpt1ScrInvoiceAmt:int = obj["Rpt1ScrInvoiceAmt"]
      self.Rpt1ScrInvVendorAmt:int = obj["Rpt1ScrInvVendorAmt"]
      self.Rpt1ScrRounding:int = obj["Rpt1ScrRounding"]
      self.Rpt1ScrTaxAmt:int = obj["Rpt1ScrTaxAmt"]
      self.Rpt1ScrTotDedTaxAmt:int = obj["Rpt1ScrTotDedTaxAmt"]
      self.Rpt1ScrTotInvoiceAmt:int = obj["Rpt1ScrTotInvoiceAmt"]
      self.Rpt1ScrTotReportableAmt:int = obj["Rpt1ScrTotReportableAmt"]
      self.Rpt1ScrTotSelfAmt:int = obj["Rpt1ScrTotSelfAmt"]
      self.Rpt1ScrTotTaxableAmt:int = obj["Rpt1ScrTotTaxableAmt"]
      self.Rpt1ScrTotWithholdingAmt:int = obj["Rpt1ScrTotWithholdingAmt"]
      self.Rpt2DspInvVendorAmt:int = obj["Rpt2DspInvVendorAmt"]
      """  Invoice Vendor Amout only for dispaly in report currency  """  
      self.Rpt2InvoiceVariance:int = obj["Rpt2InvoiceVariance"]
      self.Rpt2ScrDocInvoiceAmt:int = obj["Rpt2ScrDocInvoiceAmt"]
      self.Rpt2ScrInvExpense:int = obj["Rpt2ScrInvExpense"]
      self.Rpt2ScrInvoiceAmt:int = obj["Rpt2ScrInvoiceAmt"]
      self.Rpt2ScrInvVendorAmt:int = obj["Rpt2ScrInvVendorAmt"]
      self.Rpt2ScrRounding:int = obj["Rpt2ScrRounding"]
      self.Rpt2ScrTaxAmt:int = obj["Rpt2ScrTaxAmt"]
      self.Rpt2ScrTotDedTaxAmt:int = obj["Rpt2ScrTotDedTaxAmt"]
      self.Rpt2ScrTotInvoiceAmt:int = obj["Rpt2ScrTotInvoiceAmt"]
      self.Rpt2ScrTotReportableAmt:int = obj["Rpt2ScrTotReportableAmt"]
      self.Rpt2ScrTotSelfAmt:int = obj["Rpt2ScrTotSelfAmt"]
      self.Rpt2ScrTotTaxableAmt:int = obj["Rpt2ScrTotTaxableAmt"]
      self.Rpt2ScrTotWithholdingAmt:int = obj["Rpt2ScrTotWithholdingAmt"]
      self.Rpt3DspInvVendorAmt:int = obj["Rpt3DspInvVendorAmt"]
      """  Invoice Vendor Amout only for dispaly in report currency  """  
      self.Rpt3InvoiceVariance:int = obj["Rpt3InvoiceVariance"]
      self.Rpt3ScrDocInvoiceAmt:int = obj["Rpt3ScrDocInvoiceAmt"]
      self.Rpt3ScrInvExpense:int = obj["Rpt3ScrInvExpense"]
      self.Rpt3ScrInvoiceAmt:int = obj["Rpt3ScrInvoiceAmt"]
      self.Rpt3ScrInvVendorAmt:int = obj["Rpt3ScrInvVendorAmt"]
      self.Rpt3ScrRounding:int = obj["Rpt3ScrRounding"]
      self.Rpt3ScrTaxAmt:int = obj["Rpt3ScrTaxAmt"]
      self.Rpt3ScrTotDedTaxAmt:int = obj["Rpt3ScrTotDedTaxAmt"]
      self.Rpt3ScrTotInvoiceAmt:int = obj["Rpt3ScrTotInvoiceAmt"]
      self.Rpt3ScrTotReportableAmt:int = obj["Rpt3ScrTotReportableAmt"]
      self.Rpt3ScrTotSelfAmt:int = obj["Rpt3ScrTotSelfAmt"]
      self.Rpt3ScrTotTaxableAmt:int = obj["Rpt3ScrTotTaxableAmt"]
      self.Rpt3ScrTotWithholdingAmt:int = obj["Rpt3ScrTotWithholdingAmt"]
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.ScrDiscountAmt:int = obj["ScrDiscountAmt"]
      self.ScrDocDiscountAmt:int = obj["ScrDocDiscountAmt"]
      self.ScrDocInvExpense:int = obj["ScrDocInvExpense"]
      self.ScrDocInvoiceAmt:int = obj["ScrDocInvoiceAmt"]
      self.ScrDocInvVendorAmt:int = obj["ScrDocInvVendorAmt"]
      self.ScrDocRounding:int = obj["ScrDocRounding"]
      self.ScrDocTaxAmt:int = obj["ScrDocTaxAmt"]
      self.ScrDocTotDedTaxAmt:int = obj["ScrDocTotDedTaxAmt"]
      self.ScrDocTotInvoiceAmt:int = obj["ScrDocTotInvoiceAmt"]
      self.ScrDocTotReportableAmt:int = obj["ScrDocTotReportableAmt"]
      self.ScrDocTotSelfAmt:int = obj["ScrDocTotSelfAmt"]
      self.ScrDocTotTaxableAmt:int = obj["ScrDocTotTaxableAmt"]
      self.ScrDocTotWithholdingAmt:int = obj["ScrDocTotWithholdingAmt"]
      self.ScrInvExpense:int = obj["ScrInvExpense"]
      self.ScrInvoiceAmt:int = obj["ScrInvoiceAmt"]
      self.ScrInvoiceRef:str = obj["ScrInvoiceRef"]
      self.ScrInvVendorAmt:int = obj["ScrInvVendorAmt"]
      self.ScrRounding:int = obj["ScrRounding"]
      self.ScrTaxAmt:int = obj["ScrTaxAmt"]
      self.ScrTotDedTaxAmt:int = obj["ScrTotDedTaxAmt"]
      self.ScrTotInvoiceAmt:int = obj["ScrTotInvoiceAmt"]
      self.ScrTotReportableAmt:int = obj["ScrTotReportableAmt"]
      self.ScrTotSelfAmt:int = obj["ScrTotSelfAmt"]
      self.ScrTotTaxableAmt:int = obj["ScrTotTaxableAmt"]
      self.ScrTotWithholdingAmt:int = obj["ScrTotWithholdingAmt"]
      self.SystemTranType:str = obj["SystemTranType"]
      """  System Transaction Type: APInvoice/DebitMemo is used in the filter of TranDocType combo box.  """  
      self.TaxExchangeRate:int = obj["TaxExchangeRate"]
      self.TaxLinesExist:bool = obj["TaxLinesExist"]
      self.TaxRateLinesExist:bool = obj["TaxRateLinesExist"]
      self.TotalInvAmt:int = obj["TotalInvAmt"]
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      """  Link to TranDocType table, can be removed when path field TranDocTypeID is replaced with actual one.  """  
      self.TransApplyDate:str = obj["TransApplyDate"]
      """  This field is used when invoice is transferred form one Group to another and the user has a cance to change this invoice Apply Date.  """  
      self.UpdateEntity:bool = obj["UpdateEntity"]
      """  Not intended for external use.  Logical indicating that a default entity was created for the new logged invoice.  """  
      self.UseTaxRate:bool = obj["UseTaxRate"]
      self.VendorBank:str = obj["VendorBank"]
      """  Vendor Bank  """  
      self.VendorInactive:bool = obj["VendorInactive"]
      """  Indicates if the vendor is active  """  
      self.XRateLabel:str = obj["XRateLabel"]
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      self.FormattedVendorNameAddress:str = obj["FormattedVendorNameAddress"]
      """  Formatted Supplier Name and Address  """  
      self.ManualTaxAdj:bool = obj["ManualTaxAdj"]
      """  The flag t to indicate if Tax records created per Tax Liability assigned toLogged Invoiceare adjusted, deleted,  or any tax records were added by the user  """  
      self.VendorNumFullAddress:str = obj["VendorNumFullAddress"]
      """  Supplier Full Address. External field uses the Supplier Address1, Address2, Address3, City,State, zip  and  Country from the supplier catalog  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.PurPointName:str = obj["PurPointName"]
      self.PurPointPrimPCon:int = obj["PurPointPrimPCon"]
      self.PurPointAddress1:str = obj["PurPointAddress1"]
      self.PurPointState:str = obj["PurPointState"]
      self.PurPointAddress2:str = obj["PurPointAddress2"]
      self.PurPointAddress3:str = obj["PurPointAddress3"]
      self.PurPointZip:str = obj["PurPointZip"]
      self.PurPointCountry:str = obj["PurPointCountry"]
      self.PurPointCity:str = obj["PurPointCity"]
      self.RateGrpCodeDescription:str = obj["RateGrpCodeDescription"]
      self.SEPayMethodName:str = obj["SEPayMethodName"]
      self.SEPayMethodType:int = obj["SEPayMethodType"]
      self.SEPayMethodSummarizePerCustomer:bool = obj["SEPayMethodSummarizePerCustomer"]
      self.TaxRateGrpDescription:str = obj["TaxRateGrpDescription"]
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      self.TermsCodeDescription:str = obj["TermsCodeDescription"]
      self.UserfileName:str = obj["UserfileName"]
      self.VendBankSwiftNum:str = obj["VendBankSwiftNum"]
      self.VendBankBankName:str = obj["VendBankBankName"]
      self.VendBankBankGiroAcctNbr:str = obj["VendBankBankGiroAcctNbr"]
      self.VendBankIBANCode:str = obj["VendBankIBANCode"]
      self.VendBankBankAcctNumber:str = obj["VendBankBankAcctNumber"]
      self.VendBankPMUID:int = obj["VendBankPMUID"]
      self.VendBankCardCode:str = obj["VendBankCardCode"]
      self.VendBankLocalBIC:str = obj["VendBankLocalBIC"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VoidedByName:str = obj["VoidedByName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LogAPInvTaxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead it is assigned from the Vendor.VendorNum using VendorID to find the Vendor record.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Vendor's invoice number.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.ECAcquisitionSeq:int = obj["ECAcquisitionSeq"]
      """   Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.
NOTE:  This field is now used in VAT Reverse Charge logic.  If an invoice line is marked for Reverse Charge, a second line is created just like in the ECAcquisition logic. To distinguish the two scenarios, the ReverseCharge flag will be set to true if the second line is for Reverse Charge.  """  
      self.RateCode:str = obj["RateCode"]
      """  Rate Code  """  
      self.Void:bool = obj["Void"]
      """  Indicates if this logged invoice has been voided.  """  
      self.ReverseCharge:bool = obj["ReverseCharge"]
      """  Indicates if this tax line is for a Reverse Charge.  """  
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  Taxable amount for this invoice.  Manually entered if APInvTax.Manual = Yes else set equal to SysCalcTaxableAmt.  """  
      self.DocTaxableAmt:int = obj["DocTaxableAmt"]
      """  Taxable amount for this invoice in foreign currency. Manually entered if APInvTax.Manual = Yes else it is set equal to SysCalcDocTaxableAmt.  """  
      self.Rpt1TaxableAmt:int = obj["Rpt1TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxableAmt:int = obj["Rpt2TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxableAmt:int = obj["Rpt3TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Percent:int = obj["Percent"]
      """  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """   Sales Tax amount for the corresponding taxable sales amount.
Manually entered if APInvTax.Manual = Yes.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount in foreign currency.  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.ReportableAmt:int = obj["ReportableAmt"]
      """  The reportable sales amount to the tax jurisdiction. Set the value as follows; first determine if the item needs to be reported to the tax jurisdiction.  This is done by using the  APInvDtl.TaxCode and APInvDtl/APInvMisc.TaxCat to find a record in the SalesTxC. If a record is not found or SalesTxC.Reportable = Yes then add in the line item extended amount or if this is for a InvcMisc record InvcMisc.Amount. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcReportableAmt.  """  
      self.DocReportableAmt:int = obj["DocReportableAmt"]
      """  The reportable sales amount to the tax jurisdiction expressed in the Vendor's currency. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcDocTaxableAmt.  """  
      self.Rpt1ReportableAmt:int = obj["Rpt1ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2ReportableAmt:int = obj["Rpt2ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3ReportableAmt:int = obj["Rpt3ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Manual:bool = obj["Manual"]
      """  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  """  
      self.SysCalcTaxableAmt:int = obj["SysCalcTaxableAmt"]
      """  System calculated Taxable amount for this invoice.  """  
      self.SysCalcDocTaxableAmt:int = obj["SysCalcDocTaxableAmt"]
      """  System calculated Taxable amount for this invoice in foreign currency.  """  
      self.Rpt1SysCalcTaxableAmt:int = obj["Rpt1SysCalcTaxableAmt"]
      """  System calculated Taxable amount for this invoice.  """  
      self.Rpt2SysCalcTaxableAmt:int = obj["Rpt2SysCalcTaxableAmt"]
      """  System calculated Taxable amount for this invoice.  """  
      self.Rpt3SysCalcTaxableAmt:int = obj["Rpt3SysCalcTaxableAmt"]
      """  System calculated Taxable amount for this invoice.  """  
      self.SysCalcReportableAmt:int = obj["SysCalcReportableAmt"]
      """  System calculated reportable sales amount to the tax jurisdiction. Set the value as follows; first determine if the item needs to be reported to the tax jurisdiction.  This is done by using the  APInvDtl.TaxCode and APInvDtl/APInvMisc.TaxCat to find a record in the SalesTxC. If a record is not found or SalesTxC.Reportable = Yes then add in the line item extended amount or if this is for a InvcMisc record InvcMisc.Amount.  """  
      self.SysCalcDocReportableAmt:int = obj["SysCalcDocReportableAmt"]
      """  System calculated reportable sales amount to the tax jurisdiction expressed in the Vendor's currency.  """  
      self.Rpt1SysCalcReportableAmt:int = obj["Rpt1SysCalcReportableAmt"]
      """  System calculated reportable sales amount to the tax jurisdiction. Set the value as follows; first determine if the item needs to be reported to the tax jurisdiction.  This is done by using the  APInvDtl.TaxCode and APInvDtl/APInvMisc.TaxCat to find a record in the SalesTxC. If a record is not found or SalesTxC.Reportable = Yes then add in the line item extended amount or if this is for a InvcMisc record InvcMisc.Amount.  """  
      self.Rpt2SysCalcReportableAmt:int = obj["Rpt2SysCalcReportableAmt"]
      """  System calculated reportable sales amount to the tax jurisdiction. Set the value as follows; first determine if the item needs to be reported to the tax jurisdiction.  This is done by using the  APInvDtl.TaxCode and APInvDtl/APInvMisc.TaxCat to find a record in the SalesTxC. If a record is not found or SalesTxC.Reportable = Yes then add in the line item extended amount or if this is for a InvcMisc record InvcMisc.Amount.  """  
      self.Rpt3SysCalcReportableAmt:int = obj["Rpt3SysCalcReportableAmt"]
      """  System calculated reportable sales amount to the tax jurisdiction. Set the value as follows; first determine if the item needs to be reported to the tax jurisdiction.  This is done by using the  APInvDtl.TaxCode and APInvDtl/APInvMisc.TaxCat to find a record in the SalesTxC. If a record is not found or SalesTxC.Reportable = Yes then add in the line item extended amount or if this is for a InvcMisc record InvcMisc.Amount.  """  
      self.CollectionType:int = obj["CollectionType"]
      """  Collection Type  """  
      self.Timing:int = obj["Timing"]
      """  Timing of when to report taxes  """  
      self.ExemptType:int = obj["ExemptType"]
      """  Exemption Type  """  
      self.ExemptPercent:int = obj["ExemptPercent"]
      """  Exemption Percent  """  
      self.ResolutionNum:str = obj["ResolutionNum"]
      """  Resolution number  """  
      self.ResolutionDate:str = obj["ResolutionDate"]
      """  Resolution Date  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Tax Rate Date  """  
      self.DefTaxableAmt:int = obj["DefTaxableAmt"]
      """  Balance of the Taxable amount that has been deferred until payment  """  
      self.DocDefTaxableAmt:int = obj["DocDefTaxableAmt"]
      """  Balance of the Taxable amount that has been deferred until payment  """  
      self.Rpt1DefTaxableAmt:int = obj["Rpt1DefTaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DefTaxableAmt:int = obj["Rpt2DefTaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DefTaxableAmt:int = obj["Rpt3DefTaxableAmt"]
      """  Reporting currency value of this field  """  
      self.DefTaxAmt:int = obj["DefTaxAmt"]
      """  Balance of the Tax amount that has been deferred until payment  """  
      self.DocDefTaxAmt:int = obj["DocDefTaxAmt"]
      """  Balance of the Tax amount that has been deferred until payment  """  
      self.Rpt1DefTaxAmt:int = obj["Rpt1DefTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DefTaxAmt:int = obj["Rpt2DefTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DefTaxAmt:int = obj["Rpt3DefTaxAmt"]
      """  Reporting currency value of this field  """  
      self.ManAdd:bool = obj["ManAdd"]
      """  This record was manually added (not in Liability) but will use the standard calculations  """  
      self.DedTaxAmt:int = obj["DedTaxAmt"]
      """  Deducatable Tax Amount  """  
      self.DocDedTaxAmt:int = obj["DocDedTaxAmt"]
      """  Deducatable Tax Amount  """  
      self.Rpt1DedTaxAmt:int = obj["Rpt1DedTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DedTaxAmt:int = obj["Rpt2DedTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DedTaxAmt:int = obj["Rpt3DedTaxAmt"]
      """  Reporting currency value of this field  """  
      self.FixedAmount:int = obj["FixedAmount"]
      """  Fixed Tax Amount  """  
      self.DocFixedAmount:int = obj["DocFixedAmount"]
      """  Document Fixed Tax Amount  """  
      self.Rpt1FixedAmount:int = obj["Rpt1FixedAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt2FixedAmount:int = obj["Rpt2FixedAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt3FixedAmount:int = obj["Rpt3FixedAmount"]
      """  Reporting currency value of this field  """  
      self.TextCode:str = obj["TextCode"]
      """  Unique Identifier for Legal Text  """  
      self.TaxAmtVar:int = obj["TaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.DocTaxAmtVar:int = obj["DocTaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.Rpt1TaxAmtVar:int = obj["Rpt1TaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.Rpt2TaxAmtVar:int = obj["Rpt2TaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.Rpt3TaxAmtVar:int = obj["Rpt3TaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MovementNum:int = obj["MovementNum"]
      """  MovementNum  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.DebitMemo:bool = obj["DebitMemo"]
      self.DescCollectionType:str = obj["DescCollectionType"]
      """  Collection Type Description  """  
      self.EnableSuperGRate:bool = obj["EnableSuperGRate"]
      self.GroupID:str = obj["GroupID"]
      self.Posted:bool = obj["Posted"]
      self.RateType:int = obj["RateType"]
      self.Rpt1ScrDedTaxAmt:int = obj["Rpt1ScrDedTaxAmt"]
      self.Rpt1ScrFixedAmount:int = obj["Rpt1ScrFixedAmount"]
      """  Display field for Fixed Amount in Report Currency 1.  """  
      self.Rpt1ScrReportableAmt:int = obj["Rpt1ScrReportableAmt"]
      self.Rpt1ScrTaxableAmt:int = obj["Rpt1ScrTaxableAmt"]
      self.Rpt1ScrTaxAmt:int = obj["Rpt1ScrTaxAmt"]
      self.Rpt1ScrTaxAmtVar:int = obj["Rpt1ScrTaxAmtVar"]
      self.Rpt2ScrDedTaxAmt:int = obj["Rpt2ScrDedTaxAmt"]
      self.Rpt2ScrFixedAmount:int = obj["Rpt2ScrFixedAmount"]
      """  Display field for Fixed Amount in Report Currency 2.  """  
      self.Rpt2ScrReportableAm:int = obj["Rpt2ScrReportableAm"]
      self.Rpt2ScrReportableAmt:int = obj["Rpt2ScrReportableAmt"]
      self.Rpt2ScrTaxableAmt:int = obj["Rpt2ScrTaxableAmt"]
      self.Rpt2ScrTaxAmt:int = obj["Rpt2ScrTaxAmt"]
      self.Rpt2ScrTaxAmtVar:int = obj["Rpt2ScrTaxAmtVar"]
      self.Rpt3ScrDedTaxAmt:int = obj["Rpt3ScrDedTaxAmt"]
      self.Rpt3ScrFixedAmount:int = obj["Rpt3ScrFixedAmount"]
      """  Display field for Fixed Amount in Report Currency 31.  """  
      self.Rpt3ScrReportableAmt:int = obj["Rpt3ScrReportableAmt"]
      self.Rpt3ScrTaxableAmt:int = obj["Rpt3ScrTaxableAmt"]
      self.Rpt3ScrTaxAmt:int = obj["Rpt3ScrTaxAmt"]
      self.Rpt3ScrTaxAmtVar:int = obj["Rpt3ScrTaxAmtVar"]
      self.ScrDedTaxAmt:int = obj["ScrDedTaxAmt"]
      self.ScrDocDedTaxAmt:int = obj["ScrDocDedTaxAmt"]
      self.ScrDocFixedAmount:int = obj["ScrDocFixedAmount"]
      """  Display field for Fixed amount in document currency  """  
      self.ScrDocReportableAmt:int = obj["ScrDocReportableAmt"]
      self.ScrDocTaxableAmt:int = obj["ScrDocTaxableAmt"]
      self.ScrDocTaxAmt:int = obj["ScrDocTaxAmt"]
      self.ScrDocTaxAmtVar:int = obj["ScrDocTaxAmtVar"]
      self.ScrFixedAmount:int = obj["ScrFixedAmount"]
      """  Display field for Fixed Amount  """  
      self.ScrReportableAmt:int = obj["ScrReportableAmt"]
      self.ScrTaxableAmt:int = obj["ScrTaxableAmt"]
      self.ScrTaxAmt:int = obj["ScrTaxAmt"]
      self.ScrTaxAmtVar:int = obj["ScrTaxAmtVar"]
      self.DisableManual:bool = obj["DisableManual"]
      """  Flag to indicate if Manual field on tax record should be disabled  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RateCodeDescription:str = obj["RateCodeDescription"]
      self.TaxCodeDescription:str = obj["TaxCodeDescription"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CalcTaxes_input:
   """ Required : 
   ipQuoteNum
   ipOrderNum
   ipInvoiceNum
   ipAPInvKey
   ipCashHeadNum
   ipPayHeadNum
   ipShipPackNum
   ipEmpID
   ipEmpExpenseNum
   """  
   def __init__(self, obj):
      self.ipQuoteNum:int = obj["ipQuoteNum"]
      self.ipOrderNum:int = obj["ipOrderNum"]
      self.ipInvoiceNum:int = obj["ipInvoiceNum"]
      self.ipAPInvKey:str = obj["ipAPInvKey"]
      self.ipCashHeadNum:str = obj["ipCashHeadNum"]
      self.ipPayHeadNum:int = obj["ipPayHeadNum"]
      self.ipShipPackNum:int = obj["ipShipPackNum"]
      self.ipEmpID:str = obj["ipEmpID"]
      self.ipEmpExpenseNum:int = obj["ipEmpExpenseNum"]
      pass

class CalcTaxes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opCommFailure:bool = obj["opCommFailure"]
      self.opMessage:str = obj["parameters"]
      self.opTCStatus:bool = obj["opTCStatus"]
      pass

      """  output parameters  """  

class CanUserVoid_input:
   """ Required : 
   ipInvoiceNum
   ipVendorNum
   """  
   def __init__(self, obj):
      self.ipInvoiceNum:str = obj["ipInvoiceNum"]
      self.ipVendorNum:int = obj["ipVendorNum"]
      pass

class CanUserVoid_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opCanVoid:bool = obj["opCanVoid"]
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeApproved_input:
   """ Required : 
   proposedApproved
   confirmCheck
   ds
   """  
   def __init__(self, obj):
      self.proposedApproved:bool = obj["proposedApproved"]
      """  The proposed approval flag value  """  
      self.confirmCheck:bool = obj["confirmCheck"]
      """  Confirm Check  """  
      self.ds:list[Erp_Tablesets_LogInvAprvVoidTableset] = obj["ds"]
      pass

class ChangeApproved_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.confirmMsg:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_LogInvAprvVoidTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckDocumentIsLocked_input:
   """ Required : 
   keyValue
   keyValue2
   """  
   def __init__(self, obj):
      self.keyValue:str = obj["keyValue"]
      """  VendorNum  """  
      self.keyValue2:str = obj["keyValue2"]
      """  InvoiceNum  """  
      pass

class CheckDocumentIsLocked_output:
   def __init__(self, obj):
      pass

class DeleteByID_input:
   """ Required : 
   vendorNum
   invoiceNum
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      self.invoiceNum:str = obj["invoiceNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_EntityGLCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "Part"  control this field would contain the related Part Number,  for a "Customer"  it contains the Customer.CustNum.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.
The usage of this field is dependent on the type of record.  """  
      self.Key3:str = obj["Key3"]
      """   3rd component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key4:str = obj["Key4"]
      """   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key5:str = obj["Key5"]
      """   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key6:str = obj["Key6"]
      """   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.GLControlType:str = obj["GLControlType"]
      """  Identifier of the GL Control Type.  """  
      self.GLControlCode:str = obj["GLControlCode"]
      """  GL Control Identifier.  """  
      self.BusinessEntity:str = obj["BusinessEntity"]
      """  Identifies the entity.  Reference only.  Used for integrity validation when deleting a GLCTEntity record.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.IsExternalCompany:bool = obj["IsExternalCompany"]
      """  Flag to indicate the account in this record is for an external company.  """  
      self.GlobalEntityGLC:bool = obj["GlobalEntityGLC"]
      """  Marks this EntityGLC as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID of the related BankAcct record.  """  
      self.BankFeeID:str = obj["BankFeeID"]
      self.CallCode:str = obj["CallCode"]
      """  CallCode of the related FSCallCd record.  """  
      self.ChargeCode:str = obj["ChargeCode"]
      self.ClassCode:str = obj["ClassCode"]
      """  ClassCode of the related FAClass record.  """  
      self.ClassID:str = obj["ClassID"]
      """  ClassID.  This can be ClassID of PartClass, PRClsDed, or PRClsTax  """  
      self.ContractCode:str = obj["ContractCode"]
      """  ContractCode of the related FSContCd record.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  CurrencyCode of the related Currency record.  """  
      self.CustNum:int = obj["CustNum"]
      """  CustNum of the related Customer record  """  
      self.DeductionID:str = obj["DeductionID"]
      """  DeductionID of PRClsDed or PRDeduct.  """  
      self.EmpID:str = obj["EmpID"]
      """  EmpID of the related PREmpMas record.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  ExpenseCode of PayTLbr, LabExpCd  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  ExtSystemID of ExtCompany table  """  
      self.FromPlant:str = obj["FromPlant"]
      """  FromPlant value of the related PlntTranDef record.  """  
      self.GroupCode:str = obj["GroupCode"]
      """  GroupCode of the related FAGroup record.  """  
      self.GroupID:str = obj["GroupID"]
      self.HeadNum:int = obj["HeadNum"]
      self.InvoiceNum:str = obj["InvoiceNum"]
      self.JCDept:str = obj["JCDept"]
      """  JCDept of the related JCDept record.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  MiscCode of the related MiscChrg or PurMisc record.  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum of the related Part record.  """  
      self.PayTypeID:str = obj["PayTypeID"]
      """  PayTypeID of PayType  """  
      self.PerConName:str = obj["PerConName"]
      self.PIStatus:str = obj["PIStatus"]
      """  PI Status  """  
      self.Plant:str = obj["Plant"]
      """  Plant of the related PlantConfCtrl record.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  ProdCode of the related ProdGrup record.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  ProjectID of the related Project record.  """  
      self.PurchCode:str = obj["PurchCode"]
      """  PurchCode of the related GLPurch record.  """  
      self.RateCode:str = obj["RateCode"]
      """  RateCode of the related GLRate record.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  ReasonCode of the related Reason record.  """  
      self.ReasonType:str = obj["ReasonType"]
      """  ReasonType of the related Reason record.  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  SalesCatID of the related SalesCat record.  """  
      self.Shift:int = obj["Shift"]
      """  Shift value of the related JCShift record.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  TaxCode of the related SalesTax record.  """  
      self.TaxTblID:str = obj["TaxTblID"]
      """  TaxTblID of PRTaxMas or PRClsTax.  """  
      self.ToPlant:str = obj["ToPlant"]
      """  ToPlant value of the related PlntTranDef record.  """  
      self.TransferMethod:str = obj["TransferMethod"]
      """  TransferMethod of ExtCompany table  """  
      self.TypeID:str = obj["TypeID"]
      """  Type ID  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum of the related Vendor record.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  WarehouseCode of the related Warehse record.  """  
      self.ExpenseTypeCode:str = obj["ExpenseTypeCode"]
      self.IsFiltered:bool = obj["IsFiltered"]
      self.OprTypeCode:str = obj["OprTypeCode"]
      self.CashDeskID:str = obj["CashDeskID"]
      self.TIN:str = obj["TIN"]
      self.ReclassCodeID:str = obj["ReclassCodeID"]
      self.BitFlag:int = obj["BitFlag"]
      self.GLCntrlDescription:str = obj["GLCntrlDescription"]
      self.GLCntrlTypeDescription:str = obj["GLCntrlTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LegalNumberGenerateRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.NumberType:str = obj["NumberType"]
      self.NumberYear:int = obj["NumberYear"]
      self.NumberPrefix:str = obj["NumberPrefix"]
      """  The legal number prefix  """  
      self.NumberSuffix:str = obj["NumberSuffix"]
      self.PrefixList:str = obj["PrefixList"]
      self.GenerationType:str = obj["GenerationType"]
      self.EnableNumberPrefix:bool = obj["EnableNumberPrefix"]
      self.EnableNumberSuffix:bool = obj["EnableNumberSuffix"]
      self.NumberOption:str = obj["NumberOption"]
      self.LegalNumberNum:int = obj["LegalNumberNum"]
      """  Unique identifier of the Legal Number record  """  
      self.DocumentDate:str = obj["DocumentDate"]
      self.AdditionalParams:str = obj["AdditionalParams"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LogAPInvAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.VendorNum:int = obj["VendorNum"]
      self.InvoiceNum:str = obj["InvoiceNum"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LogAPInvListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead it is assigned from the Vendor.VendorNum using VendorID to find the Vendor record.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Vendor's invoice number.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group that the invoice was associated with  during the data entry process. This field is not directly maintainable, it is assigned by the invoice entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  """  
      self.DebitMemo:bool = obj["DebitMemo"]
      """   Indicates the type of document. Yes = Debit Memo,  No= Invoice. This value can't be changed after the record has been created.
Debit memos affect the way detail quantities and amounts are stored in the database. They will always be stored with a negative sign, but are entered as a positive.
The system uses this field to test for Debit Memos,  indicated by "DM" following the invoice number.  """  
      self.Approved:bool = obj["Approved"]
      """  Yes indicates all necessary approvals have been received.  No indicates approvals are pending.  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  Date the Logged Invoice was approved.  """  
      self.Matched:bool = obj["Matched"]
      """  Yes indicates this logged invoice has been matched to an AP Invoice.  No indicates it has not been matched.  """  
      self.MatchedDate:str = obj["MatchedDate"]
      """  Date the logged invoice was matched to an AP Invoice.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates whether or not this logged invoice has been posted to the GL.  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice date.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Contains the foreign key to the PurTerms master file.  Defaulted from Vendor.TermsCode.  This is MANDATORY ENTRY. User maintainable via a combo-box for terms description.  """  
      self.Void:bool = obj["Void"]
      """  Indicates if this logged invoice has been voided.  """  
      self.VoidedBy:str = obj["VoidedBy"]
      """  User ID that voided the invoice. This is not maintainable by the user.  """  
      self.VoidReason:str = obj["VoidReason"]
      """  Text that explains why the logged invoice was voided.  """  
      self.VoidDate:str = obj["VoidDate"]
      """  Date the Logged Invoice was voided.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Total sales tax amount for this invoice. Totals the TaxAmt from the APInvTax records of this invoice.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Total sales tax amount for this invoice. Totals the DocTaxAmt from the LogAPInvTax records of this invoice.  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.DueDate:str = obj["DueDate"]
      """  The due date of the earliest unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  Apply Date  """  
      self.Description:str = obj["Description"]
      """  A short description that can be used to explain what this invoice is for. Ex: Rent, Auto Lease Payment.  """  
      self.REFPONum:int = obj["REFPONum"]
      """  Reference PO number(optional when CM is present). Used to identify the PO that this Invoice is for.  If the Reference PO has a lock exchange rate then that is the rate that will be used on this AP  invoice,  """  
      self.InvoiceVendorAmt:int = obj["InvoiceVendorAmt"]
      """  For use by external G/L interfacing.  This field is sign flipped for debit memos.  """  
      self.DocInvoiceVendorAmt:int = obj["DocInvoiceVendorAmt"]
      """  A user entered verification amount.  DOCUMENT CURRENCY ONLY, a corresponding base currency field exists but is only used for external G/L interfacing.  This field is sign flipped for debit memos.  The calculated Invoice Amount (DocInvoiceAmt) must match this amount before the invoice can be posted.  """  
      self.Rpt1InvoiceVendorAmt:int = obj["Rpt1InvoiceVendorAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2InvoiceVendorAmt:int = obj["Rpt2InvoiceVendorAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3InvoiceVendorAmt:int = obj["Rpt3InvoiceVendorAmt"]
      """  Reporting currency value of this field  """  
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      """  Total invoice Amount.   This field has a true sign. (debit memos are negative).  """  
      self.DocInvoiceAmt:int = obj["DocInvoiceAmt"]
      """  Total invoice Amount.(Vendors Currency) This field has a true sign. (debit memos are negative).  """  
      self.Rpt1InvoiceAmt:int = obj["Rpt1InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2InvoiceAmt:int = obj["Rpt2InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3InvoiceAmt:int = obj["Rpt3InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Region for this invoice.  """  
      self.TaxPoint:str = obj["TaxPoint"]
      """  Tax Point  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Date Used to calculate Tax Rates  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  User ID that entered the invoice. This is not maintainable by the user.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.AutoApproved:bool = obj["AutoApproved"]
      """   Reserved for future development.
Indicates if the approval process is required.  If yes, an approval code is not required and the invoice is automatically approved.  If no, an approval code is required.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year. This is defaulted based on the finding the Fiscal master for the corresponding InvoiceDate.  User can override this. This value is used as one of the defaults to the InvHead records. (see InvHead for usage).  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  A Fiscal period which provides one of the defaults to be used when creating invoices within this group. This field is defaulted based on finding the Fiscal master which contains the corresponding  InvoiceDate period. (See InvcHead.FiscalPeriod for usage)  """  
      self.Rounding:int = obj["Rounding"]
      """  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  """  
      self.DocRounding:int = obj["DocRounding"]
      """  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  """  
      self.Rpt1Rounding:int = obj["Rpt1Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt2Rounding:int = obj["Rpt2Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt3Rounding:int = obj["Rpt3Rounding"]
      """  Reporting currency value of this field  """  
      self.DiscountDate:str = obj["DiscountDate"]
      """  Reserved for Future Development.  Prompt payment discount due date. The date according to the terms when you are allowed to take the prompt payment discount (if any) given by the vendor. This date is NOT directly maintainable. It is calculated using the InvoiceDate + PurTerms.DiscountDays. If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then this is not applicable and is set to ? (null value).  """  
      self.DiscountAmt:int = obj["DiscountAmt"]
      """  Reserved for Future development. Discount amount that can be taken if paid by the DiscountDate.  This is calculated by the System via APInvHed write trigger. Formula ((PurTerms.DiscountPercent/100)*APInvHed.InvoiceBal on AIn.  If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then it is not applicable and is set to zero.  """  
      self.DocDiscountAmt:int = obj["DocDiscountAmt"]
      """  Reserved for future development. Discount amount(Vendors Currency) that can be taken if paid by the DiscountDate.  This is calculated by the System via APInvHed write trigger. Formula ((PurTerms.DiscountPercent/100)*APInvHed.InvoiceBal on AIn.  If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then it is not applicable and is set to zero.  """  
      self.InvoiceRef:str = obj["InvoiceRef"]
      """   Reserved for future development. This field is maintainable/viewable only for Debit Memos. It represents the invoice # that this debit memo relates to. It can be left blank. If entered it must be a valid APInvHed record where the InvcHead.DebitMemo = No. This field is also used to order the invoices when printing aging reports. The idea is to be able to print the debit memos next to their corresponding invoice. Therefore, this field will always have a value.
For Invoices it is equal to the InvoiceNum.
For Debit memos where they are not related to an invoice it is also set equal to the Debit memo's InvoiceNum. In this later case when InvcHead.DebitMemo = Yes and InvcHead.InvoiceNum = InvcHead.InvoiceRef the InvoiceRef is reset to zero before being displayed, then when written back to the database it is set = to the InvoiceNum if the user did not enter a related invoice.  """  
      self.AuthorizedBy:str = obj["AuthorizedBy"]
      """  User ID that authorized the invoice. This is not maintainable by the user.  """  
      self.Rpt1DiscountAmt:int = obj["Rpt1DiscountAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DiscountAmt:int = obj["Rpt2DiscountAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DiscountAmt:int = obj["Rpt3DiscountAmt"]
      """  Reporting currency value of this field  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.InvExpense:int = obj["InvExpense"]
      """  Invoice Expense Amount. This is the Gross Invoice Amount minus the taxes.  """  
      self.DocInvExpense:int = obj["DocInvExpense"]
      """  Invoice Expense Amount. This is the Gross Invoice Amount minus the taxes.  """  
      self.Rpt1InvExpense:int = obj["Rpt1InvExpense"]
      """  Invoice Expense Amount. This is the Gross Invoice Amount minus the taxes.  """  
      self.Rpt2InvExpense:int = obj["Rpt2InvExpense"]
      """  Invoice Expense Amount. This is the Gross Invoice Amount minus the taxes.  """  
      self.Rpt3InvExpense:int = obj["Rpt3InvExpense"]
      """  Invoice Expense Amount. This is the Gross Invoice Amount minus the taxes.  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the invoice is ready for calculations.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.TaxRateGrpCode:str = obj["TaxRateGrpCode"]
      """  Tax Rate Group Code  """  
      self.LockTaxRate:bool = obj["LockTaxRate"]
      """  Locks Tax Rate and allows user to edit the tax exchange rate  """  
      self.SEBankRef:str = obj["SEBankRef"]
      """  Sweden and Finland Localization Field - Banking Reference  """  
      self.SEPayCode:str = obj["SEPayCode"]
      """  Sweden and Finland Localization Field - Payment Code  """  
      self.SEPMUID:int = obj["SEPMUID"]
      """  Sweden and Finland Localization field, Payment Method code  """  
      self.BankID:str = obj["BankID"]
      """  Unique ID of the vendor's bank.  """  
      self.VoidLegalNumber:str = obj["VoidLegalNumber"]
      """  Legal Number for the voiding.  """  
      self.VoidTranDocTypeID:str = obj["VoidTranDocTypeID"]
      """  Transaction Document Type for the voiding.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type for the record.  """  
      self.CardCode:str = obj["CardCode"]
      """   Denmark Localization
Card (payment) code  """  
      self.BankGiroAcctNbr:str = obj["BankGiroAcctNbr"]
      """   Denmark Localization
Account Number  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TranType:str = obj["TranType"]
      """  TranType  """  
      self.PLInvoiceReference:str = obj["PLInvoiceReference"]
      """  PLInvoiceReference  """  
      self.ScrInvVendorAmt:int = obj["ScrInvVendorAmt"]
      self.MatchInvoicePosted:bool = obj["MatchInvoicePosted"]
      """  When the APInvHed record is created from this logged invoice and the APInvHed record is posted, this flag is set to true.  This is used by the UI.  """  
      self.ScrTotDedTaxAmt:int = obj["ScrTotDedTaxAmt"]
      self.ScrDocTotSelfAmt:int = obj["ScrDocTotSelfAmt"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.Rpt3ScrTotSelfAmt:int = obj["Rpt3ScrTotSelfAmt"]
      self.EnableExchangeRate:bool = obj["EnableExchangeRate"]
      self.EnableLockRate:bool = obj["EnableLockRate"]
      self.XRateLabel:str = obj["XRateLabel"]
      self.VendorInactive:bool = obj["VendorInactive"]
      """  Indicates if the vendor is active  """  
      self.ScrTaxAmt:int = obj["ScrTaxAmt"]
      self.Rpt1ScrTaxAmt:int = obj["Rpt1ScrTaxAmt"]
      self.Rpt2ScrTaxAmt:int = obj["Rpt2ScrTaxAmt"]
      self.Rpt3ScrTaxAmt:int = obj["Rpt3ScrTaxAmt"]
      self.Rpt1ScrInvVendorAmt:int = obj["Rpt1ScrInvVendorAmt"]
      self.Rpt2ScrInvVendorAmt:int = obj["Rpt2ScrInvVendorAmt"]
      self.Rpt3ScrInvVendorAmt:int = obj["Rpt3ScrInvVendorAmt"]
      self.Rpt1ScrInvoiceAmt:int = obj["Rpt1ScrInvoiceAmt"]
      self.Rpt2ScrInvoiceAmt:int = obj["Rpt2ScrInvoiceAmt"]
      self.Rpt3ScrInvoiceAmt:int = obj["Rpt3ScrInvoiceAmt"]
      self.ScrInvoiceAmt:int = obj["ScrInvoiceAmt"]
      self.ScrDocTaxAmt:int = obj["ScrDocTaxAmt"]
      self.ScrDocInvVendorAmt:int = obj["ScrDocInvVendorAmt"]
      self.ScrDocInvoiceAmt:int = obj["ScrDocInvoiceAmt"]
      self.ScrTotTaxableAmt:int = obj["ScrTotTaxableAmt"]
      self.ScrDocTotTaxableAmt:int = obj["ScrDocTotTaxableAmt"]
      self.Rpt1ScrTotTaxableAmt:int = obj["Rpt1ScrTotTaxableAmt"]
      self.Rpt2ScrTotTaxableAmt:int = obj["Rpt2ScrTotTaxableAmt"]
      self.Rpt3ScrTotTaxableAmt:int = obj["Rpt3ScrTotTaxableAmt"]
      self.ScrTotReportableAmt:int = obj["ScrTotReportableAmt"]
      self.ScrDocTotReportableAmt:int = obj["ScrDocTotReportableAmt"]
      self.Rpt1ScrTotReportableAmt:int = obj["Rpt1ScrTotReportableAmt"]
      self.Rpt2ScrTotReportableAmt:int = obj["Rpt2ScrTotReportableAmt"]
      self.Rpt3ScrTotReportableAmt:int = obj["Rpt3ScrTotReportableAmt"]
      self.ScrDocTotDedTaxAmt:int = obj["ScrDocTotDedTaxAmt"]
      self.Rpt1ScrTotDedTaxAmt:int = obj["Rpt1ScrTotDedTaxAmt"]
      self.Rpt2ScrTotDedTaxAmt:int = obj["Rpt2ScrTotDedTaxAmt"]
      self.Rpt3ScrTotDedTaxAmt:int = obj["Rpt3ScrTotDedTaxAmt"]
      self.ScrTotWithholdingAmt:int = obj["ScrTotWithholdingAmt"]
      self.ScrDocTotWithholdingAmt:int = obj["ScrDocTotWithholdingAmt"]
      self.Rpt1ScrTotWithholdingAmt:int = obj["Rpt1ScrTotWithholdingAmt"]
      self.Rpt2ScrTotWithholdingAmt:int = obj["Rpt2ScrTotWithholdingAmt"]
      self.Rpt3ScrTotWithholdingAmt:int = obj["Rpt3ScrTotWithholdingAmt"]
      self.ScrTotSelfAmt:int = obj["ScrTotSelfAmt"]
      self.Rpt1ScrTotSelfAmt:int = obj["Rpt1ScrTotSelfAmt"]
      self.Rpt2ScrTotSelfAmt:int = obj["Rpt2ScrTotSelfAmt"]
      self.ScrDocRounding:int = obj["ScrDocRounding"]
      self.Rpt2ScrRounding:int = obj["Rpt2ScrRounding"]
      self.Rpt3ScrRounding:int = obj["Rpt3ScrRounding"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.TaxLinesExist:bool = obj["TaxLinesExist"]
      self.EnableDueDate:bool = obj["EnableDueDate"]
      self.InvoiceVariance:int = obj["InvoiceVariance"]
      self.Rpt1InvoiceVariance:int = obj["Rpt1InvoiceVariance"]
      self.Rpt2InvoiceVariance:int = obj["Rpt2InvoiceVariance"]
      self.Rpt3InvoiceVariance:int = obj["Rpt3InvoiceVariance"]
      self.BillAddressList:str = obj["BillAddressList"]
      self.ScrRounding:int = obj["ScrRounding"]
      self.DocInvoiceVariance:int = obj["DocInvoiceVariance"]
      self.Rpt1ScrRounding:int = obj["Rpt1ScrRounding"]
      self.TotalInvAmt:int = obj["TotalInvAmt"]
      self.ScrDiscountAmt:int = obj["ScrDiscountAmt"]
      self.ScrDocDiscountAmt:int = obj["ScrDocDiscountAmt"]
      self.ScrInvoiceRef:str = obj["ScrInvoiceRef"]
      self.ScrTotInvoiceAmt:int = obj["ScrTotInvoiceAmt"]
      self.ScrDocTotInvoiceAmt:int = obj["ScrDocTotInvoiceAmt"]
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.AuthAdmins:str = obj["AuthAdmins"]
      """  Intended for internal use  """  
      self.AuthAdminNames:str = obj["AuthAdminNames"]
      """  Intended for Internal Use  """  
      self.EnableTaxesInTracker:bool = obj["EnableTaxesInTracker"]
      """  Logical indicating whether or not the Logged Invoice Tracker is to enable the GL Transaction Tb  """  
      self.Rpt1ScrDocInvoiceAmt:int = obj["Rpt1ScrDocInvoiceAmt"]
      self.Rpt2ScrDocInvoiceAmt:int = obj["Rpt2ScrDocInvoiceAmt"]
      self.Rpt3ScrDocInvoiceAmt:int = obj["Rpt3ScrDocInvoiceAmt"]
      self.UpdateEntity:bool = obj["UpdateEntity"]
      """  Not intended for external use.  Logical indicating that a default entity was created for the new logged invoice.  """  
      self.Rpt2ScrTotInvoiceAmt:int = obj["Rpt2ScrTotInvoiceAmt"]
      self.Rpt3ScrTotInvoiceAmt:int = obj["Rpt3ScrTotInvoiceAmt"]
      self.Rpt1ScrTotInvoiceAmt:int = obj["Rpt1ScrTotInvoiceAmt"]
      self.IsEligibleToVoid:bool = obj["IsEligibleToVoid"]
      """  Not intended for external use.  Indicates if the user has Void authority.  """  
      self.ScrInvExpense:int = obj["ScrInvExpense"]
      self.ScrDocInvExpense:int = obj["ScrDocInvExpense"]
      self.Rpt2ScrInvExpense:int = obj["Rpt2ScrInvExpense"]
      self.Rpt3ScrInvExpense:int = obj["Rpt3ScrInvExpense"]
      self.Rpt1ScrInvExpense:int = obj["Rpt1ScrInvExpense"]
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.TransApplyDate:str = obj["TransApplyDate"]
      """  This field is used when invoice is transferred form one Group to another and the user has a cance to change this invoice Apply Date.  """  
      self.DocDspInvVendorAmt:int = obj["DocDspInvVendorAmt"]
      """  Document Invoice Vendor Amout only for dispaly  """  
      self.DspInvVendorAmt:int = obj["DspInvVendorAmt"]
      """  DspInvVendorAmt  """  
      self.Rpt1DspInvVendorAmt:int = obj["Rpt1DspInvVendorAmt"]
      """  Invoice Vendor Amout only for dispaly in report currency  """  
      self.Rpt2DspInvVendorAmt:int = obj["Rpt2DspInvVendorAmt"]
      """  Invoice Vendor Amout only for dispaly in report currency  """  
      self.Rpt3DspInvVendorAmt:int = obj["Rpt3DspInvVendorAmt"]
      """  Invoice Vendor Amout only for dispaly in report currency  """  
      self.EnableTaxLock:bool = obj["EnableTaxLock"]
      self.UseTaxRate:bool = obj["UseTaxRate"]
      self.TaxExchangeRate:int = obj["TaxExchangeRate"]
      self.EnableTaxExRate:bool = obj["EnableTaxExRate"]
      self.TaxRateLinesExist:bool = obj["TaxRateLinesExist"]
      self.PayMethod:str = obj["PayMethod"]
      """  Pay Method Type  """  
      self.VendorBank:str = obj["VendorBank"]
      """  Vendor Bank  """  
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.RateGrpCodeDescription:str = obj["RateGrpCodeDescription"]
      """  Description  """  
      self.SEPayMethodType:int = obj["SEPayMethodType"]
      """  Indicated the type of payment with the following options:
 0 = Manual (default)
 1 = Electronic Interface
 2 = Check Printing
 3 = Payment Instrument Type 1
 4 = Payment Instrument Type 2  """  
      self.SEPayMethodName:str = obj["SEPayMethodName"]
      """  Name of the payment method  """  
      self.SEPayMethodSummarizePerCustomer:bool = obj["SEPayMethodSummarizePerCustomer"]
      """   Indicates that invoices for the customer is summarized and sent as a sum to the bank without specifying the individual invoices.
A single bank transaction is created for the payment but what?s actually sent to the bank will be determined by the electronic interface plug-in program.
Only enabled if type is set to ?Electronic Interface?  """  
      self.TaxRateGrpDescription:str = obj["TaxRateGrpDescription"]
      """  Description  """  
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      """  Full description for the Tax Region.  """  
      self.TermsCodeDescription:str = obj["TermsCodeDescription"]
      """  Full description of terms....this is printed on purchase orders. Can't be blank.  """  
      self.UserfileName:str = obj["UserfileName"]
      """  User Name  """  
      self.VendBankSwiftNum:str = obj["VendBankSwiftNum"]
      """  Swift number of the bank.  """  
      self.VendBankIBANCode:str = obj["VendBankIBANCode"]
      """  IBAN Code of the Supplier Bank  """  
      self.VendBankBankGiroAcctNbr:str = obj["VendBankBankGiroAcctNbr"]
      """   Denmark Localization          
Account Number  """  
      self.VendBankLocalBIC:str = obj["VendBankLocalBIC"]
      """  Local BIC of the Supplier Bank  """  
      self.VendBankBankAcctNumber:str = obj["VendBankBankAcctNumber"]
      """  The Bank account number for the Vendor.  Used with Electronic payments.  """  
      self.VendBankBankName:str = obj["VendBankBankName"]
      """  Supplier Bank Name  """  
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      """  Second address line of the Supplier  """  
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorNumState:str = obj["VendorNumState"]
      """  Can be blank.  """  
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.VoidedByName:str = obj["VoidedByName"]
      """  User Name  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LogAPInvListTableset:
   def __init__(self, obj):
      self.LogAPInvList:list[Erp_Tablesets_LogAPInvListRow] = obj["LogAPInvList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_LogAPInvRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead it is assigned from the Vendor.VendorNum using VendorID to find the Vendor record.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Vendor's invoice number.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group that the invoice was associated with  during the data entry process. This field is not directly maintainable, it is assigned by the invoice entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  """  
      self.DebitMemo:bool = obj["DebitMemo"]
      """   Indicates the type of document. Yes = Debit Memo,  No= Invoice. This value can't be changed after the record has been created.
Debit memos affect the way detail quantities and amounts are stored in the database. They will always be stored with a negative sign, but are entered as a positive.
The system uses this field to test for Debit Memos,  indicated by "DM" following the invoice number.  """  
      self.Approved:bool = obj["Approved"]
      """  Yes indicates all necessary approvals have been received.  No indicates approvals are pending.  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  Date the Logged Invoice was approved.  """  
      self.Matched:bool = obj["Matched"]
      """  Yes indicates this logged invoice has been matched to an AP Invoice.  No indicates it has not been matched.  """  
      self.MatchedDate:str = obj["MatchedDate"]
      """  Date the logged invoice was matched to an AP Invoice.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates whether or not this logged invoice has been posted to the GL.  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice date.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Contains the foreign key to the PurTerms master file.  Defaulted from Vendor.TermsCode.  This is MANDATORY ENTRY. User maintainable via a combo-box for terms description.  """  
      self.Void:bool = obj["Void"]
      """  Indicates if this logged invoice has been voided.  """  
      self.VoidedBy:str = obj["VoidedBy"]
      """  User ID that voided the invoice. This is not maintainable by the user.  """  
      self.VoidReason:str = obj["VoidReason"]
      """  Text that explains why the logged invoice was voided.  """  
      self.VoidDate:str = obj["VoidDate"]
      """  Date the Logged Invoice was voided.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Total sales tax amount for this invoice. Totals the TaxAmt from the APInvTax records of this invoice.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Total sales tax amount for this invoice. Totals the DocTaxAmt from the LogAPInvTax records of this invoice.  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.DueDate:str = obj["DueDate"]
      """  The due date of the earliest unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  Apply Date  """  
      self.Description:str = obj["Description"]
      """  A short description that can be used to explain what this invoice is for. Ex: Rent, Auto Lease Payment.  """  
      self.REFPONum:int = obj["REFPONum"]
      """  Reference PO number(optional when CM is present). Used to identify the PO that this Invoice is for.  If the Reference PO has a lock exchange rate then that is the rate that will be used on this AP  invoice,  """  
      self.InvoiceVendorAmt:int = obj["InvoiceVendorAmt"]
      """  For use by external G/L interfacing.  This field is sign flipped for debit memos.  """  
      self.DocInvoiceVendorAmt:int = obj["DocInvoiceVendorAmt"]
      """  A user entered verification amount.  DOCUMENT CURRENCY ONLY, a corresponding base currency field exists but is only used for external G/L interfacing.  This field is sign flipped for debit memos.  The calculated Invoice Amount (DocInvoiceAmt) must match this amount before the invoice can be posted.  """  
      self.Rpt1InvoiceVendorAmt:int = obj["Rpt1InvoiceVendorAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2InvoiceVendorAmt:int = obj["Rpt2InvoiceVendorAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3InvoiceVendorAmt:int = obj["Rpt3InvoiceVendorAmt"]
      """  Reporting currency value of this field  """  
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      """  Total invoice Amount.   This field has a true sign. (debit memos are negative).  """  
      self.DocInvoiceAmt:int = obj["DocInvoiceAmt"]
      """  Total invoice Amount.(Vendors Currency) This field has a true sign. (debit memos are negative).  """  
      self.Rpt1InvoiceAmt:int = obj["Rpt1InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2InvoiceAmt:int = obj["Rpt2InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3InvoiceAmt:int = obj["Rpt3InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Region for this invoice.  """  
      self.TaxPoint:str = obj["TaxPoint"]
      """  Tax Point  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Date Used to calculate Tax Rates  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  User ID that entered the invoice. This is not maintainable by the user.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.AutoApproved:bool = obj["AutoApproved"]
      """   Reserved for future development.
Indicates if the approval process is required.  If yes, an approval code is not required and the invoice is automatically approved.  If no, an approval code is required.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year. This is defaulted based on the finding the Fiscal master for the corresponding InvoiceDate.  User can override this. This value is used as one of the defaults to the InvHead records. (see InvHead for usage).  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  A Fiscal period which provides one of the defaults to be used when creating invoices within this group. This field is defaulted based on finding the Fiscal master which contains the corresponding  InvoiceDate period. (See InvcHead.FiscalPeriod for usage)  """  
      self.Rounding:int = obj["Rounding"]
      """  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  """  
      self.DocRounding:int = obj["DocRounding"]
      """  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  """  
      self.Rpt1Rounding:int = obj["Rpt1Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt2Rounding:int = obj["Rpt2Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt3Rounding:int = obj["Rpt3Rounding"]
      """  Reporting currency value of this field  """  
      self.DiscountDate:str = obj["DiscountDate"]
      """  Reserved for Future Development.  Prompt payment discount due date. The date according to the terms when you are allowed to take the prompt payment discount (if any) given by the vendor. This date is NOT directly maintainable. It is calculated using the InvoiceDate + PurTerms.DiscountDays. If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then this is not applicable and is set to ? (null value).  """  
      self.DiscountAmt:int = obj["DiscountAmt"]
      """  Reserved for Future development. Discount amount that can be taken if paid by the DiscountDate.  This is calculated by the System via APInvHed write trigger. Formula ((PurTerms.DiscountPercent/100)*APInvHed.InvoiceBal on AIn.  If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then it is not applicable and is set to zero.  """  
      self.DocDiscountAmt:int = obj["DocDiscountAmt"]
      """  Reserved for future development. Discount amount(Vendors Currency) that can be taken if paid by the DiscountDate.  This is calculated by the System via APInvHed write trigger. Formula ((PurTerms.DiscountPercent/100)*APInvHed.InvoiceBal on AIn.  If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then it is not applicable and is set to zero.  """  
      self.InvoiceRef:str = obj["InvoiceRef"]
      """   Reserved for future development. This field is maintainable/viewable only for Debit Memos. It represents the invoice # that this debit memo relates to. It can be left blank. If entered it must be a valid APInvHed record where the InvcHead.DebitMemo = No. This field is also used to order the invoices when printing aging reports. The idea is to be able to print the debit memos next to their corresponding invoice. Therefore, this field will always have a value.
For Invoices it is equal to the InvoiceNum.
For Debit memos where they are not related to an invoice it is also set equal to the Debit memo's InvoiceNum. In this later case when InvcHead.DebitMemo = Yes and InvcHead.InvoiceNum = InvcHead.InvoiceRef the InvoiceRef is reset to zero before being displayed, then when written back to the database it is set = to the InvoiceNum if the user did not enter a related invoice.  """  
      self.AuthorizedBy:str = obj["AuthorizedBy"]
      """  User ID that authorized the invoice. This is not maintainable by the user.  """  
      self.Rpt1DiscountAmt:int = obj["Rpt1DiscountAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DiscountAmt:int = obj["Rpt2DiscountAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DiscountAmt:int = obj["Rpt3DiscountAmt"]
      """  Reporting currency value of this field  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.InvExpense:int = obj["InvExpense"]
      """  Invoice Expense Amount. This is the Gross Invoice Amount minus the taxes.  """  
      self.DocInvExpense:int = obj["DocInvExpense"]
      """  Invoice Expense Amount. This is the Gross Invoice Amount minus the taxes.  """  
      self.Rpt1InvExpense:int = obj["Rpt1InvExpense"]
      """  Invoice Expense Amount. This is the Gross Invoice Amount minus the taxes.  """  
      self.Rpt2InvExpense:int = obj["Rpt2InvExpense"]
      """  Invoice Expense Amount. This is the Gross Invoice Amount minus the taxes.  """  
      self.Rpt3InvExpense:int = obj["Rpt3InvExpense"]
      """  Invoice Expense Amount. This is the Gross Invoice Amount minus the taxes.  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the invoice is ready for calculations.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.TaxRateGrpCode:str = obj["TaxRateGrpCode"]
      """  Tax Rate Group Code  """  
      self.LockTaxRate:bool = obj["LockTaxRate"]
      """  Locks Tax Rate and allows user to edit the tax exchange rate  """  
      self.SEBankRef:str = obj["SEBankRef"]
      """  Sweden and Finland Localization Field - Banking Reference  """  
      self.SEPayCode:str = obj["SEPayCode"]
      """  Sweden and Finland Localization Field - Payment Code  """  
      self.SEPMUID:int = obj["SEPMUID"]
      """  Sweden and Finland Localization field, Payment Method code  """  
      self.BankID:str = obj["BankID"]
      """  Unique ID of the vendor's bank.  """  
      self.VoidLegalNumber:str = obj["VoidLegalNumber"]
      """  Legal Number for the voiding.  """  
      self.VoidTranDocTypeID:str = obj["VoidTranDocTypeID"]
      """  Transaction Document Type for the voiding.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type for the record.  """  
      self.CardCode:str = obj["CardCode"]
      """   Denmark Localization
Card (payment) code  """  
      self.BankGiroAcctNbr:str = obj["BankGiroAcctNbr"]
      """   Denmark Localization
Account Number  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CHISRCodeLine:str = obj["CHISRCodeLine"]
      """  CHISRCodeLine  """  
      self.CustomsNumber:str = obj["CustomsNumber"]
      """  CustomsNumber  """  
      self.ReceivedDate:str = obj["ReceivedDate"]
      """  ReceivedDate  """  
      self.TranType:str = obj["TranType"]
      """  TranType  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID.  """  
      self.PLInvoiceReference:str = obj["PLInvoiceReference"]
      """  PLInvoiceReference  """  
      self.VoidDescription:str = obj["VoidDescription"]
      """  VoidDescription  """  
      self.APTaxRoundOption:int = obj["APTaxRoundOption"]
      """  APTaxRoundOption  """  
      self.AuthAdminNames:str = obj["AuthAdminNames"]
      """  Intended for Internal Use  """  
      self.AuthAdmins:str = obj["AuthAdmins"]
      """  Intended for internal use  """  
      self.BankName:str = obj["BankName"]
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.BillAddressList:str = obj["BillAddressList"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.DocDspInvVendorAmt:int = obj["DocDspInvVendorAmt"]
      """  Document Invoice Vendor Amout only for dispaly  """  
      self.DocInvoiceVariance:int = obj["DocInvoiceVariance"]
      self.DspInvVendorAmt:int = obj["DspInvVendorAmt"]
      """  DspInvVendorAmt  """  
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      self.EnableDueDate:bool = obj["EnableDueDate"]
      self.EnableExchangeRate:bool = obj["EnableExchangeRate"]
      self.EnableLockRate:bool = obj["EnableLockRate"]
      self.EnableTaxesInTracker:bool = obj["EnableTaxesInTracker"]
      """  Logical indicating whether or not the Logged Invoice Tracker is to enable the GL Transaction Tb  """  
      self.EnableTaxExRate:bool = obj["EnableTaxExRate"]
      self.EnableTaxLock:bool = obj["EnableTaxLock"]
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      """  Enable setting of Transaction Document Type  """  
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      self.InvoiceVariance:int = obj["InvoiceVariance"]
      self.IsDiscountforDebitM:bool = obj["IsDiscountforDebitM"]
      self.IsEligibleToVoid:bool = obj["IsEligibleToVoid"]
      """  Not intended for external use.  Indicates if the user has Void authority.  """  
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.MatchInvoicePosted:bool = obj["MatchInvoicePosted"]
      """  When the APInvHed record is created from this logged invoice and the APInvHed record is posted, this flag is set to true.  This is used by the UI.  """  
      self.PayMethod:str = obj["PayMethod"]
      """  Pay Method Type  """  
      self.PLVendorAutoInvoiceNum:bool = obj["PLVendorAutoInvoiceNum"]
      """  CSF Poland. Vendor uses Invoice reference number  """  
      self.Rpt1DspInvVendorAmt:int = obj["Rpt1DspInvVendorAmt"]
      """  Invoice Vendor Amout only for dispaly in report currency  """  
      self.Rpt1InvoiceVariance:int = obj["Rpt1InvoiceVariance"]
      self.Rpt1ScrDocInvoiceAmt:int = obj["Rpt1ScrDocInvoiceAmt"]
      self.Rpt1ScrInvExpense:int = obj["Rpt1ScrInvExpense"]
      self.Rpt1ScrInvoiceAmt:int = obj["Rpt1ScrInvoiceAmt"]
      self.Rpt1ScrInvVendorAmt:int = obj["Rpt1ScrInvVendorAmt"]
      self.Rpt1ScrRounding:int = obj["Rpt1ScrRounding"]
      self.Rpt1ScrTaxAmt:int = obj["Rpt1ScrTaxAmt"]
      self.Rpt1ScrTotDedTaxAmt:int = obj["Rpt1ScrTotDedTaxAmt"]
      self.Rpt1ScrTotInvoiceAmt:int = obj["Rpt1ScrTotInvoiceAmt"]
      self.Rpt1ScrTotReportableAmt:int = obj["Rpt1ScrTotReportableAmt"]
      self.Rpt1ScrTotSelfAmt:int = obj["Rpt1ScrTotSelfAmt"]
      self.Rpt1ScrTotTaxableAmt:int = obj["Rpt1ScrTotTaxableAmt"]
      self.Rpt1ScrTotWithholdingAmt:int = obj["Rpt1ScrTotWithholdingAmt"]
      self.Rpt2DspInvVendorAmt:int = obj["Rpt2DspInvVendorAmt"]
      """  Invoice Vendor Amout only for dispaly in report currency  """  
      self.Rpt2InvoiceVariance:int = obj["Rpt2InvoiceVariance"]
      self.Rpt2ScrDocInvoiceAmt:int = obj["Rpt2ScrDocInvoiceAmt"]
      self.Rpt2ScrInvExpense:int = obj["Rpt2ScrInvExpense"]
      self.Rpt2ScrInvoiceAmt:int = obj["Rpt2ScrInvoiceAmt"]
      self.Rpt2ScrInvVendorAmt:int = obj["Rpt2ScrInvVendorAmt"]
      self.Rpt2ScrRounding:int = obj["Rpt2ScrRounding"]
      self.Rpt2ScrTaxAmt:int = obj["Rpt2ScrTaxAmt"]
      self.Rpt2ScrTotDedTaxAmt:int = obj["Rpt2ScrTotDedTaxAmt"]
      self.Rpt2ScrTotInvoiceAmt:int = obj["Rpt2ScrTotInvoiceAmt"]
      self.Rpt2ScrTotReportableAmt:int = obj["Rpt2ScrTotReportableAmt"]
      self.Rpt2ScrTotSelfAmt:int = obj["Rpt2ScrTotSelfAmt"]
      self.Rpt2ScrTotTaxableAmt:int = obj["Rpt2ScrTotTaxableAmt"]
      self.Rpt2ScrTotWithholdingAmt:int = obj["Rpt2ScrTotWithholdingAmt"]
      self.Rpt3DspInvVendorAmt:int = obj["Rpt3DspInvVendorAmt"]
      """  Invoice Vendor Amout only for dispaly in report currency  """  
      self.Rpt3InvoiceVariance:int = obj["Rpt3InvoiceVariance"]
      self.Rpt3ScrDocInvoiceAmt:int = obj["Rpt3ScrDocInvoiceAmt"]
      self.Rpt3ScrInvExpense:int = obj["Rpt3ScrInvExpense"]
      self.Rpt3ScrInvoiceAmt:int = obj["Rpt3ScrInvoiceAmt"]
      self.Rpt3ScrInvVendorAmt:int = obj["Rpt3ScrInvVendorAmt"]
      self.Rpt3ScrRounding:int = obj["Rpt3ScrRounding"]
      self.Rpt3ScrTaxAmt:int = obj["Rpt3ScrTaxAmt"]
      self.Rpt3ScrTotDedTaxAmt:int = obj["Rpt3ScrTotDedTaxAmt"]
      self.Rpt3ScrTotInvoiceAmt:int = obj["Rpt3ScrTotInvoiceAmt"]
      self.Rpt3ScrTotReportableAmt:int = obj["Rpt3ScrTotReportableAmt"]
      self.Rpt3ScrTotSelfAmt:int = obj["Rpt3ScrTotSelfAmt"]
      self.Rpt3ScrTotTaxableAmt:int = obj["Rpt3ScrTotTaxableAmt"]
      self.Rpt3ScrTotWithholdingAmt:int = obj["Rpt3ScrTotWithholdingAmt"]
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.ScrDiscountAmt:int = obj["ScrDiscountAmt"]
      self.ScrDocDiscountAmt:int = obj["ScrDocDiscountAmt"]
      self.ScrDocInvExpense:int = obj["ScrDocInvExpense"]
      self.ScrDocInvoiceAmt:int = obj["ScrDocInvoiceAmt"]
      self.ScrDocInvVendorAmt:int = obj["ScrDocInvVendorAmt"]
      self.ScrDocRounding:int = obj["ScrDocRounding"]
      self.ScrDocTaxAmt:int = obj["ScrDocTaxAmt"]
      self.ScrDocTotDedTaxAmt:int = obj["ScrDocTotDedTaxAmt"]
      self.ScrDocTotInvoiceAmt:int = obj["ScrDocTotInvoiceAmt"]
      self.ScrDocTotReportableAmt:int = obj["ScrDocTotReportableAmt"]
      self.ScrDocTotSelfAmt:int = obj["ScrDocTotSelfAmt"]
      self.ScrDocTotTaxableAmt:int = obj["ScrDocTotTaxableAmt"]
      self.ScrDocTotWithholdingAmt:int = obj["ScrDocTotWithholdingAmt"]
      self.ScrInvExpense:int = obj["ScrInvExpense"]
      self.ScrInvoiceAmt:int = obj["ScrInvoiceAmt"]
      self.ScrInvoiceRef:str = obj["ScrInvoiceRef"]
      self.ScrInvVendorAmt:int = obj["ScrInvVendorAmt"]
      self.ScrRounding:int = obj["ScrRounding"]
      self.ScrTaxAmt:int = obj["ScrTaxAmt"]
      self.ScrTotDedTaxAmt:int = obj["ScrTotDedTaxAmt"]
      self.ScrTotInvoiceAmt:int = obj["ScrTotInvoiceAmt"]
      self.ScrTotReportableAmt:int = obj["ScrTotReportableAmt"]
      self.ScrTotSelfAmt:int = obj["ScrTotSelfAmt"]
      self.ScrTotTaxableAmt:int = obj["ScrTotTaxableAmt"]
      self.ScrTotWithholdingAmt:int = obj["ScrTotWithholdingAmt"]
      self.SystemTranType:str = obj["SystemTranType"]
      """  System Transaction Type: APInvoice/DebitMemo is used in the filter of TranDocType combo box.  """  
      self.TaxExchangeRate:int = obj["TaxExchangeRate"]
      self.TaxLinesExist:bool = obj["TaxLinesExist"]
      self.TaxRateLinesExist:bool = obj["TaxRateLinesExist"]
      self.TotalInvAmt:int = obj["TotalInvAmt"]
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      """  Link to TranDocType table, can be removed when path field TranDocTypeID is replaced with actual one.  """  
      self.TransApplyDate:str = obj["TransApplyDate"]
      """  This field is used when invoice is transferred form one Group to another and the user has a cance to change this invoice Apply Date.  """  
      self.UpdateEntity:bool = obj["UpdateEntity"]
      """  Not intended for external use.  Logical indicating that a default entity was created for the new logged invoice.  """  
      self.UseTaxRate:bool = obj["UseTaxRate"]
      self.VendorBank:str = obj["VendorBank"]
      """  Vendor Bank  """  
      self.VendorInactive:bool = obj["VendorInactive"]
      """  Indicates if the vendor is active  """  
      self.XRateLabel:str = obj["XRateLabel"]
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      self.FormattedVendorNameAddress:str = obj["FormattedVendorNameAddress"]
      """  Formatted Supplier Name and Address  """  
      self.ManualTaxAdj:bool = obj["ManualTaxAdj"]
      """  The flag t to indicate if Tax records created per Tax Liability assigned toLogged Invoiceare adjusted, deleted,  or any tax records were added by the user  """  
      self.VendorNumFullAddress:str = obj["VendorNumFullAddress"]
      """  Supplier Full Address. External field uses the Supplier Address1, Address2, Address3, City,State, zip  and  Country from the supplier catalog  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.PurPointName:str = obj["PurPointName"]
      self.PurPointPrimPCon:int = obj["PurPointPrimPCon"]
      self.PurPointAddress1:str = obj["PurPointAddress1"]
      self.PurPointState:str = obj["PurPointState"]
      self.PurPointAddress2:str = obj["PurPointAddress2"]
      self.PurPointAddress3:str = obj["PurPointAddress3"]
      self.PurPointZip:str = obj["PurPointZip"]
      self.PurPointCountry:str = obj["PurPointCountry"]
      self.PurPointCity:str = obj["PurPointCity"]
      self.RateGrpCodeDescription:str = obj["RateGrpCodeDescription"]
      self.SEPayMethodName:str = obj["SEPayMethodName"]
      self.SEPayMethodType:int = obj["SEPayMethodType"]
      self.SEPayMethodSummarizePerCustomer:bool = obj["SEPayMethodSummarizePerCustomer"]
      self.TaxRateGrpDescription:str = obj["TaxRateGrpDescription"]
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      self.TermsCodeDescription:str = obj["TermsCodeDescription"]
      self.UserfileName:str = obj["UserfileName"]
      self.VendBankSwiftNum:str = obj["VendBankSwiftNum"]
      self.VendBankBankName:str = obj["VendBankBankName"]
      self.VendBankBankGiroAcctNbr:str = obj["VendBankBankGiroAcctNbr"]
      self.VendBankIBANCode:str = obj["VendBankIBANCode"]
      self.VendBankBankAcctNumber:str = obj["VendBankBankAcctNumber"]
      self.VendBankPMUID:int = obj["VendBankPMUID"]
      self.VendBankCardCode:str = obj["VendBankCardCode"]
      self.VendBankLocalBIC:str = obj["VendBankLocalBIC"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VoidedByName:str = obj["VoidedByName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LogAPInvTaxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead it is assigned from the Vendor.VendorNum using VendorID to find the Vendor record.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Vendor's invoice number.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.ECAcquisitionSeq:int = obj["ECAcquisitionSeq"]
      """   Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.
NOTE:  This field is now used in VAT Reverse Charge logic.  If an invoice line is marked for Reverse Charge, a second line is created just like in the ECAcquisition logic. To distinguish the two scenarios, the ReverseCharge flag will be set to true if the second line is for Reverse Charge.  """  
      self.RateCode:str = obj["RateCode"]
      """  Rate Code  """  
      self.Void:bool = obj["Void"]
      """  Indicates if this logged invoice has been voided.  """  
      self.ReverseCharge:bool = obj["ReverseCharge"]
      """  Indicates if this tax line is for a Reverse Charge.  """  
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  Taxable amount for this invoice.  Manually entered if APInvTax.Manual = Yes else set equal to SysCalcTaxableAmt.  """  
      self.DocTaxableAmt:int = obj["DocTaxableAmt"]
      """  Taxable amount for this invoice in foreign currency. Manually entered if APInvTax.Manual = Yes else it is set equal to SysCalcDocTaxableAmt.  """  
      self.Rpt1TaxableAmt:int = obj["Rpt1TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxableAmt:int = obj["Rpt2TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxableAmt:int = obj["Rpt3TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Percent:int = obj["Percent"]
      """  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """   Sales Tax amount for the corresponding taxable sales amount.
Manually entered if APInvTax.Manual = Yes.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount in foreign currency.  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.ReportableAmt:int = obj["ReportableAmt"]
      """  The reportable sales amount to the tax jurisdiction. Set the value as follows; first determine if the item needs to be reported to the tax jurisdiction.  This is done by using the  APInvDtl.TaxCode and APInvDtl/APInvMisc.TaxCat to find a record in the SalesTxC. If a record is not found or SalesTxC.Reportable = Yes then add in the line item extended amount or if this is for a InvcMisc record InvcMisc.Amount. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcReportableAmt.  """  
      self.DocReportableAmt:int = obj["DocReportableAmt"]
      """  The reportable sales amount to the tax jurisdiction expressed in the Vendor's currency. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcDocTaxableAmt.  """  
      self.Rpt1ReportableAmt:int = obj["Rpt1ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2ReportableAmt:int = obj["Rpt2ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3ReportableAmt:int = obj["Rpt3ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Manual:bool = obj["Manual"]
      """  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  """  
      self.SysCalcTaxableAmt:int = obj["SysCalcTaxableAmt"]
      """  System calculated Taxable amount for this invoice.  """  
      self.SysCalcDocTaxableAmt:int = obj["SysCalcDocTaxableAmt"]
      """  System calculated Taxable amount for this invoice in foreign currency.  """  
      self.Rpt1SysCalcTaxableAmt:int = obj["Rpt1SysCalcTaxableAmt"]
      """  System calculated Taxable amount for this invoice.  """  
      self.Rpt2SysCalcTaxableAmt:int = obj["Rpt2SysCalcTaxableAmt"]
      """  System calculated Taxable amount for this invoice.  """  
      self.Rpt3SysCalcTaxableAmt:int = obj["Rpt3SysCalcTaxableAmt"]
      """  System calculated Taxable amount for this invoice.  """  
      self.SysCalcReportableAmt:int = obj["SysCalcReportableAmt"]
      """  System calculated reportable sales amount to the tax jurisdiction. Set the value as follows; first determine if the item needs to be reported to the tax jurisdiction.  This is done by using the  APInvDtl.TaxCode and APInvDtl/APInvMisc.TaxCat to find a record in the SalesTxC. If a record is not found or SalesTxC.Reportable = Yes then add in the line item extended amount or if this is for a InvcMisc record InvcMisc.Amount.  """  
      self.SysCalcDocReportableAmt:int = obj["SysCalcDocReportableAmt"]
      """  System calculated reportable sales amount to the tax jurisdiction expressed in the Vendor's currency.  """  
      self.Rpt1SysCalcReportableAmt:int = obj["Rpt1SysCalcReportableAmt"]
      """  System calculated reportable sales amount to the tax jurisdiction. Set the value as follows; first determine if the item needs to be reported to the tax jurisdiction.  This is done by using the  APInvDtl.TaxCode and APInvDtl/APInvMisc.TaxCat to find a record in the SalesTxC. If a record is not found or SalesTxC.Reportable = Yes then add in the line item extended amount or if this is for a InvcMisc record InvcMisc.Amount.  """  
      self.Rpt2SysCalcReportableAmt:int = obj["Rpt2SysCalcReportableAmt"]
      """  System calculated reportable sales amount to the tax jurisdiction. Set the value as follows; first determine if the item needs to be reported to the tax jurisdiction.  This is done by using the  APInvDtl.TaxCode and APInvDtl/APInvMisc.TaxCat to find a record in the SalesTxC. If a record is not found or SalesTxC.Reportable = Yes then add in the line item extended amount or if this is for a InvcMisc record InvcMisc.Amount.  """  
      self.Rpt3SysCalcReportableAmt:int = obj["Rpt3SysCalcReportableAmt"]
      """  System calculated reportable sales amount to the tax jurisdiction. Set the value as follows; first determine if the item needs to be reported to the tax jurisdiction.  This is done by using the  APInvDtl.TaxCode and APInvDtl/APInvMisc.TaxCat to find a record in the SalesTxC. If a record is not found or SalesTxC.Reportable = Yes then add in the line item extended amount or if this is for a InvcMisc record InvcMisc.Amount.  """  
      self.CollectionType:int = obj["CollectionType"]
      """  Collection Type  """  
      self.Timing:int = obj["Timing"]
      """  Timing of when to report taxes  """  
      self.ExemptType:int = obj["ExemptType"]
      """  Exemption Type  """  
      self.ExemptPercent:int = obj["ExemptPercent"]
      """  Exemption Percent  """  
      self.ResolutionNum:str = obj["ResolutionNum"]
      """  Resolution number  """  
      self.ResolutionDate:str = obj["ResolutionDate"]
      """  Resolution Date  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Tax Rate Date  """  
      self.DefTaxableAmt:int = obj["DefTaxableAmt"]
      """  Balance of the Taxable amount that has been deferred until payment  """  
      self.DocDefTaxableAmt:int = obj["DocDefTaxableAmt"]
      """  Balance of the Taxable amount that has been deferred until payment  """  
      self.Rpt1DefTaxableAmt:int = obj["Rpt1DefTaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DefTaxableAmt:int = obj["Rpt2DefTaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DefTaxableAmt:int = obj["Rpt3DefTaxableAmt"]
      """  Reporting currency value of this field  """  
      self.DefTaxAmt:int = obj["DefTaxAmt"]
      """  Balance of the Tax amount that has been deferred until payment  """  
      self.DocDefTaxAmt:int = obj["DocDefTaxAmt"]
      """  Balance of the Tax amount that has been deferred until payment  """  
      self.Rpt1DefTaxAmt:int = obj["Rpt1DefTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DefTaxAmt:int = obj["Rpt2DefTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DefTaxAmt:int = obj["Rpt3DefTaxAmt"]
      """  Reporting currency value of this field  """  
      self.ManAdd:bool = obj["ManAdd"]
      """  This record was manually added (not in Liability) but will use the standard calculations  """  
      self.DedTaxAmt:int = obj["DedTaxAmt"]
      """  Deducatable Tax Amount  """  
      self.DocDedTaxAmt:int = obj["DocDedTaxAmt"]
      """  Deducatable Tax Amount  """  
      self.Rpt1DedTaxAmt:int = obj["Rpt1DedTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DedTaxAmt:int = obj["Rpt2DedTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DedTaxAmt:int = obj["Rpt3DedTaxAmt"]
      """  Reporting currency value of this field  """  
      self.FixedAmount:int = obj["FixedAmount"]
      """  Fixed Tax Amount  """  
      self.DocFixedAmount:int = obj["DocFixedAmount"]
      """  Document Fixed Tax Amount  """  
      self.Rpt1FixedAmount:int = obj["Rpt1FixedAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt2FixedAmount:int = obj["Rpt2FixedAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt3FixedAmount:int = obj["Rpt3FixedAmount"]
      """  Reporting currency value of this field  """  
      self.TextCode:str = obj["TextCode"]
      """  Unique Identifier for Legal Text  """  
      self.TaxAmtVar:int = obj["TaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.DocTaxAmtVar:int = obj["DocTaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.Rpt1TaxAmtVar:int = obj["Rpt1TaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.Rpt2TaxAmtVar:int = obj["Rpt2TaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.Rpt3TaxAmtVar:int = obj["Rpt3TaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MovementNum:int = obj["MovementNum"]
      """  MovementNum  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.DebitMemo:bool = obj["DebitMemo"]
      self.DescCollectionType:str = obj["DescCollectionType"]
      """  Collection Type Description  """  
      self.EnableSuperGRate:bool = obj["EnableSuperGRate"]
      self.GroupID:str = obj["GroupID"]
      self.Posted:bool = obj["Posted"]
      self.RateType:int = obj["RateType"]
      self.Rpt1ScrDedTaxAmt:int = obj["Rpt1ScrDedTaxAmt"]
      self.Rpt1ScrFixedAmount:int = obj["Rpt1ScrFixedAmount"]
      """  Display field for Fixed Amount in Report Currency 1.  """  
      self.Rpt1ScrReportableAmt:int = obj["Rpt1ScrReportableAmt"]
      self.Rpt1ScrTaxableAmt:int = obj["Rpt1ScrTaxableAmt"]
      self.Rpt1ScrTaxAmt:int = obj["Rpt1ScrTaxAmt"]
      self.Rpt1ScrTaxAmtVar:int = obj["Rpt1ScrTaxAmtVar"]
      self.Rpt2ScrDedTaxAmt:int = obj["Rpt2ScrDedTaxAmt"]
      self.Rpt2ScrFixedAmount:int = obj["Rpt2ScrFixedAmount"]
      """  Display field for Fixed Amount in Report Currency 2.  """  
      self.Rpt2ScrReportableAm:int = obj["Rpt2ScrReportableAm"]
      self.Rpt2ScrReportableAmt:int = obj["Rpt2ScrReportableAmt"]
      self.Rpt2ScrTaxableAmt:int = obj["Rpt2ScrTaxableAmt"]
      self.Rpt2ScrTaxAmt:int = obj["Rpt2ScrTaxAmt"]
      self.Rpt2ScrTaxAmtVar:int = obj["Rpt2ScrTaxAmtVar"]
      self.Rpt3ScrDedTaxAmt:int = obj["Rpt3ScrDedTaxAmt"]
      self.Rpt3ScrFixedAmount:int = obj["Rpt3ScrFixedAmount"]
      """  Display field for Fixed Amount in Report Currency 31.  """  
      self.Rpt3ScrReportableAmt:int = obj["Rpt3ScrReportableAmt"]
      self.Rpt3ScrTaxableAmt:int = obj["Rpt3ScrTaxableAmt"]
      self.Rpt3ScrTaxAmt:int = obj["Rpt3ScrTaxAmt"]
      self.Rpt3ScrTaxAmtVar:int = obj["Rpt3ScrTaxAmtVar"]
      self.ScrDedTaxAmt:int = obj["ScrDedTaxAmt"]
      self.ScrDocDedTaxAmt:int = obj["ScrDocDedTaxAmt"]
      self.ScrDocFixedAmount:int = obj["ScrDocFixedAmount"]
      """  Display field for Fixed amount in document currency  """  
      self.ScrDocReportableAmt:int = obj["ScrDocReportableAmt"]
      self.ScrDocTaxableAmt:int = obj["ScrDocTaxableAmt"]
      self.ScrDocTaxAmt:int = obj["ScrDocTaxAmt"]
      self.ScrDocTaxAmtVar:int = obj["ScrDocTaxAmtVar"]
      self.ScrFixedAmount:int = obj["ScrFixedAmount"]
      """  Display field for Fixed Amount  """  
      self.ScrReportableAmt:int = obj["ScrReportableAmt"]
      self.ScrTaxableAmt:int = obj["ScrTaxableAmt"]
      self.ScrTaxAmt:int = obj["ScrTaxAmt"]
      self.ScrTaxAmtVar:int = obj["ScrTaxAmtVar"]
      self.DisableManual:bool = obj["DisableManual"]
      """  Flag to indicate if Manual field on tax record should be disabled  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RateCodeDescription:str = obj["RateCodeDescription"]
      self.TaxCodeDescription:str = obj["TaxCodeDescription"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LogInvAprvVoidTableset:
   def __init__(self, obj):
      self.LogAPInv:list[Erp_Tablesets_LogAPInvRow] = obj["LogAPInv"]
      self.LogAPInvAttch:list[Erp_Tablesets_LogAPInvAttchRow] = obj["LogAPInvAttch"]
      self.LogAPInvTax:list[Erp_Tablesets_LogAPInvTaxRow] = obj["LogAPInvTax"]
      self.EntityGLC:list[Erp_Tablesets_EntityGLCRow] = obj["EntityGLC"]
      self.LegalNumberGenerate:list[Erp_Tablesets_LegalNumberGenerateRow] = obj["LegalNumberGenerate"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtLogInvAprvVoidTableset:
   def __init__(self, obj):
      self.LogAPInv:list[Erp_Tablesets_LogAPInvRow] = obj["LogAPInv"]
      self.LogAPInvAttch:list[Erp_Tablesets_LogAPInvAttchRow] = obj["LogAPInvAttch"]
      self.LogAPInvTax:list[Erp_Tablesets_LogAPInvTaxRow] = obj["LogAPInvTax"]
      self.EntityGLC:list[Erp_Tablesets_EntityGLCRow] = obj["EntityGLC"]
      self.LegalNumberGenerate:list[Erp_Tablesets_LegalNumberGenerateRow] = obj["LegalNumberGenerate"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   vendorNum
   invoiceNum
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      self.invoiceNum:str = obj["invoiceNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LogInvAprvVoidTableset] = obj["returnObj"]
      pass

class GetBySysRowID_input:
   """ Required : 
   id
   """  
   def __init__(self, obj):
      self.id:str = obj["id"]
      pass

class GetBySysRowID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LogInvAprvVoidTableset] = obj["returnObj"]
      pass

class GetBySysRowIDs_input:
   """ Required : 
   ids
   """  
   def __init__(self, obj):
      self.ids:str = obj["ids"]
      pass

class GetBySysRowIDs_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LogInvAprvVoidTableset] = obj["returnObj"]
      pass

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LogAPInvListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewEntityGLC_input:
   """ Required : 
   ds
   relatedToFile
   key1
   key2
   key3
   key4
   key5
   key6
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LogInvAprvVoidTableset] = obj["ds"]
      self.relatedToFile:str = obj["relatedToFile"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.key4:str = obj["key4"]
      self.key5:str = obj["key5"]
      self.key6:str = obj["key6"]
      pass

class GetNewEntityGLC_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LogInvAprvVoidTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewLegalNumberGenerate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LogInvAprvVoidTableset] = obj["ds"]
      pass

class GetNewLegalNumberGenerate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LogInvAprvVoidTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewLogAPInvAttch_input:
   """ Required : 
   ds
   vendorNum
   invoiceNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LogInvAprvVoidTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      self.invoiceNum:str = obj["invoiceNum"]
      pass

class GetNewLogAPInvAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LogInvAprvVoidTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewLogAPInvTax_input:
   """ Required : 
   ds
   vendorNum
   invoiceNum
   taxCode
   rateCode
   ecAcquisitionSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LogInvAprvVoidTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      self.invoiceNum:str = obj["invoiceNum"]
      self.taxCode:str = obj["taxCode"]
      self.rateCode:str = obj["rateCode"]
      self.ecAcquisitionSeq:int = obj["ecAcquisitionSeq"]
      pass

class GetNewLogAPInvTax_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LogInvAprvVoidTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewLogAPInv_input:
   """ Required : 
   ds
   vendorNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LogInvAprvVoidTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      pass

class GetNewLogAPInv_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LogInvAprvVoidTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseLogAPInv
   whereClauseLogAPInvAttch
   whereClauseLogAPInvTax
   whereClauseEntityGLC
   whereClauseLegalNumberGenerate
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseLogAPInv:str = obj["whereClauseLogAPInv"]
      self.whereClauseLogAPInvAttch:str = obj["whereClauseLogAPInvAttch"]
      self.whereClauseLogAPInvTax:str = obj["whereClauseLogAPInvTax"]
      self.whereClauseEntityGLC:str = obj["whereClauseEntityGLC"]
      self.whereClauseLegalNumberGenerate:str = obj["whereClauseLegalNumberGenerate"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LogInvAprvVoidTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class Ice_BOUpdErrorRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      self.ErrorLevel:str = obj["ErrorLevel"]
      self.ErrorType:str = obj["ErrorType"]
      self.ErrorText:str = obj["ErrorText"]
      self.ErrorSysRowID:str = obj["ErrorSysRowID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_BOUpdErrorTableset:
   def __init__(self, obj):
      self.BOUpdError:list[Ice_BOUpdErrorRow] = obj["BOUpdError"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Extensions_ExtensionRow:
   def __init__(self, obj):
      self.ColumnValues:object
      self.RowMod:str = obj["RowMod"]
      self.SysRowID:str = obj["SysRowID"]
      pass

class Ice_Extensions_ExtensionTableColumn:
   def __init__(self, obj):
      self.ColumnName:str = obj["ColumnName"]
      self.ColumnType:str = obj["ColumnType"]
      pass

class Ice_Extensions_ExtensionTableData:
   def __init__(self, obj):
      self.Table:list[Ice_Extensions_ExtensionRow] = obj["Table"]
      self.SystemCode:str = obj["SystemCode"]
      self.TableName:str = obj["TableName"]
      self.Columns:list[Ice_Extensions_ExtensionTableColumn] = obj["Columns"]
      self.PrimaryKeyColumns:str = obj["PrimaryKeyColumns"]
      self.PeerTableSystemCode:str = obj["PeerTableSystemCode"]
      self.PeerTableName:str = obj["PeerTableName"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtLogInvAprvVoidTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtLogInvAprvVoidTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LogInvAprvVoidTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LogInvAprvVoidTableset] = obj["ds"]
      pass

      """  output parameters  """  

class VoidLoggedInvoice_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LogInvAprvVoidTableset] = obj["ds"]
      pass

class VoidLoggedInvoice_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LogInvAprvVoidTableset] = obj["ds"]
      pass

      """  output parameters  """  

