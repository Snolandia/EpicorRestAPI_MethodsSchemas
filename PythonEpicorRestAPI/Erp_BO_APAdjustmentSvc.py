import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.APAdjustmentSvc
# Description: APAdjustment Service
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APAdjustmentSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APAdjustmentSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_APAdjustments(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get APAdjustments items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APAdjustments
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APInvHedAdjRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APAdjustmentSvc/APAdjustments",headers=creds) as resp:
           return await resp.json()

async def post_APAdjustments(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APAdjustments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APInvHedAdjRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.APInvHedAdjRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APAdjustmentSvc/APAdjustments", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_APAdjustments_Company_VendorNum_InvoiceNum(Company, VendorNum, InvoiceNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the APAdjustment item
   Description: Calls GetByID to retrieve the APAdjustment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APAdjustment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APInvHedAdjRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APAdjustmentSvc/APAdjustments(" + Company + "," + VendorNum + "," + InvoiceNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_APAdjustments_Company_VendorNum_InvoiceNum(Company, VendorNum, InvoiceNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update APAdjustment for the service
   Description: Calls UpdateExt to update APAdjustment. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APAdjustment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.APInvHedAdjRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.APAdjustmentSvc/APAdjustments(" + Company + "," + VendorNum + "," + InvoiceNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_APAdjustments_Company_VendorNum_InvoiceNum(Company, VendorNum, InvoiceNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete APAdjustment item
   Description: Call UpdateExt to delete APAdjustment item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APAdjustment
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.APAdjustmentSvc/APAdjustments(" + Company + "," + VendorNum + "," + InvoiceNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_APAdjustments_Company_VendorNum_InvoiceNum_APTrans(Company, VendorNum, InvoiceNum, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get APTrans items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_APTrans1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APTranRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APAdjustmentSvc/APAdjustments(" + Company + "," + VendorNum + "," + InvoiceNum + ")/APTrans",headers=creds) as resp:
           return await resp.json()

async def get_APAdjustments_Company_VendorNum_InvoiceNum_APTrans_Company_HeadNum_APTranNo_InvoiceNum_Voided(Company, VendorNum, InvoiceNum, HeadNum, APTranNo, Voided, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the APTran item
   Description: Calls GetByID to retrieve the APTran item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APTran1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param APTranNo: Desc: APTranNo   Required: True
      :param Voided: Desc: Voided   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APTranRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APAdjustmentSvc/APAdjustments(" + Company + "," + VendorNum + "," + InvoiceNum + ")/APTrans(" + Company + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + Voided + ")",headers=creds) as resp:
           return await resp.json()

async def get_APTrans(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get APTrans items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APTrans
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APTranRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APAdjustmentSvc/APTrans",headers=creds) as resp:
           return await resp.json()

async def post_APTrans(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APTrans
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APTranRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.APTranRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APAdjustmentSvc/APTrans", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_APTrans_Company_HeadNum_APTranNo_InvoiceNum_Voided(Company, HeadNum, APTranNo, InvoiceNum, Voided, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the APTran item
   Description: Calls GetByID to retrieve the APTran item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APTran
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param APTranNo: Desc: APTranNo   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param Voided: Desc: Voided   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APTranRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APAdjustmentSvc/APTrans(" + Company + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + Voided + ")",headers=creds) as resp:
           return await resp.json()

async def patch_APTrans_Company_HeadNum_APTranNo_InvoiceNum_Voided(Company, HeadNum, APTranNo, InvoiceNum, Voided, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update APTran for the service
   Description: Calls UpdateExt to update APTran. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APTran
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param APTranNo: Desc: APTranNo   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param Voided: Desc: Voided   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.APTranRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.APAdjustmentSvc/APTrans(" + Company + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + Voided + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_APTrans_Company_HeadNum_APTranNo_InvoiceNum_Voided(Company, HeadNum, APTranNo, InvoiceNum, Voided, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete APTran item
   Description: Call UpdateExt to delete APTran item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APTran
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param APTranNo: Desc: APTranNo   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param Voided: Desc: Voided   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.APAdjustmentSvc/APTrans(" + Company + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + Voided + ")",headers=creds) as resp:
           return await resp.json()

async def get_APTrans_Company_HeadNum_APTranNo_InvoiceNum_Voided_APTranTGLCs(Company, HeadNum, APTranNo, InvoiceNum, Voided, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get APTranTGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_APTranTGLCs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param APTranNo: Desc: APTranNo   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param Voided: Desc: Voided   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APTranTGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APAdjustmentSvc/APTrans(" + Company + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + Voided + ")/APTranTGLCs",headers=creds) as resp:
           return await resp.json()

async def get_APTrans_Company_HeadNum_APTranNo_InvoiceNum_Voided_APTranTGLCs_Company_HeadNum_APTranNo_InvoiceNum_Voided_SysRowID(Company, HeadNum, APTranNo, InvoiceNum, Voided, SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the APTranTGLC item
   Description: Calls GetByID to retrieve the APTranTGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APTranTGLC1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param APTranNo: Desc: APTranNo   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param Voided: Desc: Voided   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APTranTGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APAdjustmentSvc/APTrans(" + Company + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + Voided + ")/APTranTGLCs(" + Company + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + Voided + "," + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_APTranTGLCs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get APTranTGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APTranTGLCs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APTranTGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APAdjustmentSvc/APTranTGLCs",headers=creds) as resp:
           return await resp.json()

async def post_APTranTGLCs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APTranTGLCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APTranTGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.APTranTGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APAdjustmentSvc/APTranTGLCs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_APTranTGLCs_Company_HeadNum_APTranNo_InvoiceNum_Voided_SysRowID(Company, HeadNum, APTranNo, InvoiceNum, Voided, SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the APTranTGLC item
   Description: Calls GetByID to retrieve the APTranTGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APTranTGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param APTranNo: Desc: APTranNo   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param Voided: Desc: Voided   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APTranTGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APAdjustmentSvc/APTranTGLCs(" + Company + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + Voided + "," + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_APTranTGLCs_Company_HeadNum_APTranNo_InvoiceNum_Voided_SysRowID(Company, HeadNum, APTranNo, InvoiceNum, Voided, SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update APTranTGLC for the service
   Description: Calls UpdateExt to update APTranTGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APTranTGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param APTranNo: Desc: APTranNo   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param Voided: Desc: Voided   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.APTranTGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.APAdjustmentSvc/APTranTGLCs(" + Company + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + Voided + "," + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_APTranTGLCs_Company_HeadNum_APTranNo_InvoiceNum_Voided_SysRowID(Company, HeadNum, APTranNo, InvoiceNum, Voided, SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete APTranTGLC item
   Description: Call UpdateExt to delete APTranTGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APTranTGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param APTranNo: Desc: APTranNo   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param Voided: Desc: Voided   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.APAdjustmentSvc/APTranTGLCs(" + Company + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + Voided + "," + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_LegalNumGenOpts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LegalNumGenOpts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LegalNumGenOpts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LegalNumGenOptsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APAdjustmentSvc/LegalNumGenOpts",headers=creds) as resp:
           return await resp.json()

async def post_LegalNumGenOpts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LegalNumGenOpts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APAdjustmentSvc/LegalNumGenOpts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LegalNumGenOpts_Company_LegalNumberID(Company, LegalNumberID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LegalNumGenOpt item
   Description: Calls GetByID to retrieve the LegalNumGenOpt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LegalNumGenOpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APAdjustmentSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LegalNumGenOpts_Company_LegalNumberID(Company, LegalNumberID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LegalNumGenOpt for the service
   Description: Calls UpdateExt to update LegalNumGenOpt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LegalNumGenOpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.APAdjustmentSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LegalNumGenOpts_Company_LegalNumberID(Company, LegalNumberID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LegalNumGenOpt item
   Description: Call UpdateExt to delete LegalNumGenOpt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LegalNumGenOpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.APAdjustmentSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APInvHedAdjListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APAdjustmentSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseAPInvHedAdj, whereClauseAPTran, whereClauseAPTranTGLC, whereClauseLegalNumGenOpts, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
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
   params += "whereClauseAPInvHedAdj=" + whereClauseAPInvHedAdj
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAPTran=" + whereClauseAPTran
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAPTranTGLC=" + whereClauseAPTranTGLC
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseLegalNumGenOpts=" + whereClauseLegalNumGenOpts
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APAdjustmentSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APAdjustmentSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APAdjustmentSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ChangeAdjAmount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeAdjAmount
   Description: This method updates the APTran amounts when the adjustment amount changes or
the currency switch toggles.
   OperationID: ChangeAdjAmount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeAdjAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeAdjAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APAdjustmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCopyRate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCopyRate
   Description: This method updates exchange rate for the transaction and update currency gain/loss
date changes.
   OperationID: ChangeCopyRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCopyRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCopyRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APAdjustmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeGLAcctDisp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeGLAcctDisp
   Description: This method updates the GLAcctDisp when the transaction
G/L Account changes.
   OperationID: ChangeGLAcctDisp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeGLAcctDisp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeGLAcctDisp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APAdjustmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRateGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRateGroup
   Description: Purpose:
Parameters:
<param name="ipRateGroupCode">rate group code for adjustment</param><param name="ds">The A/P Adjustment Entry data set </param>
   OperationID: ChangeRateGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRateGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRateGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APAdjustmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTranDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTranDate
   Description: This method updates the APTran fiscal period and year when the transaction
date changes.
   OperationID: ChangeTranDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTranDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTranDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APAdjustmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckGLInterface(epicorHeaders = None):
   """  
   Summary: Invoke method CheckGLInterface
   Description: Call this method once to validate the G/L Interface.  This method checks for
GLSyst availability and if G/L is interfaced with A/P. If A/P is not interfaced
with G/L then user should be asked if okay to continue without posting to G/L.
This method will return a Message for the user if not interfaced else the Message
is blank. If the user do not wish to continue then exit this object. This method
also returns a logical flag to indicate if Posting to G/L.  This value should be
passed on to each new A/P Adjustment (APTran) record to process.
   OperationID: CheckGLInterface
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckGLInterface_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APAdjustmentSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetNewAPTran1(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAPTran1
   Description: This method is to be used in place of GetNewAPTran.  This method asks for
vendor number and invoice number to link the A/P Invoice Header (APInvHed)
to A/P Invoice Adjustment (APTran).
   OperationID: GetNewAPTran1
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAPTran1_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPTran1_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APAdjustmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   Description: This method updates the APTran fiscal period and year when the transaction
date changes.
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APAdjustmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAvailTranDocTypes(epicorHeaders = None):
   """  
   Summary: Invoke method GetAvailTranDocTypes
   Description: Gets available TranDocTypes for APAdjust Type
   OperationID: GetAvailTranDocTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailTranDocTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APAdjustmentSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_PreUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreUpdate
   Description: Checks if the user needs to provide a prefix for manual legal numbers
   OperationID: PreUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APAdjustmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAPInvHedAdj(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAPInvHedAdj
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAPInvHedAdj
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAPInvHedAdj_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPInvHedAdj_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APAdjustmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAPTran(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAPTran
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAPTran
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAPTran_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPTran_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APAdjustmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAPTranTGLC(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAPTranTGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAPTranTGLC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAPTranTGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPTranTGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APAdjustmentSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APAdjustmentSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APAdjustmentSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APAdjustmentSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APAdjustmentSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APAdjustmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APInvHedAdjListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_APInvHedAdjListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APInvHedAdjRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_APInvHedAdjRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APTranRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_APTranRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APTranTGLCRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_APTranTGLCRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["value"]
      pass

class Erp_Tablesets_APInvHedAdjListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenPayable:bool = obj["OpenPayable"]
      """  Indicates if this is an "open" Payable.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead it is assigned from the Vendor.VendorNum using VendorID to find the Vendor record.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Vendor's invoice number.  """  
      self.DebitMemo:bool = obj["DebitMemo"]
      """   Indicates the type of document. Yes = Debit Memo,  No= Invoice. This value can't be changed after the record has been created.
Debit memos affect the way detail quantities and amounts are stored in the database. They will always be stored with a negative sign, but are entered as a positive.
The system uses this field to test for Debit Memos,  indicated by "DM" following the invoice number.  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice date.  """  
      self.DueDate:str = obj["DueDate"]
      """  The due date of the earliest unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates if this invoice has been Posted to the open payables file.    Only invoices that have been Posted (true) will be included as part of the open payables, that is they will not appear on reports or inquiries other than those used within invoice entry. Otherwise they are considered as still being in data entry. This field is always "no" when the invoice is created. It is set to "yes"  by the  "Post function". Once an invoice is posted it can't be maintained via data entry.  """  
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      """  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (APInvDtl) and of the miscellaneous charges/credits (APInvMsc) records.  This field has a true sign. (debit memos are negative).  """  
      self.DocInvoiceAmt:int = obj["DocInvoiceAmt"]
      """  Total invoice Amount.(Vendors Currency) This field is an accumulation of the extended net amounts of the detail line items (APInvDtl) and of the miscellaneous charges/credits (APInvMsc) records.  This field has a true sign. (debit memos are negative).  """  
      self.InvoiceBal:int = obj["InvoiceBal"]
      """  Current outstanding balance. Carries a true sign. (Credit memos are negative).  """  
      self.DocInvoiceBal:int = obj["DocInvoiceBal"]
      """  Current outstanding balance.(Vendors currency)  Carries a true sign. (Credit memos are negative).  """  
      self.UnpostedBal:int = obj["UnpostedBal"]
      """  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  """  
      self.DocUnpostedBal:int = obj["DocUnpostedBal"]
      """  Current outstanding balance which includes the unposted cash receipt amounts(Vendors currency). This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  """  
      self.InvoiceHeld:bool = obj["InvoiceHeld"]
      """  Invoices that are within a data entry group can be put on "Hold". They will not be posted until InvoiceHeld=No. This flag can be used for whatever the reason the user may wish to keep an invoice in a data entry group from being posted.  This is NOT the same thing as putting an invoice on PaymentHold.  """  
      self.Description:str = obj["Description"]
      """  A short description that can be used to explain what this invoice is for. Ex: Rent, Auto Lease Payment.  This description is defaulted into the APTran.Description field when payments are made against the invoice.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.Rpt1InvoiceAmt:int = obj["Rpt1InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2InvoiceAmt:int = obj["Rpt2InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3InvoiceAmt:int = obj["Rpt3InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1InvoiceBal:int = obj["Rpt1InvoiceBal"]
      """  Reporting currency value of this field  """  
      self.Rpt2InvoiceBal:int = obj["Rpt2InvoiceBal"]
      """  Reporting currency value of this field  """  
      self.Rpt3InvoiceBal:int = obj["Rpt3InvoiceBal"]
      """  Reporting currency value of this field  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  The date this invoice will get applied to the books when it is posted.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      """  Currency Switch  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for BASE  """  
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
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
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APInvHedAdjRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenPayable:bool = obj["OpenPayable"]
      """  Indicates if this is an "open" Payable.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead it is assigned from the Vendor.VendorNum using VendorID to find the Vendor record.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Vendor's invoice number.  """  
      self.DebitMemo:bool = obj["DebitMemo"]
      """   Indicates the type of document. Yes = Debit Memo,  No= Invoice. This value can't be changed after the record has been created.
Debit memos affect the way detail quantities and amounts are stored in the database. They will always be stored with a negative sign, but are entered as a positive.
The system uses this field to test for Debit Memos,  indicated by "DM" following the invoice number.  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice date.  """  
      self.DueDate:str = obj["DueDate"]
      """  The due date of the earliest unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates if this invoice has been Posted to the open payables file.    Only invoices that have been Posted (true) will be included as part of the open payables, that is they will not appear on reports or inquiries other than those used within invoice entry. Otherwise they are considered as still being in data entry. This field is always "no" when the invoice is created. It is set to "yes"  by the  "Post function". Once an invoice is posted it can't be maintained via data entry.  """  
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      """  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (APInvDtl) and of the miscellaneous charges/credits (APInvMsc) records.  This field has a true sign. (debit memos are negative).  """  
      self.DocInvoiceAmt:int = obj["DocInvoiceAmt"]
      """  Total invoice Amount.(Vendors Currency) This field is an accumulation of the extended net amounts of the detail line items (APInvDtl) and of the miscellaneous charges/credits (APInvMsc) records.  This field has a true sign. (debit memos are negative).  """  
      self.InvoiceBal:int = obj["InvoiceBal"]
      """  Current outstanding balance. Carries a true sign. (Credit memos are negative).  """  
      self.DocInvoiceBal:int = obj["DocInvoiceBal"]
      """  Current outstanding balance.(Vendors currency)  Carries a true sign. (Credit memos are negative).  """  
      self.UnpostedBal:int = obj["UnpostedBal"]
      """  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  """  
      self.DocUnpostedBal:int = obj["DocUnpostedBal"]
      """  Current outstanding balance which includes the unposted cash receipt amounts(Vendors currency). This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  """  
      self.InvoiceHeld:bool = obj["InvoiceHeld"]
      """  Invoices that are within a data entry group can be put on "Hold". They will not be posted until InvoiceHeld=No. This flag can be used for whatever the reason the user may wish to keep an invoice in a data entry group from being posted.  This is NOT the same thing as putting an invoice on PaymentHold.  """  
      self.Description:str = obj["Description"]
      """  A short description that can be used to explain what this invoice is for. Ex: Rent, Auto Lease Payment.  This description is defaulted into the APTran.Description field when payments are made against the invoice.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.Rpt1InvoiceAmt:int = obj["Rpt1InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2InvoiceAmt:int = obj["Rpt2InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3InvoiceAmt:int = obj["Rpt3InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1InvoiceBal:int = obj["Rpt1InvoiceBal"]
      """  Reporting currency value of this field  """  
      self.Rpt2InvoiceBal:int = obj["Rpt2InvoiceBal"]
      """  Reporting currency value of this field  """  
      self.Rpt3InvoiceBal:int = obj["Rpt3InvoiceBal"]
      """  Reporting currency value of this field  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  The date this invoice will get applied to the books when it is posted.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      """  Currency Switch  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for BASE  """  
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.CorrectionInvNeg:bool = obj["CorrectionInvNeg"]
      """  Indictes if the invoice being adjusted  is Correction Invoice with negative amount  """  
      self.CopyRate:bool = obj["CopyRate"]
      """  If Copy Rate is true then original AP Invoice exchange rates are used when Adjustmet is applied and no currency gain/loss are calculated  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APTranRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TranType:str = obj["TranType"]
      """  An internal flag which identifies the type of transaction. Valid types are "Pay" or "Adj".  """  
      self.HeadNum:int = obj["HeadNum"]
      """  If TranType = "Pay" or "ADJ" for a currency gain/loss  then this is a duplicate of the related CheckHed.HeadNum,  otherwise it is set to zero.  """  
      self.APTranNo:int = obj["APTranNo"]
      """  Integer assigned by the system which is used as one of the fields to uniquely identify the APTran record.  If (TranType = "Pay"  and InvoiceNum = "") or (TranType = "Adj") it is assigned a unique #  using the database sequence "APTranNo", for Void checks it is a duplicate of the related APTran.APTranNo, else it is set to zero.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Invoice Number that is being paid or adjusted. This is blank in the case of paying a non-payables expense. Otherwise it DOES have to be valid in the APInvHed file.  """  
      self.Posted:bool = obj["Posted"]
      """  An internal flag which indicates if this check has been Posted.  If "NO" then it is considered as still being in the data entry mode. In which case it is still accessible by the check entry programs.  It is set to "Yes" by the group posting process. This is only applicable for TranType = "Pay".  """  
      self.TranAmt:int = obj["TranAmt"]
      """  Transaction Amount. Represents the amount to be applied against the related invoice balance. In the case of payments, this amount excludes any discount, considered as gross payment. TranAmt with a positive sign REDUCES payables while negative INCREASES payables. Example, check detail payments of expenses are positive, unless they are referencing a debit memo. The logic used is that these records are subtracted from the invoice balance.  The adjustment entry program flips the signs of these fields between the user interface and the database. That is to say, the user enters a positive to increase the related invoice or debit memo or a credit to decrease but it is flip when going to/from the database.  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """  Transaction Amount in the vendor's currency. Represents the amount to be applied against the related invoice balance. In the case of payments, this amount excludes any discount, considered as gross payment. TranAmt with a positive sign REDUCES payables while negative INCREASES payables. Example, check detail payments of expenses are positive, unless they are referencing a debit memo. The logic used is that these records are subtracted from the invoice balance.  The adjustment entry program flips the signs of these fields between the user interface and the database. That is to say, the user enters a positive to increase the related invoice or debit memo or a credit to decrease but it is flip when going to/from the database.  """  
      self.DiscAmt:int = obj["DiscAmt"]
      """  Prompt Payment discount. Only applicable if related to a valid APInvHed record. In which case it can be defaulted. This would carry a positive sign except in the case of void checks.  """  
      self.DocDiscAmt:int = obj["DocDiscAmt"]
      """  Prompt Payment discount in Vendors currency. Only applicable if related to a valid APInvHed record. In which case it can be defaulted. This would carry a positive sign except in the case of void checks.  """  
      self.Description:str = obj["Description"]
      """  In the case of payment details this description is printed on the check stub. If referencing a invoice the APInvHed.Description is used as a default.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID of the BankAcct master that this check was drawn  against. This field is updated during the check printing process for system printed checks or entered by the user for manually printed checks. It must be entered and valid for manual checks. It is invalid if not found or BankAcct.Active = No.  """  
      self.CheckNum:int = obj["CheckNum"]
      """  Check number of the related CheckHed.  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction Date. This may be the CheckDate, Void date, or adjustment date. Check dates are duplicated from the CheckHed.CheckDate during the Check printing process. Void date is entered by the user and the void check program duplicates it into each APTran record it generates for the check. Adjustment dates are directly entered by the user.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """   Fiscal Year that transaction will be posted to. For check payments this is duplicated from CheckHed.FiscalYear during check posting.
Void Check entry and adjustment entry assigns the proper fiscal year to each record on the TranDate  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  G\L fiscal period that this transaction is posted to. Updated by the check printing process for system printed checks or by the user for manually printed checks.  If entered must be valid in the Fiscal master.  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Indicates if this transaction has been posted to the General Ledger.  This is set during the G/L transfer process.  """  
      self.Voided:bool = obj["Voided"]
      """   An internal flag indicating if this is a Void payment transaction.
This is set by the A/P void check program. Void payments are duplicates of their original APTran payment record with the exception of having the signs on TranAmt and DiscAmt fields flipped.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  UserID that created this APTran record.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Vendor number. The foreign key that relates the record to the Vendor master record. For TranType = "Pay" it is set equal to CheckHed.VendorNum. For TranType = "Adj" it is captured from the Vendor.VendorNum field.  """  
      self.Comment:str = obj["Comment"]
      """  Allows user to enter comments about the transaction. This is only applicable with TranType = "Adj".  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Region for this payment.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Sales Tax Amount.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Tax Amount in the vendors currency.  """  
      self.RefType:str = obj["RefType"]
      """  Link to the related GLRefTyp.RefType.  """  
      self.RefCode:str = obj["RefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.RefCodeDesc:str = obj["RefCodeDesc"]
      """  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  """  
      self.RoundDiff:int = obj["RoundDiff"]
      """  Rounding difference arises when invoice in one currency are settled in another currency  """  
      self.Rpt1DiscAmt:int = obj["Rpt1DiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DiscAmt:int = obj["Rpt2DiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DiscAmt:int = obj["Rpt3DiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Reporting currency value of this field  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """   Fiscal Year Suffix that transaction will be posted to. For check payments this is duplicated from CheckHed.FiscalYearSuffix during check posting.
Void Check entry and adjustment entry assigns the proper fiscal year suffix to each record on the TranDate  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  """  
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
      self.SelfAssessAmt:int = obj["SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.DocSelfAssessAmt:int = obj["DocSelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt1SelfAssessAmt:int = obj["Rpt1SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt2SelfAssessAmt:int = obj["Rpt2SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt3SelfAssessAmt:int = obj["Rpt3SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.RedStorno:bool = obj["RedStorno"]
      """  Red Storno Flag  """  
      self.PrePayment:bool = obj["PrePayment"]
      """  Indicates that this is prepayment.  """  
      self.ContractRef:str = obj["ContractRef"]
      """  Free form Reference (e.g. Contract Number or other reference specified by user) In case Ref PO is specified, default reference is 'PO: 99999', but can be changed by user.  """  
      self.ContractRefDate:str = obj["ContractRefDate"]
      """  Reference Date (e.g. Contract Date, PO Date or other related date) In case Ref PO is specified, default is PO date, and but be changed by user.  """  
      self.RefPONum:int = obj["RefPONum"]
      """  Reference Purchase Order Number for Prepayments.  """  
      self.TaxReceiptDate:str = obj["TaxReceiptDate"]
      """  Tax Receipt Date (Thailand Localization)  """  
      self.TaxReceiptNo:str = obj["TaxReceiptNo"]
      """  Tax Receipt Number (Thailand Localization)  """  
      self.WHTCertificateDate:str = obj["WHTCertificateDate"]
      """  Withholding Tax Certificate Date (Thailand Localization)  """  
      self.WHTCertificateNo:str = obj["WHTCertificateNo"]
      """  Withholding Tax Certificate Number (Thailand Localization)  """  
      self.PCashDeskID:str = obj["PCashDeskID"]
      """  Unique identifier of Petty Cash Desk  """  
      self.GainLossType:str = obj["GainLossType"]
      """  "R" for realized or "U" for unrealized Gain/Loss  """  
      self.PCashRefNum:int = obj["PCashRefNum"]
      """  Reference Number, unique identifier of Petty Cash Document  """  
      self.ReverseGL:bool = obj["ReverseGL"]
      """  Indicates if it's a reversing Gain/Loss adjustment  """  
      self.RevalueDate:str = obj["RevalueDate"]
      """  Revaluation date that generated the gain/loss record  """  
      self.RevalueBal:int = obj["RevalueBal"]
      """  Invoice Balance at the time of revaluation  """  
      self.DocRevalueBal:int = obj["DocRevalueBal"]
      """  Document currency Invoice Balance at the time of revaluation  """  
      self.Rpt1RevalueBal:int = obj["Rpt1RevalueBal"]
      """  Reporting currency Invoice Balance at the time of revaluation  """  
      self.Rpt2RevalueBal:int = obj["Rpt2RevalueBal"]
      """  Reporting currency Invoice Balance at the time of revaluation  """  
      self.Rpt3RevalueBal:int = obj["Rpt3RevalueBal"]
      """  Reporting currency Invoice Balance at the time of revaluation  """  
      self.BankID:str = obj["BankID"]
      """  Unique ID of the vendor's bank.  """  
      self.BankPaidAmt:int = obj["BankPaidAmt"]
      """  Amount Bank Paid  """  
      self.DocBankPaidAmt:int = obj["DocBankPaidAmt"]
      """  Amount Bank Paid  """  
      self.Rpt1BankPaidAmt:int = obj["Rpt1BankPaidAmt"]
      """  Amount Bank Paid  """  
      self.Rpt2BankPaidAmt:int = obj["Rpt2BankPaidAmt"]
      """  Amount Bank Paid  """  
      self.Rpt3BankPaidAmt:int = obj["Rpt3BankPaidAmt"]
      """  Amount Bank Paid  """  
      self.AdjLegalNumber:str = obj["AdjLegalNumber"]
      """  Legal Number for the adjustment.  """  
      self.AdjTranDocTypeID:str = obj["AdjTranDocTypeID"]
      """  Transaction Document Type for the adjustment.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Indicates the transaction document type for the record. A document type links a system transaction to a unique legal number.  """  
      self.MainSite:bool = obj["MainSite"]
      """  Main Site  """  
      self.SiteCode:str = obj["SiteCode"]
      """  Site Code  """  
      self.BranchID:str = obj["BranchID"]
      """  Branch ID  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice Date  """  
      self.Remarks:str = obj["Remarks"]
      """  Remarks  """  
      self.AssetTypeCode:str = obj["AssetTypeCode"]
      """  Asset Type Code  """  
      self.Cash:bool = obj["Cash"]
      """  Cash  """  
      self.CreditCard:bool = obj["CreditCard"]
      """  Credit Card  """  
      self.Normal:bool = obj["Normal"]
      """  Normal  """  
      self.CardID:str = obj["CardID"]
      """  Card ID  """  
      self.CardHolderTaxID:str = obj["CardHolderTaxID"]
      """  Card Holder Tax ID  """  
      self.CardMemberName:str = obj["CardMemberName"]
      """  Card Member Name  """  
      self.Excluded:bool = obj["Excluded"]
      """  Excluded  """  
      self.Deferred:bool = obj["Deferred"]
      """  Deferred  """  
      self.NonDeductAmt:int = obj["NonDeductAmt"]
      """  Non Deductable Amount  """  
      self.NonDeductDocAmt:int = obj["NonDeductDocAmt"]
      """  Non Deductable Doc Amount  """  
      self.NonDeductRpt1Amt:int = obj["NonDeductRpt1Amt"]
      """  Non Deductable Rpt1 Amount  """  
      self.NonDeductRpt2Amt:int = obj["NonDeductRpt2Amt"]
      """  Non Deductable Rpt2 Amount  """  
      self.NonDeductRpt3Amt:int = obj["NonDeductRpt3Amt"]
      """  Non Deductable Rpt3 Amount  """  
      self.PaymentNumber:str = obj["PaymentNumber"]
      """  PaymentNumber  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.UrgentPayment:bool = obj["UrgentPayment"]
      """  UrgentPayment  """  
      self.InvoiceRef:str = obj["InvoiceRef"]
      """  InvoiceRef  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Rate Group Code for transactions of type ADJ  """  
      self.CNCFICode:str = obj["CNCFICode"]
      """  CNCFICode  """  
      self.Gen1099Date:str = obj["Gen1099Date"]
      """  Generation 1099 Date  """  
      self.NOTranReason:str = obj["NOTranReason"]
      """  NOTranReason  """  
      self.PEIsDetractionPayment:bool = obj["PEIsDetractionPayment"]
      """  PEIsDetractionPayment  """  
      self.Code1099ID:str = obj["Code1099ID"]
      """  Code1099ID  """  
      self.FormTypeID:str = obj["FormTypeID"]
      """  FormTypeID  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.DocWhManAddAmt:int = obj["DocWhManAddAmt"]
      """  DocWhManAddAmt  """  
      self.WhManAddAmt:int = obj["WhManAddAmt"]
      """  WhManAddAmt  """  
      self.Rpt1WhManAddAmt:int = obj["Rpt1WhManAddAmt"]
      """  Rpt1WhManAddAmt  """  
      self.Rpt2WhManAddAmt:int = obj["Rpt2WhManAddAmt"]
      """  Rpt2WhManAddAmt  """  
      self.Rpt3WhManAddAmt:int = obj["Rpt3WhManAddAmt"]
      """  Rpt3WhManAddAmt  """  
      self.BaseAdjustAmt:int = obj["BaseAdjustAmt"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for BASE  """  
      self.BaseCurrSymbolCurrDesc:str = obj["BaseCurrSymbolCurrDesc"]
      self.BaseCurrSymbolCurrName:str = obj["BaseCurrSymbolCurrName"]
      self.BaseCurrSymbolCurrSymbol:str = obj["BaseCurrSymbolCurrSymbol"]
      self.BaseCurrSymbolDocumentDesc:str = obj["BaseCurrSymbolDocumentDesc"]
      self.BaseSelfAssessedTax:int = obj["BaseSelfAssessedTax"]
      self.ChangeExchangeRateResponse:str = obj["ChangeExchangeRateResponse"]
      """  Yes and No considered valid response.  All other values including blank treated as question was not posed to the user.  """  
      self.CNCFICodeDescription:str = obj["CNCFICodeDescription"]
      self.CopyRate:bool = obj["CopyRate"]
      """  If Copy Rate is true then original AP Invoice exchange rates are used when Adjustmet is applied and no currency gain/loss are calculated  """  
      self.CorrectionInv:bool = obj["CorrectionInv"]
      """  The flag to indicate if this payment line is realted to Correction invoice with negative amount  """  
      self.CPayLinked:bool = obj["CPayLinked"]
      """  Indicates if the related invoice is linked to a Central Payment invoice  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencyGainLoss:int = obj["CurrencyGainLoss"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      """  Currency.CurrSymbol from APInvHed  """  
      self.CurrSymbolCurrDesc:str = obj["CurrSymbolCurrDesc"]
      self.CurrSymbolCurrName:str = obj["CurrSymbolCurrName"]
      self.CurrSymbolCurrSymbol:str = obj["CurrSymbolCurrSymbol"]
      self.CurrSymbolDocumentDesc:str = obj["CurrSymbolDocumentDesc"]
      self.DebitMemo:bool = obj["DebitMemo"]
      self.DisableFieldsForPCashDoc:bool = obj["DisableFieldsForPCashDoc"]
      self.DiscountAvailable:bool = obj["DiscountAvailable"]
      self.DiscountDate:str = obj["DiscountDate"]
      self.DispGLAcct:str = obj["DispGLAcct"]
      """  The display gl account.  """  
      self.DispTranAmt:int = obj["DispTranAmt"]
      self.DocBaseSelfAssessedTax:int = obj["DocBaseSelfAssessedTax"]
      self.DocDispTranAmt:int = obj["DocDispTranAmt"]
      self.DocExpenseAmount:int = obj["DocExpenseAmount"]
      self.DocGainLossAmt:int = obj["DocGainLossAmt"]
      self.DocInvoiceAmt:int = obj["DocInvoiceAmt"]
      self.DocInvoiceBal:int = obj["DocInvoiceBal"]
      self.DocNetAmount:int = obj["DocNetAmount"]
      self.DocNewBalance:int = obj["DocNewBalance"]
      self.DocSelfAssessedTax:int = obj["DocSelfAssessedTax"]
      self.DocUnPostedBal:int = obj["DocUnPostedBal"]
      self.DocWithHoldTax:int = obj["DocWithHoldTax"]
      self.DsblCopyRate:bool = obj["DsblCopyRate"]
      """  If this flag is true then Copy Rate checkbox is Read Only  """  
      self.DueDate:str = obj["DueDate"]
      self.ExchangeRate:int = obj["ExchangeRate"]
      self.ExpenseAmount:int = obj["ExpenseAmount"]
      self.FullyPaid:bool = obj["FullyPaid"]
      """  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency.  """  
      self.GainLossAmt:int = obj["GainLossAmt"]
      self.GlbCompany:str = obj["GlbCompany"]
      """  This is the source Company of the Central Payment linked invoice  """  
      self.GroupID:str = obj["GroupID"]
      self.InitUrgentPayment:bool = obj["InitUrgentPayment"]
      """  CSF Switzerland - Initial value for Urgent Invoice Payment flag.  """  
      self.InvExchangeRate:int = obj["InvExchangeRate"]
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      self.InvoiceBal:int = obj["InvoiceBal"]
      self.isDiscountforDebitM:bool = obj["isDiscountforDebitM"]
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.LegalNumStyle:str = obj["LegalNumStyle"]
      """  Indicates if the legal number is manually generated or system generated  """  
      self.LockRate:bool = obj["LockRate"]
      self.MiscPayment:bool = obj["MiscPayment"]
      self.NetAmount:int = obj["NetAmount"]
      self.NewBalance:int = obj["NewBalance"]
      self.PaymentDesc:str = obj["PaymentDesc"]
      """  This field equals "Invoice" for Invoice payment, and "Misc" for Miscelleneous payment. This field  is used as label in tree.  """  
      self.PostErrMess:str = obj["PostErrMess"]
      """  Posting Error Message  """  
      self.PostToGL:bool = obj["PostToGL"]
      """  Indicates if posting GL transactions.  """  
      self.Print1099:bool = obj["Print1099"]
      """  Print 1099  """  
      self.RateGroupDescription:str = obj["RateGroupDescription"]
      self.RefCodeEnabled:bool = obj["RefCodeEnabled"]
      self.RefCodeList:str = obj["RefCodeList"]
      """  Delimited list of possible Ref codes.  """  
      self.RefCodeStatus:str = obj["RefCodeStatus"]
      """  Indicates if Reference Code is (M)andatory, (O)ptional, (E)xcluded or Blank.  Enable Reference Code if "M" or "O".  """  
      self.Rpt1DispTranAmt:int = obj["Rpt1DispTranAmt"]
      self.Rpt1GainLossAmt:int = obj["Rpt1GainLossAmt"]
      self.Rpt1InvoiceAmt:int = obj["Rpt1InvoiceAmt"]
      self.Rpt1InvoiceBal:int = obj["Rpt1InvoiceBal"]
      """  Invoice balance before adjustment in Rpt1 currency  """  
      self.Rpt1NewBalance:int = obj["Rpt1NewBalance"]
      self.Rpt2DispTranAmt:int = obj["Rpt2DispTranAmt"]
      self.Rpt2GainLossAmt:int = obj["Rpt2GainLossAmt"]
      self.Rpt2InvoiceAmt:int = obj["Rpt2InvoiceAmt"]
      self.Rpt2InvoiceBal:int = obj["Rpt2InvoiceBal"]
      """  Invoice balance before adjustment in Rpt2 currency  """  
      self.Rpt2NewBalance:int = obj["Rpt2NewBalance"]
      self.Rpt3DispTranAmt:int = obj["Rpt3DispTranAmt"]
      self.Rpt3GainLossAmt:int = obj["Rpt3GainLossAmt"]
      self.Rpt3InvoiceAmt:int = obj["Rpt3InvoiceAmt"]
      self.Rpt3InvoiceBal:int = obj["Rpt3InvoiceBal"]
      """  Report balance before adjustment in rpt3 currency  """  
      self.Rpt3NewBalance:int = obj["Rpt3NewBalance"]
      self.SelfAssessedTax:int = obj["SelfAssessedTax"]
      self.TaxableTransaction:bool = obj["TaxableTransaction"]
      """  Indicates if tax records are created and posted for AP Invoice adjustment  """  
      self.TaxLinesExist:bool = obj["TaxLinesExist"]
      self.TermsCode:str = obj["TermsCode"]
      self.TermsCodeDescription:str = obj["TermsCodeDescription"]
      self.UnPostedBal:int = obj["UnPostedBal"]
      """  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  """  
      self.WithHoldTax:int = obj["WithHoldTax"]
      self.XRateLabel:str = obj["XRateLabel"]
      self.AmtToAP:int = obj["AmtToAP"]
      self.ApplyDate:str = obj["ApplyDate"]
      self.InvoiceLegalNumber:str = obj["InvoiceLegalNumber"]
      self.PLInvoiceReference:str = obj["PLInvoiceReference"]
      self.isPrecalcTax:bool = obj["isPrecalcTax"]
      """  The internal flag to indicate if Tax Liability assigned to the invoice being paid has Witholding taxes with Payment timing (WH taxes will be precalculated)  """  
      self.PrepayApld:bool = obj["PrepayApld"]
      """  The flag to indicate if the invoice being paid (applied)in Payment Entry/Invoice Payment is AP Invoice created for Misc. Payment / Prepayment by the system.  """  
      self.ManualTaxAdj:bool = obj["ManualTaxAdj"]
      """  The flag related to Misc. payment to indicate if Tax records created per Tax Liability assigned to Misc. payment are adjusted,  deleted,  or any tax records were added by the user  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      self.Code1099Description:str = obj["Code1099Description"]
      self.FormTypeDescription:str = obj["FormTypeDescription"]
      self.InvoiceNumDescription:str = obj["InvoiceNumDescription"]
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APTranTGLCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "PORel" control this field would contain the related PO Number.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.   For example: For a "PORel" control this field would contain the related PO Line Number.
The usage of this field is dependent on the type of record.  """  
      self.Key3:str = obj["Key3"]
      """  3rd component of the foreign key to the related master record.  For example: For a "PORel" control this field would contain the related PO Release Number.  The usage of this field is dependent record type.  """  
      self.Key4:str = obj["Key4"]
      """   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key5:str = obj["Key5"]
      """   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key6:str = obj["Key6"]
      """   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.TGLCTranNum:int = obj["TGLCTranNum"]
      """  Internal identifier used to keep records unique for the related record.  The system generates this number by finding the last TranGLC record for the RelatedToFile-Key1-Key2 etc. and adding 1 to it.  """  
      self.GLAcctContext:str = obj["GLAcctContext"]
      """  String identifier of the account context.  """  
      self.BookID:str = obj["BookID"]
      """  Reference to an accounting book.  If not blank must be a valid entry in the GLBook table.  """  
      self.COACode:str = obj["COACode"]
      """  The chart of account code used by the book.  Will contain the Master COA when BookID is blank.  Reference only.  Used for integrity checking when updating/deleting a GL account.  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Full account containing the non-dynamic segment values up to 200 characters.  Unique identifier for the GL Account.  """  
      self.UserCanModify:bool = obj["UserCanModify"]
      """  Indicates if the user can update or delete this record.  """  
      self.SegValue1:str = obj["SegValue1"]
      """  Segement Value 1 of the account for this context.  """  
      self.SegValue2:str = obj["SegValue2"]
      """  Segement Value 2 of the account for this context.  """  
      self.SegValue3:str = obj["SegValue3"]
      """  Segement Value 3 of the account for this context.  """  
      self.SegValue4:str = obj["SegValue4"]
      """  Segement Value 4 of the account for this context.  """  
      self.SegValue5:str = obj["SegValue5"]
      """  Segement Value 5 of the account for this context.  """  
      self.SegValue6:str = obj["SegValue6"]
      """  Segement Value 6 of the account for this context.  """  
      self.SegValue7:str = obj["SegValue7"]
      """  Segement Value 7 of the account for this context.  """  
      self.SegValue8:str = obj["SegValue8"]
      """  Segement Value 8 of the account for this context.  """  
      self.SegValue9:str = obj["SegValue9"]
      """  Segement Value 9 of the account for this context.  """  
      self.SegValue10:str = obj["SegValue10"]
      """  Segement Value 10 of the account for this context.  """  
      self.SegValue11:str = obj["SegValue11"]
      """  Segement Value 11 of the account for this context.  """  
      self.SegValue12:str = obj["SegValue12"]
      """  Segement Value 12 of the account for this context.  """  
      self.SegValue13:str = obj["SegValue13"]
      """  Segement Value 13 of the account for this context.  """  
      self.SegValue14:str = obj["SegValue14"]
      """  Segement Value 14 of the account for this context.  """  
      self.SegValue15:str = obj["SegValue15"]
      """  Segement Value 15 of the account for this context.  """  
      self.SegValue16:str = obj["SegValue16"]
      """  Segement Value 16 of the account for this context.  """  
      self.SegValue17:str = obj["SegValue17"]
      """  Segement Value 17 of the account for this context.  """  
      self.SegValue18:str = obj["SegValue18"]
      """  Segement Value 18 of the account for this context.  """  
      self.SegValue19:str = obj["SegValue19"]
      """  Segement Value 19 of the account for this context.  """  
      self.SegValue20:str = obj["SegValue20"]
      """  Segement Value 20 of the account for this context.  """  
      self.SysGLControlType:str = obj["SysGLControlType"]
      """  Unique Identifier of the system GL Control Type.  """  
      self.SysGLControlCode:str = obj["SysGLControlCode"]
      """  System generated GL Control Identifier.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.IsExternalCompany:bool = obj["IsExternalCompany"]
      """  Flag to indicate the account in this record is for an external company.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal year of the related GLJrnDtl.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  JournalCode of the related GLJrnDtl.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  Journal number of the related GLJrnDtl.  """  
      self.JournalLine:int = obj["JournalLine"]
      """  JournalLine of the related GLJrnDtl.  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction date of the transaction.  This is used in order to display the transactions in date order.  """  
      self.TranSource:str = obj["TranSource"]
      """   An internal code to identify the table of  the source transaction.
P = PartTran
L = LaborDtl
I = InvcHead
Note: The system does not combine TranSource when creating GLJrnDtl. That is, a specific GLJrnDtl record can only be related to one source.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  LaborHedSeq of the related LaborDtl.  Pertains only to source from LaborDtl (TranSource = "L")  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  LaborDtlSeq of the related LaborDtl. Pertains only to source from LaborDtl (TranSource = "L")  """  
      self.SysDate:str = obj["SysDate"]
      """  System date of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.SysTime:int = obj["SysTime"]
      """  System time of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.TranNum:int = obj["TranNum"]
      """  TranNum of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.ARInvoiceNum:int = obj["ARInvoiceNum"]
      """  InvoiceNum of the related InvcHead record.  Pertains only to source from PartTran (TranSource = "I")  """  
      self.TransAmt:int = obj["TransAmt"]
      """  Transaction amount that this transaction posted to the related GlJrnDtl.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Invoice Line Number associated with this GL Journal  """  
      self.SeqNum:int = obj["SeqNum"]
      """  The sequence number associated with this GL journal  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  Vendor's invoice number.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Date record was created  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.CreditAmount:int = obj["CreditAmount"]
      """  Credit Amount.  """  
      self.DebitAmount:int = obj["DebitAmount"]
      """  Debit Amount.  """  
      self.BookCreditAmount:int = obj["BookCreditAmount"]
      """  BookCreditAmount  """  
      self.BookDebitAmount:int = obj["BookDebitAmount"]
      """  Book Debit Amount  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the document currency.  """  
      self.RecordType:str = obj["RecordType"]
      """   Indicates if this record contains account data only or reference data such as journal number, amounts, etc.  Valid  values are:
A - account data only
R - reference data  """  
      self.CorrAccUID:int = obj["CorrAccUID"]
      """  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  """  
      self.ABTUID:str = obj["ABTUID"]
      """  this field equals ABTUID which was created during posting  """  
      self.RuleUID:int = obj["RuleUID"]
      """  Technical identifier.  """  
      self.Statistical:int = obj["Statistical"]
      """   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  """  
      self.StatUOMCode:str = obj["StatUOMCode"]
      """  Statistical UOM code.  """  
      self.DebitStatAmt:int = obj["DebitStatAmt"]
      """  This field shows Debit statistical amount.  """  
      self.CreditStatAmt:int = obj["CreditStatAmt"]
      """  This field shows Credit statistical amount.  """  
      self.IsModifiedByUser:bool = obj["IsModifiedByUser"]
      """  IsModifiedByUser  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MovementNum:int = obj["MovementNum"]
      """  MovementNum  """  
      self.MovementType:str = obj["MovementType"]
      """  MovementType  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.GroupID:str = obj["GroupID"]
      """  GroupID of APTran  """  
      self.HeadNum:int = obj["HeadNum"]
      """  HeadNum of APTran  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  InvoiceNum of APTran  """  
      self.Voided:bool = obj["Voided"]
      """  Voided of APTran  """  
      self.APTranNo:int = obj["APTranNo"]
      """  APTranNo of APTran  """  
      self.BitFlag:int = obj["BitFlag"]
      self.COADescription:str = obj["COADescription"]
      self.GLAccountAccountDesc:str = obj["GLAccountAccountDesc"]
      self.GLAccountGLAcctDisp:str = obj["GLAccountGLAcctDisp"]
      self.GLAccountGLShortAcct:str = obj["GLAccountGLShortAcct"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LegalNumberID:str = obj["LegalNumberID"]
      self.TransYear:int = obj["TransYear"]
      self.TransYearSuffix:str = obj["TransYearSuffix"]
      self.DspTransYear:str = obj["DspTransYear"]
      self.ShowDspTransYear:bool = obj["ShowDspTransYear"]
      """  Indicates if DspTransYear should be displayed when prompting for a manual number.  """  
      self.Prefix:str = obj["Prefix"]
      self.PrefixList:str = obj["PrefixList"]
      """  The list of prefixes that can be selected by the user for manual numbers.  """  
      self.NumberSuffix:str = obj["NumberSuffix"]
      """  The suffix portion of the legal number.  """  
      self.EnablePrefix:bool = obj["EnablePrefix"]
      """  Indicates if the prefix can be entered by the user.  """  
      self.EnableSuffix:bool = obj["EnableSuffix"]
      """  Indicates if the suffix (number) can be entered by the user.  """  
      self.NumberOption:str = obj["NumberOption"]
      self.DocumentDate:str = obj["DocumentDate"]
      self.GenerationType:str = obj["GenerationType"]
      self.Description:str = obj["Description"]
      self.TransPeriod:int = obj["TransPeriod"]
      self.PeriodPrefix:str = obj["PeriodPrefix"]
      """  Prefix for the period  """  
      self.ShowTransPeriod:bool = obj["ShowTransPeriod"]
      self.LegalNumber:str = obj["LegalNumber"]
      """  Used when the full legal number is entered  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      self.TranDocTypeID2:str = obj["TranDocTypeID2"]
      self.GenerationOption:str = obj["GenerationOption"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangeAdjAmount_input:
   """ Required : 
   ipTranAmtType
   ProposedTranAmt
   ipRateGroupCode
   ds
   """  
   def __init__(self, obj):
      self.ipTranAmtType:str = obj["ipTranAmtType"]
      """  Indicate which of the transaction amount is changed.
            Valid values are: 'B' for Base Tran Amount and 'D' for Doc Tran Amount  """  
      self.ProposedTranAmt:int = obj["ProposedTranAmt"]
      """  The proposed Display Transaction Amount  """  
      self.ipRateGroupCode:str = obj["ipRateGroupCode"]
      """  rate group code for adjustment  """  
      self.ds:list[Erp_Tablesets_APAdjustmentTableset] = obj["ds"]
      pass

class ChangeAdjAmount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APAdjustmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeCopyRate_input:
   """ Required : 
   proposedCopyRate
   ds
   """  
   def __init__(self, obj):
      self.proposedCopyRate:bool = obj["proposedCopyRate"]
      """  The proposed flag to copy or not to copy the exchange rates of the invoice  """  
      self.ds:list[Erp_Tablesets_APAdjustmentTableset] = obj["ds"]
      pass

class ChangeCopyRate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APAdjustmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeGLAcctDisp_input:
   """ Required : 
   ipCompany
   ipCOACode
   ipGLAccount
   ipSegValues
   """  
   def __init__(self, obj):
      self.ipCompany:str = obj["ipCompany"]
      """  TranGLC Company for G/L Account  """  
      self.ipCOACode:str = obj["ipCOACode"]
      """  TranGLC COA Code for G/L Account  """  
      self.ipGLAccount:str = obj["ipGLAccount"]
      """  TranGLC G/L Account  """  
      self.ipSegValues:str = obj["ipSegValues"]
      """  TranGLC Segment valuse for G/L Account  """  
      pass

class ChangeGLAcctDisp_output:
   def __init__(self, obj):
      pass

class ChangeRateGroup_input:
   """ Required : 
   ipRateGroupCode
   ds
   """  
   def __init__(self, obj):
      self.ipRateGroupCode:str = obj["ipRateGroupCode"]
      self.ds:list[Erp_Tablesets_APAdjustmentTableset] = obj["ds"]
      pass

class ChangeRateGroup_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APAdjustmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeTranDate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APAdjustmentTableset] = obj["ds"]
      pass

class ChangeTranDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APAdjustmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckGLInterface_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      self.opPostToGL:bool = obj["opPostToGL"]
      pass

      """  output parameters  """  

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

class Erp_Tablesets_APAdjustmentTableset:
   def __init__(self, obj):
      self.APInvHedAdj:list[Erp_Tablesets_APInvHedAdjRow] = obj["APInvHedAdj"]
      self.APTran:list[Erp_Tablesets_APTranRow] = obj["APTran"]
      self.APTranTGLC:list[Erp_Tablesets_APTranTGLCRow] = obj["APTranTGLC"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_APInvHedAdjListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenPayable:bool = obj["OpenPayable"]
      """  Indicates if this is an "open" Payable.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead it is assigned from the Vendor.VendorNum using VendorID to find the Vendor record.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Vendor's invoice number.  """  
      self.DebitMemo:bool = obj["DebitMemo"]
      """   Indicates the type of document. Yes = Debit Memo,  No= Invoice. This value can't be changed after the record has been created.
Debit memos affect the way detail quantities and amounts are stored in the database. They will always be stored with a negative sign, but are entered as a positive.
The system uses this field to test for Debit Memos,  indicated by "DM" following the invoice number.  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice date.  """  
      self.DueDate:str = obj["DueDate"]
      """  The due date of the earliest unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates if this invoice has been Posted to the open payables file.    Only invoices that have been Posted (true) will be included as part of the open payables, that is they will not appear on reports or inquiries other than those used within invoice entry. Otherwise they are considered as still being in data entry. This field is always "no" when the invoice is created. It is set to "yes"  by the  "Post function". Once an invoice is posted it can't be maintained via data entry.  """  
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      """  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (APInvDtl) and of the miscellaneous charges/credits (APInvMsc) records.  This field has a true sign. (debit memos are negative).  """  
      self.DocInvoiceAmt:int = obj["DocInvoiceAmt"]
      """  Total invoice Amount.(Vendors Currency) This field is an accumulation of the extended net amounts of the detail line items (APInvDtl) and of the miscellaneous charges/credits (APInvMsc) records.  This field has a true sign. (debit memos are negative).  """  
      self.InvoiceBal:int = obj["InvoiceBal"]
      """  Current outstanding balance. Carries a true sign. (Credit memos are negative).  """  
      self.DocInvoiceBal:int = obj["DocInvoiceBal"]
      """  Current outstanding balance.(Vendors currency)  Carries a true sign. (Credit memos are negative).  """  
      self.UnpostedBal:int = obj["UnpostedBal"]
      """  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  """  
      self.DocUnpostedBal:int = obj["DocUnpostedBal"]
      """  Current outstanding balance which includes the unposted cash receipt amounts(Vendors currency). This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  """  
      self.InvoiceHeld:bool = obj["InvoiceHeld"]
      """  Invoices that are within a data entry group can be put on "Hold". They will not be posted until InvoiceHeld=No. This flag can be used for whatever the reason the user may wish to keep an invoice in a data entry group from being posted.  This is NOT the same thing as putting an invoice on PaymentHold.  """  
      self.Description:str = obj["Description"]
      """  A short description that can be used to explain what this invoice is for. Ex: Rent, Auto Lease Payment.  This description is defaulted into the APTran.Description field when payments are made against the invoice.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.Rpt1InvoiceAmt:int = obj["Rpt1InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2InvoiceAmt:int = obj["Rpt2InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3InvoiceAmt:int = obj["Rpt3InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1InvoiceBal:int = obj["Rpt1InvoiceBal"]
      """  Reporting currency value of this field  """  
      self.Rpt2InvoiceBal:int = obj["Rpt2InvoiceBal"]
      """  Reporting currency value of this field  """  
      self.Rpt3InvoiceBal:int = obj["Rpt3InvoiceBal"]
      """  Reporting currency value of this field  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  The date this invoice will get applied to the books when it is posted.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      """  Currency Switch  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for BASE  """  
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
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
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APInvHedAdjListTableset:
   def __init__(self, obj):
      self.APInvHedAdjList:list[Erp_Tablesets_APInvHedAdjListRow] = obj["APInvHedAdjList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_APInvHedAdjRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenPayable:bool = obj["OpenPayable"]
      """  Indicates if this is an "open" Payable.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead it is assigned from the Vendor.VendorNum using VendorID to find the Vendor record.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Vendor's invoice number.  """  
      self.DebitMemo:bool = obj["DebitMemo"]
      """   Indicates the type of document. Yes = Debit Memo,  No= Invoice. This value can't be changed after the record has been created.
Debit memos affect the way detail quantities and amounts are stored in the database. They will always be stored with a negative sign, but are entered as a positive.
The system uses this field to test for Debit Memos,  indicated by "DM" following the invoice number.  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice date.  """  
      self.DueDate:str = obj["DueDate"]
      """  The due date of the earliest unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates if this invoice has been Posted to the open payables file.    Only invoices that have been Posted (true) will be included as part of the open payables, that is they will not appear on reports or inquiries other than those used within invoice entry. Otherwise they are considered as still being in data entry. This field is always "no" when the invoice is created. It is set to "yes"  by the  "Post function". Once an invoice is posted it can't be maintained via data entry.  """  
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      """  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (APInvDtl) and of the miscellaneous charges/credits (APInvMsc) records.  This field has a true sign. (debit memos are negative).  """  
      self.DocInvoiceAmt:int = obj["DocInvoiceAmt"]
      """  Total invoice Amount.(Vendors Currency) This field is an accumulation of the extended net amounts of the detail line items (APInvDtl) and of the miscellaneous charges/credits (APInvMsc) records.  This field has a true sign. (debit memos are negative).  """  
      self.InvoiceBal:int = obj["InvoiceBal"]
      """  Current outstanding balance. Carries a true sign. (Credit memos are negative).  """  
      self.DocInvoiceBal:int = obj["DocInvoiceBal"]
      """  Current outstanding balance.(Vendors currency)  Carries a true sign. (Credit memos are negative).  """  
      self.UnpostedBal:int = obj["UnpostedBal"]
      """  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  """  
      self.DocUnpostedBal:int = obj["DocUnpostedBal"]
      """  Current outstanding balance which includes the unposted cash receipt amounts(Vendors currency). This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  """  
      self.InvoiceHeld:bool = obj["InvoiceHeld"]
      """  Invoices that are within a data entry group can be put on "Hold". They will not be posted until InvoiceHeld=No. This flag can be used for whatever the reason the user may wish to keep an invoice in a data entry group from being posted.  This is NOT the same thing as putting an invoice on PaymentHold.  """  
      self.Description:str = obj["Description"]
      """  A short description that can be used to explain what this invoice is for. Ex: Rent, Auto Lease Payment.  This description is defaulted into the APTran.Description field when payments are made against the invoice.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.Rpt1InvoiceAmt:int = obj["Rpt1InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2InvoiceAmt:int = obj["Rpt2InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3InvoiceAmt:int = obj["Rpt3InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1InvoiceBal:int = obj["Rpt1InvoiceBal"]
      """  Reporting currency value of this field  """  
      self.Rpt2InvoiceBal:int = obj["Rpt2InvoiceBal"]
      """  Reporting currency value of this field  """  
      self.Rpt3InvoiceBal:int = obj["Rpt3InvoiceBal"]
      """  Reporting currency value of this field  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  The date this invoice will get applied to the books when it is posted.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      """  Currency Switch  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for BASE  """  
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.CorrectionInvNeg:bool = obj["CorrectionInvNeg"]
      """  Indictes if the invoice being adjusted  is Correction Invoice with negative amount  """  
      self.CopyRate:bool = obj["CopyRate"]
      """  If Copy Rate is true then original AP Invoice exchange rates are used when Adjustmet is applied and no currency gain/loss are calculated  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APTranRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TranType:str = obj["TranType"]
      """  An internal flag which identifies the type of transaction. Valid types are "Pay" or "Adj".  """  
      self.HeadNum:int = obj["HeadNum"]
      """  If TranType = "Pay" or "ADJ" for a currency gain/loss  then this is a duplicate of the related CheckHed.HeadNum,  otherwise it is set to zero.  """  
      self.APTranNo:int = obj["APTranNo"]
      """  Integer assigned by the system which is used as one of the fields to uniquely identify the APTran record.  If (TranType = "Pay"  and InvoiceNum = "") or (TranType = "Adj") it is assigned a unique #  using the database sequence "APTranNo", for Void checks it is a duplicate of the related APTran.APTranNo, else it is set to zero.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Invoice Number that is being paid or adjusted. This is blank in the case of paying a non-payables expense. Otherwise it DOES have to be valid in the APInvHed file.  """  
      self.Posted:bool = obj["Posted"]
      """  An internal flag which indicates if this check has been Posted.  If "NO" then it is considered as still being in the data entry mode. In which case it is still accessible by the check entry programs.  It is set to "Yes" by the group posting process. This is only applicable for TranType = "Pay".  """  
      self.TranAmt:int = obj["TranAmt"]
      """  Transaction Amount. Represents the amount to be applied against the related invoice balance. In the case of payments, this amount excludes any discount, considered as gross payment. TranAmt with a positive sign REDUCES payables while negative INCREASES payables. Example, check detail payments of expenses are positive, unless they are referencing a debit memo. The logic used is that these records are subtracted from the invoice balance.  The adjustment entry program flips the signs of these fields between the user interface and the database. That is to say, the user enters a positive to increase the related invoice or debit memo or a credit to decrease but it is flip when going to/from the database.  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """  Transaction Amount in the vendor's currency. Represents the amount to be applied against the related invoice balance. In the case of payments, this amount excludes any discount, considered as gross payment. TranAmt with a positive sign REDUCES payables while negative INCREASES payables. Example, check detail payments of expenses are positive, unless they are referencing a debit memo. The logic used is that these records are subtracted from the invoice balance.  The adjustment entry program flips the signs of these fields between the user interface and the database. That is to say, the user enters a positive to increase the related invoice or debit memo or a credit to decrease but it is flip when going to/from the database.  """  
      self.DiscAmt:int = obj["DiscAmt"]
      """  Prompt Payment discount. Only applicable if related to a valid APInvHed record. In which case it can be defaulted. This would carry a positive sign except in the case of void checks.  """  
      self.DocDiscAmt:int = obj["DocDiscAmt"]
      """  Prompt Payment discount in Vendors currency. Only applicable if related to a valid APInvHed record. In which case it can be defaulted. This would carry a positive sign except in the case of void checks.  """  
      self.Description:str = obj["Description"]
      """  In the case of payment details this description is printed on the check stub. If referencing a invoice the APInvHed.Description is used as a default.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID of the BankAcct master that this check was drawn  against. This field is updated during the check printing process for system printed checks or entered by the user for manually printed checks. It must be entered and valid for manual checks. It is invalid if not found or BankAcct.Active = No.  """  
      self.CheckNum:int = obj["CheckNum"]
      """  Check number of the related CheckHed.  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction Date. This may be the CheckDate, Void date, or adjustment date. Check dates are duplicated from the CheckHed.CheckDate during the Check printing process. Void date is entered by the user and the void check program duplicates it into each APTran record it generates for the check. Adjustment dates are directly entered by the user.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """   Fiscal Year that transaction will be posted to. For check payments this is duplicated from CheckHed.FiscalYear during check posting.
Void Check entry and adjustment entry assigns the proper fiscal year to each record on the TranDate  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  G\L fiscal period that this transaction is posted to. Updated by the check printing process for system printed checks or by the user for manually printed checks.  If entered must be valid in the Fiscal master.  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Indicates if this transaction has been posted to the General Ledger.  This is set during the G/L transfer process.  """  
      self.Voided:bool = obj["Voided"]
      """   An internal flag indicating if this is a Void payment transaction.
This is set by the A/P void check program. Void payments are duplicates of their original APTran payment record with the exception of having the signs on TranAmt and DiscAmt fields flipped.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  UserID that created this APTran record.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Vendor number. The foreign key that relates the record to the Vendor master record. For TranType = "Pay" it is set equal to CheckHed.VendorNum. For TranType = "Adj" it is captured from the Vendor.VendorNum field.  """  
      self.Comment:str = obj["Comment"]
      """  Allows user to enter comments about the transaction. This is only applicable with TranType = "Adj".  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Region for this payment.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Sales Tax Amount.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Tax Amount in the vendors currency.  """  
      self.RefType:str = obj["RefType"]
      """  Link to the related GLRefTyp.RefType.  """  
      self.RefCode:str = obj["RefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.RefCodeDesc:str = obj["RefCodeDesc"]
      """  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  """  
      self.RoundDiff:int = obj["RoundDiff"]
      """  Rounding difference arises when invoice in one currency are settled in another currency  """  
      self.Rpt1DiscAmt:int = obj["Rpt1DiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DiscAmt:int = obj["Rpt2DiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DiscAmt:int = obj["Rpt3DiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Reporting currency value of this field  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """   Fiscal Year Suffix that transaction will be posted to. For check payments this is duplicated from CheckHed.FiscalYearSuffix during check posting.
Void Check entry and adjustment entry assigns the proper fiscal year suffix to each record on the TranDate  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  """  
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
      self.SelfAssessAmt:int = obj["SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.DocSelfAssessAmt:int = obj["DocSelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt1SelfAssessAmt:int = obj["Rpt1SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt2SelfAssessAmt:int = obj["Rpt2SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt3SelfAssessAmt:int = obj["Rpt3SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.RedStorno:bool = obj["RedStorno"]
      """  Red Storno Flag  """  
      self.PrePayment:bool = obj["PrePayment"]
      """  Indicates that this is prepayment.  """  
      self.ContractRef:str = obj["ContractRef"]
      """  Free form Reference (e.g. Contract Number or other reference specified by user) In case Ref PO is specified, default reference is 'PO: 99999', but can be changed by user.  """  
      self.ContractRefDate:str = obj["ContractRefDate"]
      """  Reference Date (e.g. Contract Date, PO Date or other related date) In case Ref PO is specified, default is PO date, and but be changed by user.  """  
      self.RefPONum:int = obj["RefPONum"]
      """  Reference Purchase Order Number for Prepayments.  """  
      self.TaxReceiptDate:str = obj["TaxReceiptDate"]
      """  Tax Receipt Date (Thailand Localization)  """  
      self.TaxReceiptNo:str = obj["TaxReceiptNo"]
      """  Tax Receipt Number (Thailand Localization)  """  
      self.WHTCertificateDate:str = obj["WHTCertificateDate"]
      """  Withholding Tax Certificate Date (Thailand Localization)  """  
      self.WHTCertificateNo:str = obj["WHTCertificateNo"]
      """  Withholding Tax Certificate Number (Thailand Localization)  """  
      self.PCashDeskID:str = obj["PCashDeskID"]
      """  Unique identifier of Petty Cash Desk  """  
      self.GainLossType:str = obj["GainLossType"]
      """  "R" for realized or "U" for unrealized Gain/Loss  """  
      self.PCashRefNum:int = obj["PCashRefNum"]
      """  Reference Number, unique identifier of Petty Cash Document  """  
      self.ReverseGL:bool = obj["ReverseGL"]
      """  Indicates if it's a reversing Gain/Loss adjustment  """  
      self.RevalueDate:str = obj["RevalueDate"]
      """  Revaluation date that generated the gain/loss record  """  
      self.RevalueBal:int = obj["RevalueBal"]
      """  Invoice Balance at the time of revaluation  """  
      self.DocRevalueBal:int = obj["DocRevalueBal"]
      """  Document currency Invoice Balance at the time of revaluation  """  
      self.Rpt1RevalueBal:int = obj["Rpt1RevalueBal"]
      """  Reporting currency Invoice Balance at the time of revaluation  """  
      self.Rpt2RevalueBal:int = obj["Rpt2RevalueBal"]
      """  Reporting currency Invoice Balance at the time of revaluation  """  
      self.Rpt3RevalueBal:int = obj["Rpt3RevalueBal"]
      """  Reporting currency Invoice Balance at the time of revaluation  """  
      self.BankID:str = obj["BankID"]
      """  Unique ID of the vendor's bank.  """  
      self.BankPaidAmt:int = obj["BankPaidAmt"]
      """  Amount Bank Paid  """  
      self.DocBankPaidAmt:int = obj["DocBankPaidAmt"]
      """  Amount Bank Paid  """  
      self.Rpt1BankPaidAmt:int = obj["Rpt1BankPaidAmt"]
      """  Amount Bank Paid  """  
      self.Rpt2BankPaidAmt:int = obj["Rpt2BankPaidAmt"]
      """  Amount Bank Paid  """  
      self.Rpt3BankPaidAmt:int = obj["Rpt3BankPaidAmt"]
      """  Amount Bank Paid  """  
      self.AdjLegalNumber:str = obj["AdjLegalNumber"]
      """  Legal Number for the adjustment.  """  
      self.AdjTranDocTypeID:str = obj["AdjTranDocTypeID"]
      """  Transaction Document Type for the adjustment.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Indicates the transaction document type for the record. A document type links a system transaction to a unique legal number.  """  
      self.MainSite:bool = obj["MainSite"]
      """  Main Site  """  
      self.SiteCode:str = obj["SiteCode"]
      """  Site Code  """  
      self.BranchID:str = obj["BranchID"]
      """  Branch ID  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice Date  """  
      self.Remarks:str = obj["Remarks"]
      """  Remarks  """  
      self.AssetTypeCode:str = obj["AssetTypeCode"]
      """  Asset Type Code  """  
      self.Cash:bool = obj["Cash"]
      """  Cash  """  
      self.CreditCard:bool = obj["CreditCard"]
      """  Credit Card  """  
      self.Normal:bool = obj["Normal"]
      """  Normal  """  
      self.CardID:str = obj["CardID"]
      """  Card ID  """  
      self.CardHolderTaxID:str = obj["CardHolderTaxID"]
      """  Card Holder Tax ID  """  
      self.CardMemberName:str = obj["CardMemberName"]
      """  Card Member Name  """  
      self.Excluded:bool = obj["Excluded"]
      """  Excluded  """  
      self.Deferred:bool = obj["Deferred"]
      """  Deferred  """  
      self.NonDeductAmt:int = obj["NonDeductAmt"]
      """  Non Deductable Amount  """  
      self.NonDeductDocAmt:int = obj["NonDeductDocAmt"]
      """  Non Deductable Doc Amount  """  
      self.NonDeductRpt1Amt:int = obj["NonDeductRpt1Amt"]
      """  Non Deductable Rpt1 Amount  """  
      self.NonDeductRpt2Amt:int = obj["NonDeductRpt2Amt"]
      """  Non Deductable Rpt2 Amount  """  
      self.NonDeductRpt3Amt:int = obj["NonDeductRpt3Amt"]
      """  Non Deductable Rpt3 Amount  """  
      self.PaymentNumber:str = obj["PaymentNumber"]
      """  PaymentNumber  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.UrgentPayment:bool = obj["UrgentPayment"]
      """  UrgentPayment  """  
      self.InvoiceRef:str = obj["InvoiceRef"]
      """  InvoiceRef  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Rate Group Code for transactions of type ADJ  """  
      self.CNCFICode:str = obj["CNCFICode"]
      """  CNCFICode  """  
      self.Gen1099Date:str = obj["Gen1099Date"]
      """  Generation 1099 Date  """  
      self.NOTranReason:str = obj["NOTranReason"]
      """  NOTranReason  """  
      self.PEIsDetractionPayment:bool = obj["PEIsDetractionPayment"]
      """  PEIsDetractionPayment  """  
      self.Code1099ID:str = obj["Code1099ID"]
      """  Code1099ID  """  
      self.FormTypeID:str = obj["FormTypeID"]
      """  FormTypeID  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.DocWhManAddAmt:int = obj["DocWhManAddAmt"]
      """  DocWhManAddAmt  """  
      self.WhManAddAmt:int = obj["WhManAddAmt"]
      """  WhManAddAmt  """  
      self.Rpt1WhManAddAmt:int = obj["Rpt1WhManAddAmt"]
      """  Rpt1WhManAddAmt  """  
      self.Rpt2WhManAddAmt:int = obj["Rpt2WhManAddAmt"]
      """  Rpt2WhManAddAmt  """  
      self.Rpt3WhManAddAmt:int = obj["Rpt3WhManAddAmt"]
      """  Rpt3WhManAddAmt  """  
      self.BaseAdjustAmt:int = obj["BaseAdjustAmt"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for BASE  """  
      self.BaseCurrSymbolCurrDesc:str = obj["BaseCurrSymbolCurrDesc"]
      self.BaseCurrSymbolCurrName:str = obj["BaseCurrSymbolCurrName"]
      self.BaseCurrSymbolCurrSymbol:str = obj["BaseCurrSymbolCurrSymbol"]
      self.BaseCurrSymbolDocumentDesc:str = obj["BaseCurrSymbolDocumentDesc"]
      self.BaseSelfAssessedTax:int = obj["BaseSelfAssessedTax"]
      self.ChangeExchangeRateResponse:str = obj["ChangeExchangeRateResponse"]
      """  Yes and No considered valid response.  All other values including blank treated as question was not posed to the user.  """  
      self.CNCFICodeDescription:str = obj["CNCFICodeDescription"]
      self.CopyRate:bool = obj["CopyRate"]
      """  If Copy Rate is true then original AP Invoice exchange rates are used when Adjustmet is applied and no currency gain/loss are calculated  """  
      self.CorrectionInv:bool = obj["CorrectionInv"]
      """  The flag to indicate if this payment line is realted to Correction invoice with negative amount  """  
      self.CPayLinked:bool = obj["CPayLinked"]
      """  Indicates if the related invoice is linked to a Central Payment invoice  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencyGainLoss:int = obj["CurrencyGainLoss"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      """  Currency.CurrSymbol from APInvHed  """  
      self.CurrSymbolCurrDesc:str = obj["CurrSymbolCurrDesc"]
      self.CurrSymbolCurrName:str = obj["CurrSymbolCurrName"]
      self.CurrSymbolCurrSymbol:str = obj["CurrSymbolCurrSymbol"]
      self.CurrSymbolDocumentDesc:str = obj["CurrSymbolDocumentDesc"]
      self.DebitMemo:bool = obj["DebitMemo"]
      self.DisableFieldsForPCashDoc:bool = obj["DisableFieldsForPCashDoc"]
      self.DiscountAvailable:bool = obj["DiscountAvailable"]
      self.DiscountDate:str = obj["DiscountDate"]
      self.DispGLAcct:str = obj["DispGLAcct"]
      """  The display gl account.  """  
      self.DispTranAmt:int = obj["DispTranAmt"]
      self.DocBaseSelfAssessedTax:int = obj["DocBaseSelfAssessedTax"]
      self.DocDispTranAmt:int = obj["DocDispTranAmt"]
      self.DocExpenseAmount:int = obj["DocExpenseAmount"]
      self.DocGainLossAmt:int = obj["DocGainLossAmt"]
      self.DocInvoiceAmt:int = obj["DocInvoiceAmt"]
      self.DocInvoiceBal:int = obj["DocInvoiceBal"]
      self.DocNetAmount:int = obj["DocNetAmount"]
      self.DocNewBalance:int = obj["DocNewBalance"]
      self.DocSelfAssessedTax:int = obj["DocSelfAssessedTax"]
      self.DocUnPostedBal:int = obj["DocUnPostedBal"]
      self.DocWithHoldTax:int = obj["DocWithHoldTax"]
      self.DsblCopyRate:bool = obj["DsblCopyRate"]
      """  If this flag is true then Copy Rate checkbox is Read Only  """  
      self.DueDate:str = obj["DueDate"]
      self.ExchangeRate:int = obj["ExchangeRate"]
      self.ExpenseAmount:int = obj["ExpenseAmount"]
      self.FullyPaid:bool = obj["FullyPaid"]
      """  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency.  """  
      self.GainLossAmt:int = obj["GainLossAmt"]
      self.GlbCompany:str = obj["GlbCompany"]
      """  This is the source Company of the Central Payment linked invoice  """  
      self.GroupID:str = obj["GroupID"]
      self.InitUrgentPayment:bool = obj["InitUrgentPayment"]
      """  CSF Switzerland - Initial value for Urgent Invoice Payment flag.  """  
      self.InvExchangeRate:int = obj["InvExchangeRate"]
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      self.InvoiceBal:int = obj["InvoiceBal"]
      self.isDiscountforDebitM:bool = obj["isDiscountforDebitM"]
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.LegalNumStyle:str = obj["LegalNumStyle"]
      """  Indicates if the legal number is manually generated or system generated  """  
      self.LockRate:bool = obj["LockRate"]
      self.MiscPayment:bool = obj["MiscPayment"]
      self.NetAmount:int = obj["NetAmount"]
      self.NewBalance:int = obj["NewBalance"]
      self.PaymentDesc:str = obj["PaymentDesc"]
      """  This field equals "Invoice" for Invoice payment, and "Misc" for Miscelleneous payment. This field  is used as label in tree.  """  
      self.PostErrMess:str = obj["PostErrMess"]
      """  Posting Error Message  """  
      self.PostToGL:bool = obj["PostToGL"]
      """  Indicates if posting GL transactions.  """  
      self.Print1099:bool = obj["Print1099"]
      """  Print 1099  """  
      self.RateGroupDescription:str = obj["RateGroupDescription"]
      self.RefCodeEnabled:bool = obj["RefCodeEnabled"]
      self.RefCodeList:str = obj["RefCodeList"]
      """  Delimited list of possible Ref codes.  """  
      self.RefCodeStatus:str = obj["RefCodeStatus"]
      """  Indicates if Reference Code is (M)andatory, (O)ptional, (E)xcluded or Blank.  Enable Reference Code if "M" or "O".  """  
      self.Rpt1DispTranAmt:int = obj["Rpt1DispTranAmt"]
      self.Rpt1GainLossAmt:int = obj["Rpt1GainLossAmt"]
      self.Rpt1InvoiceAmt:int = obj["Rpt1InvoiceAmt"]
      self.Rpt1InvoiceBal:int = obj["Rpt1InvoiceBal"]
      """  Invoice balance before adjustment in Rpt1 currency  """  
      self.Rpt1NewBalance:int = obj["Rpt1NewBalance"]
      self.Rpt2DispTranAmt:int = obj["Rpt2DispTranAmt"]
      self.Rpt2GainLossAmt:int = obj["Rpt2GainLossAmt"]
      self.Rpt2InvoiceAmt:int = obj["Rpt2InvoiceAmt"]
      self.Rpt2InvoiceBal:int = obj["Rpt2InvoiceBal"]
      """  Invoice balance before adjustment in Rpt2 currency  """  
      self.Rpt2NewBalance:int = obj["Rpt2NewBalance"]
      self.Rpt3DispTranAmt:int = obj["Rpt3DispTranAmt"]
      self.Rpt3GainLossAmt:int = obj["Rpt3GainLossAmt"]
      self.Rpt3InvoiceAmt:int = obj["Rpt3InvoiceAmt"]
      self.Rpt3InvoiceBal:int = obj["Rpt3InvoiceBal"]
      """  Report balance before adjustment in rpt3 currency  """  
      self.Rpt3NewBalance:int = obj["Rpt3NewBalance"]
      self.SelfAssessedTax:int = obj["SelfAssessedTax"]
      self.TaxableTransaction:bool = obj["TaxableTransaction"]
      """  Indicates if tax records are created and posted for AP Invoice adjustment  """  
      self.TaxLinesExist:bool = obj["TaxLinesExist"]
      self.TermsCode:str = obj["TermsCode"]
      self.TermsCodeDescription:str = obj["TermsCodeDescription"]
      self.UnPostedBal:int = obj["UnPostedBal"]
      """  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  """  
      self.WithHoldTax:int = obj["WithHoldTax"]
      self.XRateLabel:str = obj["XRateLabel"]
      self.AmtToAP:int = obj["AmtToAP"]
      self.ApplyDate:str = obj["ApplyDate"]
      self.InvoiceLegalNumber:str = obj["InvoiceLegalNumber"]
      self.PLInvoiceReference:str = obj["PLInvoiceReference"]
      self.isPrecalcTax:bool = obj["isPrecalcTax"]
      """  The internal flag to indicate if Tax Liability assigned to the invoice being paid has Witholding taxes with Payment timing (WH taxes will be precalculated)  """  
      self.PrepayApld:bool = obj["PrepayApld"]
      """  The flag to indicate if the invoice being paid (applied)in Payment Entry/Invoice Payment is AP Invoice created for Misc. Payment / Prepayment by the system.  """  
      self.ManualTaxAdj:bool = obj["ManualTaxAdj"]
      """  The flag related to Misc. payment to indicate if Tax records created per Tax Liability assigned to Misc. payment are adjusted,  deleted,  or any tax records were added by the user  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      self.Code1099Description:str = obj["Code1099Description"]
      self.FormTypeDescription:str = obj["FormTypeDescription"]
      self.InvoiceNumDescription:str = obj["InvoiceNumDescription"]
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APTranTGLCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "PORel" control this field would contain the related PO Number.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.   For example: For a "PORel" control this field would contain the related PO Line Number.
The usage of this field is dependent on the type of record.  """  
      self.Key3:str = obj["Key3"]
      """  3rd component of the foreign key to the related master record.  For example: For a "PORel" control this field would contain the related PO Release Number.  The usage of this field is dependent record type.  """  
      self.Key4:str = obj["Key4"]
      """   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key5:str = obj["Key5"]
      """   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key6:str = obj["Key6"]
      """   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.TGLCTranNum:int = obj["TGLCTranNum"]
      """  Internal identifier used to keep records unique for the related record.  The system generates this number by finding the last TranGLC record for the RelatedToFile-Key1-Key2 etc. and adding 1 to it.  """  
      self.GLAcctContext:str = obj["GLAcctContext"]
      """  String identifier of the account context.  """  
      self.BookID:str = obj["BookID"]
      """  Reference to an accounting book.  If not blank must be a valid entry in the GLBook table.  """  
      self.COACode:str = obj["COACode"]
      """  The chart of account code used by the book.  Will contain the Master COA when BookID is blank.  Reference only.  Used for integrity checking when updating/deleting a GL account.  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Full account containing the non-dynamic segment values up to 200 characters.  Unique identifier for the GL Account.  """  
      self.UserCanModify:bool = obj["UserCanModify"]
      """  Indicates if the user can update or delete this record.  """  
      self.SegValue1:str = obj["SegValue1"]
      """  Segement Value 1 of the account for this context.  """  
      self.SegValue2:str = obj["SegValue2"]
      """  Segement Value 2 of the account for this context.  """  
      self.SegValue3:str = obj["SegValue3"]
      """  Segement Value 3 of the account for this context.  """  
      self.SegValue4:str = obj["SegValue4"]
      """  Segement Value 4 of the account for this context.  """  
      self.SegValue5:str = obj["SegValue5"]
      """  Segement Value 5 of the account for this context.  """  
      self.SegValue6:str = obj["SegValue6"]
      """  Segement Value 6 of the account for this context.  """  
      self.SegValue7:str = obj["SegValue7"]
      """  Segement Value 7 of the account for this context.  """  
      self.SegValue8:str = obj["SegValue8"]
      """  Segement Value 8 of the account for this context.  """  
      self.SegValue9:str = obj["SegValue9"]
      """  Segement Value 9 of the account for this context.  """  
      self.SegValue10:str = obj["SegValue10"]
      """  Segement Value 10 of the account for this context.  """  
      self.SegValue11:str = obj["SegValue11"]
      """  Segement Value 11 of the account for this context.  """  
      self.SegValue12:str = obj["SegValue12"]
      """  Segement Value 12 of the account for this context.  """  
      self.SegValue13:str = obj["SegValue13"]
      """  Segement Value 13 of the account for this context.  """  
      self.SegValue14:str = obj["SegValue14"]
      """  Segement Value 14 of the account for this context.  """  
      self.SegValue15:str = obj["SegValue15"]
      """  Segement Value 15 of the account for this context.  """  
      self.SegValue16:str = obj["SegValue16"]
      """  Segement Value 16 of the account for this context.  """  
      self.SegValue17:str = obj["SegValue17"]
      """  Segement Value 17 of the account for this context.  """  
      self.SegValue18:str = obj["SegValue18"]
      """  Segement Value 18 of the account for this context.  """  
      self.SegValue19:str = obj["SegValue19"]
      """  Segement Value 19 of the account for this context.  """  
      self.SegValue20:str = obj["SegValue20"]
      """  Segement Value 20 of the account for this context.  """  
      self.SysGLControlType:str = obj["SysGLControlType"]
      """  Unique Identifier of the system GL Control Type.  """  
      self.SysGLControlCode:str = obj["SysGLControlCode"]
      """  System generated GL Control Identifier.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.IsExternalCompany:bool = obj["IsExternalCompany"]
      """  Flag to indicate the account in this record is for an external company.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal year of the related GLJrnDtl.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  JournalCode of the related GLJrnDtl.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  Journal number of the related GLJrnDtl.  """  
      self.JournalLine:int = obj["JournalLine"]
      """  JournalLine of the related GLJrnDtl.  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction date of the transaction.  This is used in order to display the transactions in date order.  """  
      self.TranSource:str = obj["TranSource"]
      """   An internal code to identify the table of  the source transaction.
P = PartTran
L = LaborDtl
I = InvcHead
Note: The system does not combine TranSource when creating GLJrnDtl. That is, a specific GLJrnDtl record can only be related to one source.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  LaborHedSeq of the related LaborDtl.  Pertains only to source from LaborDtl (TranSource = "L")  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  LaborDtlSeq of the related LaborDtl. Pertains only to source from LaborDtl (TranSource = "L")  """  
      self.SysDate:str = obj["SysDate"]
      """  System date of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.SysTime:int = obj["SysTime"]
      """  System time of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.TranNum:int = obj["TranNum"]
      """  TranNum of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.ARInvoiceNum:int = obj["ARInvoiceNum"]
      """  InvoiceNum of the related InvcHead record.  Pertains only to source from PartTran (TranSource = "I")  """  
      self.TransAmt:int = obj["TransAmt"]
      """  Transaction amount that this transaction posted to the related GlJrnDtl.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Invoice Line Number associated with this GL Journal  """  
      self.SeqNum:int = obj["SeqNum"]
      """  The sequence number associated with this GL journal  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  Vendor's invoice number.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Date record was created  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.CreditAmount:int = obj["CreditAmount"]
      """  Credit Amount.  """  
      self.DebitAmount:int = obj["DebitAmount"]
      """  Debit Amount.  """  
      self.BookCreditAmount:int = obj["BookCreditAmount"]
      """  BookCreditAmount  """  
      self.BookDebitAmount:int = obj["BookDebitAmount"]
      """  Book Debit Amount  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the document currency.  """  
      self.RecordType:str = obj["RecordType"]
      """   Indicates if this record contains account data only or reference data such as journal number, amounts, etc.  Valid  values are:
A - account data only
R - reference data  """  
      self.CorrAccUID:int = obj["CorrAccUID"]
      """  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  """  
      self.ABTUID:str = obj["ABTUID"]
      """  this field equals ABTUID which was created during posting  """  
      self.RuleUID:int = obj["RuleUID"]
      """  Technical identifier.  """  
      self.Statistical:int = obj["Statistical"]
      """   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  """  
      self.StatUOMCode:str = obj["StatUOMCode"]
      """  Statistical UOM code.  """  
      self.DebitStatAmt:int = obj["DebitStatAmt"]
      """  This field shows Debit statistical amount.  """  
      self.CreditStatAmt:int = obj["CreditStatAmt"]
      """  This field shows Credit statistical amount.  """  
      self.IsModifiedByUser:bool = obj["IsModifiedByUser"]
      """  IsModifiedByUser  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MovementNum:int = obj["MovementNum"]
      """  MovementNum  """  
      self.MovementType:str = obj["MovementType"]
      """  MovementType  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.GroupID:str = obj["GroupID"]
      """  GroupID of APTran  """  
      self.HeadNum:int = obj["HeadNum"]
      """  HeadNum of APTran  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  InvoiceNum of APTran  """  
      self.Voided:bool = obj["Voided"]
      """  Voided of APTran  """  
      self.APTranNo:int = obj["APTranNo"]
      """  APTranNo of APTran  """  
      self.BitFlag:int = obj["BitFlag"]
      self.COADescription:str = obj["COADescription"]
      self.GLAccountAccountDesc:str = obj["GLAccountAccountDesc"]
      self.GLAccountGLAcctDisp:str = obj["GLAccountGLAcctDisp"]
      self.GLAccountGLShortAcct:str = obj["GLAccountGLShortAcct"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LegalNumberID:str = obj["LegalNumberID"]
      self.TransYear:int = obj["TransYear"]
      self.TransYearSuffix:str = obj["TransYearSuffix"]
      self.DspTransYear:str = obj["DspTransYear"]
      self.ShowDspTransYear:bool = obj["ShowDspTransYear"]
      """  Indicates if DspTransYear should be displayed when prompting for a manual number.  """  
      self.Prefix:str = obj["Prefix"]
      self.PrefixList:str = obj["PrefixList"]
      """  The list of prefixes that can be selected by the user for manual numbers.  """  
      self.NumberSuffix:str = obj["NumberSuffix"]
      """  The suffix portion of the legal number.  """  
      self.EnablePrefix:bool = obj["EnablePrefix"]
      """  Indicates if the prefix can be entered by the user.  """  
      self.EnableSuffix:bool = obj["EnableSuffix"]
      """  Indicates if the suffix (number) can be entered by the user.  """  
      self.NumberOption:str = obj["NumberOption"]
      self.DocumentDate:str = obj["DocumentDate"]
      self.GenerationType:str = obj["GenerationType"]
      self.Description:str = obj["Description"]
      self.TransPeriod:int = obj["TransPeriod"]
      self.PeriodPrefix:str = obj["PeriodPrefix"]
      """  Prefix for the period  """  
      self.ShowTransPeriod:bool = obj["ShowTransPeriod"]
      self.LegalNumber:str = obj["LegalNumber"]
      """  Used when the full legal number is entered  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      self.TranDocTypeID2:str = obj["TranDocTypeID2"]
      self.GenerationOption:str = obj["GenerationOption"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtAPAdjustmentTableset:
   def __init__(self, obj):
      self.APInvHedAdj:list[Erp_Tablesets_APInvHedAdjRow] = obj["APInvHedAdj"]
      self.APTran:list[Erp_Tablesets_APTranRow] = obj["APTran"]
      self.APTranTGLC:list[Erp_Tablesets_APTranTGLCRow] = obj["APTranTGLC"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetAvailTranDocTypes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.availTypes:str = obj["parameters"]
      pass

      """  output parameters  """  

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
      self.returnObj:list[Erp_Tablesets_APAdjustmentTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_APAdjustmentTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_APAdjustmentTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  The table name.  """  
      self.fieldName:str = obj["fieldName"]
      """  The field name.  """  
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_APInvHedAdjListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewAPInvHedAdj_input:
   """ Required : 
   ds
   vendorNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APAdjustmentTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      pass

class GetNewAPInvHedAdj_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APAdjustmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewAPTran1_input:
   """ Required : 
   ds
   ipVendorNum
   ipInvoiceNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APAdjustmentTableset] = obj["ds"]
      self.ipVendorNum:int = obj["ipVendorNum"]
      """  The Vendor Number for this A/P invoice adjustment  """  
      self.ipInvoiceNum:str = obj["ipInvoiceNum"]
      """  The A/P Invoice Number for adjustment  """  
      pass

class GetNewAPTran1_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APAdjustmentTableset] = obj["ds"]
      self.opXRateLabel:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetNewAPTranTGLC_input:
   """ Required : 
   ds
   headNum
   apTranNo
   invoiceNum
   voided
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APAdjustmentTableset] = obj["ds"]
      self.headNum:int = obj["headNum"]
      self.apTranNo:int = obj["apTranNo"]
      self.invoiceNum:str = obj["invoiceNum"]
      self.voided:bool = obj["voided"]
      pass

class GetNewAPTranTGLC_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APAdjustmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewAPTran_input:
   """ Required : 
   ds
   headNum
   apTranNo
   invoiceNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APAdjustmentTableset] = obj["ds"]
      self.headNum:int = obj["headNum"]
      self.apTranNo:int = obj["apTranNo"]
      self.invoiceNum:str = obj["invoiceNum"]
      pass

class GetNewAPTran_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APAdjustmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseAPInvHedAdj
   whereClauseAPTran
   whereClauseAPTranTGLC
   whereClauseLegalNumGenOpts
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseAPInvHedAdj:str = obj["whereClauseAPInvHedAdj"]
      self.whereClauseAPTran:str = obj["whereClauseAPTran"]
      self.whereClauseAPTranTGLC:str = obj["whereClauseAPTranTGLC"]
      self.whereClauseLegalNumGenOpts:str = obj["whereClauseLegalNumGenOpts"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_APAdjustmentTableset] = obj["returnObj"]
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

class PreUpdate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APAdjustmentTableset] = obj["ds"]
      pass

class PreUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APAdjustmentTableset] = obj["ds"]
      self.requiresUserInput:bool = obj["requiresUserInput"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtAPAdjustmentTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtAPAdjustmentTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APAdjustmentTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APAdjustmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

