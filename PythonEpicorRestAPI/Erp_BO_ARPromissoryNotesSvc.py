import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ARPromissoryNotesSvc
# Description: The AR promissory note service.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ARPromissoryNotes(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ARPromissoryNotes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ARPromissoryNotes
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARPNHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPromissoryNotes",headers=creds) as resp:
           return await resp.json()

async def post_ARPromissoryNotes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ARPromissoryNotes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ARPNHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ARPNHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPromissoryNotes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ARPromissoryNotes_Company_GroupID_HeadNum(Company, GroupID, HeadNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ARPromissoryNote item
   Description: Calls GetByID to retrieve the ARPromissoryNote item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ARPromissoryNote
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ARPNHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ARPromissoryNotes_Company_GroupID_HeadNum(Company, GroupID, HeadNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ARPromissoryNote for the service
   Description: Calls UpdateExt to update ARPromissoryNote. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ARPromissoryNote
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ARPNHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ARPromissoryNotes_Company_GroupID_HeadNum(Company, GroupID, HeadNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ARPromissoryNote item
   Description: Call UpdateExt to delete ARPromissoryNote item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ARPromissoryNote
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_ARPromissoryNotes_Company_GroupID_HeadNum_BankTrans(Company, GroupID, HeadNum, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get BankTrans items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BankTrans1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BankTranRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")/BankTrans",headers=creds) as resp:
           return await resp.json()

async def get_ARPromissoryNotes_Company_GroupID_HeadNum_BankTrans_Company_BankAcctID_TranNum_Voided(Company, GroupID, HeadNum, BankAcctID, TranNum, Voided, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BankTran item
   Description: Calls GetByID to retrieve the BankTran item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BankTran1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param Voided: Desc: Voided   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BankTranRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")",headers=creds) as resp:
           return await resp.json()

async def get_ARPromissoryNotes_Company_GroupID_HeadNum_ARPNDtls(Company, GroupID, HeadNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ARPNDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ARPNDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARPNDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")/ARPNDtls",headers=creds) as resp:
           return await resp.json()

async def get_ARPromissoryNotes_Company_GroupID_HeadNum_ARPNDtls_Company_HeadNum_InvoiceNum_InvoiceRef(Company, GroupID, HeadNum, InvoiceNum, InvoiceRef, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ARPNDtl item
   Description: Calls GetByID to retrieve the ARPNDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ARPNDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceRef: Desc: InvoiceRef   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ARPNDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")/ARPNDtls(" + Company + "," + HeadNum + "," + InvoiceNum + "," + InvoiceRef + ")",headers=creds) as resp:
           return await resp.json()

async def get_ARPromissoryNotes_Company_GroupID_HeadNum_TaxDtls(Company, GroupID, HeadNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get TaxDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TaxDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")/TaxDtls",headers=creds) as resp:
           return await resp.json()

async def get_ARPromissoryNotes_Company_GroupID_HeadNum_TaxDtls_Company_SourceModule_HeadNum_APTranNo_InvoiceNum_InvoiceRef_BankAcctID_TranNum_Voided_TaxCode_RateCode_ECAcquisitionSeq(Company, GroupID, HeadNum, SourceModule, APTranNo, InvoiceNum, InvoiceRef, BankAcctID, TranNum, Voided, TaxCode, RateCode, ECAcquisitionSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaxDtl item
   Description: Calls GetByID to retrieve the TaxDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param SourceModule: Desc: SourceModule   Required: True   Allow empty value : True
      :param APTranNo: Desc: APTranNo   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceRef: Desc: InvoiceRef   Required: True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param Voided: Desc: Voided   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")/TaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ARPromissoryNotes_Company_GroupID_HeadNum_ARPNHeadTGLCs(Company, GroupID, HeadNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ARPNHeadTGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ARPNHeadTGLCs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARPNHeadTGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")/ARPNHeadTGLCs",headers=creds) as resp:
           return await resp.json()

async def get_ARPromissoryNotes_Company_GroupID_HeadNum_ARPNHeadTGLCs_Company_GroupID_HeadNum_TGLCTranNum(Company, GroupID, HeadNum, TGLCTranNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ARPNHeadTGLC item
   Description: Calls GetByID to retrieve the ARPNHeadTGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ARPNHeadTGLC1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param TGLCTranNum: Desc: TGLCTranNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ARPNHeadTGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")/ARPNHeadTGLCs(" + Company + "," + GroupID + "," + HeadNum + "," + TGLCTranNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_ARPromissoryNotes_Company_GroupID_HeadNum_ARPNHeadAttches(Company, GroupID, HeadNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ARPNHeadAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ARPNHeadAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARPNHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")/ARPNHeadAttches",headers=creds) as resp:
           return await resp.json()

async def get_ARPromissoryNotes_Company_GroupID_HeadNum_ARPNHeadAttches_Company_GroupID_HeadNum_DrawingSeq(Company, GroupID, HeadNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ARPNHeadAttch item
   Description: Calls GetByID to retrieve the ARPNHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ARPNHeadAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ARPNHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")/ARPNHeadAttches(" + Company + "," + GroupID + "," + HeadNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_BankTrans(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BankTrans items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BankTrans
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BankTranRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/BankTrans",headers=creds) as resp:
           return await resp.json()

async def post_BankTrans(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BankTrans
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BankTranRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.BankTranRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/BankTrans", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BankTrans_Company_BankAcctID_TranNum_Voided(Company, BankAcctID, TranNum, Voided, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BankTran item
   Description: Calls GetByID to retrieve the BankTran item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BankTran
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param Voided: Desc: Voided   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BankTranRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BankTrans_Company_BankAcctID_TranNum_Voided(Company, BankAcctID, TranNum, Voided, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BankTran for the service
   Description: Calls UpdateExt to update BankTran. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BankTran
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param Voided: Desc: Voided   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.BankTranRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BankTrans_Company_BankAcctID_TranNum_Voided(Company, BankAcctID, TranNum, Voided, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BankTran item
   Description: Call UpdateExt to delete BankTran item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BankTran
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")",headers=creds) as resp:
           return await resp.json()

async def get_BankTrans_Company_BankAcctID_TranNum_Voided_BankTranTaxDtls(Company, BankAcctID, TranNum, Voided, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get BankTranTaxDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BankTranTaxDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BankTranTaxDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")/BankTranTaxDtls",headers=creds) as resp:
           return await resp.json()

async def get_BankTrans_Company_BankAcctID_TranNum_Voided_BankTranTaxDtls_Company_SourceModule_HeadNum_APTranNo_InvoiceNum_InvoiceRef_BankAcctID_TranNum_Voided_TaxCode_RateCode_ECAcquisitionSeq(Company, BankAcctID, TranNum, Voided, SourceModule, HeadNum, APTranNo, InvoiceNum, InvoiceRef, TaxCode, RateCode, ECAcquisitionSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BankTranTaxDtl item
   Description: Calls GetByID to retrieve the BankTranTaxDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BankTranTaxDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param Voided: Desc: Voided   Required: True
      :param SourceModule: Desc: SourceModule   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param APTranNo: Desc: APTranNo   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceRef: Desc: InvoiceRef   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BankTranTaxDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")/BankTranTaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_BankTrans_Company_BankAcctID_TranNum_Voided_BankTranTGLCs(Company, BankAcctID, TranNum, Voided, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get BankTranTGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BankTranTGLCs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BankTranTGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")/BankTranTGLCs",headers=creds) as resp:
           return await resp.json()

async def get_BankTrans_Company_BankAcctID_TranNum_Voided_BankTranTGLCs_Company_BankAcctID_TranNum_Voided_SysRowID(Company, BankAcctID, TranNum, Voided, SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BankTranTGLC item
   Description: Calls GetByID to retrieve the BankTranTGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BankTranTGLC1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param Voided: Desc: Voided   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BankTranTGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")/BankTranTGLCs(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + "," + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_BankTranTaxDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BankTranTaxDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BankTranTaxDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BankTranTaxDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/BankTranTaxDtls",headers=creds) as resp:
           return await resp.json()

async def post_BankTranTaxDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BankTranTaxDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BankTranTaxDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.BankTranTaxDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/BankTranTaxDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BankTranTaxDtls_Company_SourceModule_HeadNum_APTranNo_InvoiceNum_InvoiceRef_BankAcctID_TranNum_Voided_TaxCode_RateCode_ECAcquisitionSeq(Company, SourceModule, HeadNum, APTranNo, InvoiceNum, InvoiceRef, BankAcctID, TranNum, Voided, TaxCode, RateCode, ECAcquisitionSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BankTranTaxDtl item
   Description: Calls GetByID to retrieve the BankTranTaxDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BankTranTaxDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SourceModule: Desc: SourceModule   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param APTranNo: Desc: APTranNo   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceRef: Desc: InvoiceRef   Required: True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param Voided: Desc: Voided   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BankTranTaxDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/BankTranTaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BankTranTaxDtls_Company_SourceModule_HeadNum_APTranNo_InvoiceNum_InvoiceRef_BankAcctID_TranNum_Voided_TaxCode_RateCode_ECAcquisitionSeq(Company, SourceModule, HeadNum, APTranNo, InvoiceNum, InvoiceRef, BankAcctID, TranNum, Voided, TaxCode, RateCode, ECAcquisitionSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BankTranTaxDtl for the service
   Description: Calls UpdateExt to update BankTranTaxDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BankTranTaxDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SourceModule: Desc: SourceModule   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param APTranNo: Desc: APTranNo   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceRef: Desc: InvoiceRef   Required: True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param Voided: Desc: Voided   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.BankTranTaxDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/BankTranTaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BankTranTaxDtls_Company_SourceModule_HeadNum_APTranNo_InvoiceNum_InvoiceRef_BankAcctID_TranNum_Voided_TaxCode_RateCode_ECAcquisitionSeq(Company, SourceModule, HeadNum, APTranNo, InvoiceNum, InvoiceRef, BankAcctID, TranNum, Voided, TaxCode, RateCode, ECAcquisitionSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BankTranTaxDtl item
   Description: Call UpdateExt to delete BankTranTaxDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BankTranTaxDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SourceModule: Desc: SourceModule   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param APTranNo: Desc: APTranNo   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceRef: Desc: InvoiceRef   Required: True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param Voided: Desc: Voided   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/BankTranTaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_BankTranTGLCs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BankTranTGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BankTranTGLCs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BankTranTGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/BankTranTGLCs",headers=creds) as resp:
           return await resp.json()

async def post_BankTranTGLCs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BankTranTGLCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BankTranTGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.BankTranTGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/BankTranTGLCs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BankTranTGLCs_Company_BankAcctID_TranNum_Voided_SysRowID(Company, BankAcctID, TranNum, Voided, SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BankTranTGLC item
   Description: Calls GetByID to retrieve the BankTranTGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BankTranTGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param Voided: Desc: Voided   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BankTranTGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/BankTranTGLCs(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + "," + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BankTranTGLCs_Company_BankAcctID_TranNum_Voided_SysRowID(Company, BankAcctID, TranNum, Voided, SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BankTranTGLC for the service
   Description: Calls UpdateExt to update BankTranTGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BankTranTGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param Voided: Desc: Voided   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.BankTranTGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/BankTranTGLCs(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + "," + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BankTranTGLCs_Company_BankAcctID_TranNum_Voided_SysRowID(Company, BankAcctID, TranNum, Voided, SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BankTranTGLC item
   Description: Call UpdateExt to delete BankTranTGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BankTranTGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/BankTranTGLCs(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + "," + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ARPNDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ARPNDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ARPNDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARPNDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPNDtls",headers=creds) as resp:
           return await resp.json()

async def post_ARPNDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ARPNDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ARPNDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ARPNDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPNDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ARPNDtls_Company_HeadNum_InvoiceNum_InvoiceRef(Company, HeadNum, InvoiceNum, InvoiceRef, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ARPNDtl item
   Description: Calls GetByID to retrieve the ARPNDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ARPNDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceRef: Desc: InvoiceRef   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ARPNDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPNDtls(" + Company + "," + HeadNum + "," + InvoiceNum + "," + InvoiceRef + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ARPNDtls_Company_HeadNum_InvoiceNum_InvoiceRef(Company, HeadNum, InvoiceNum, InvoiceRef, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ARPNDtl for the service
   Description: Calls UpdateExt to update ARPNDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ARPNDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceRef: Desc: InvoiceRef   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ARPNDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPNDtls(" + Company + "," + HeadNum + "," + InvoiceNum + "," + InvoiceRef + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ARPNDtls_Company_HeadNum_InvoiceNum_InvoiceRef(Company, HeadNum, InvoiceNum, InvoiceRef, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ARPNDtl item
   Description: Call UpdateExt to delete ARPNDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ARPNDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceRef: Desc: InvoiceRef   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPNDtls(" + Company + "," + HeadNum + "," + InvoiceNum + "," + InvoiceRef + ")",headers=creds) as resp:
           return await resp.json()

async def get_TaxDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TaxDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TaxDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/TaxDtls",headers=creds) as resp:
           return await resp.json()

async def post_TaxDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TaxDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaxDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TaxDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/TaxDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TaxDtls_Company_SourceModule_HeadNum_APTranNo_InvoiceNum_InvoiceRef_BankAcctID_TranNum_Voided_TaxCode_RateCode_ECAcquisitionSeq(Company, SourceModule, HeadNum, APTranNo, InvoiceNum, InvoiceRef, BankAcctID, TranNum, Voided, TaxCode, RateCode, ECAcquisitionSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaxDtl item
   Description: Calls GetByID to retrieve the TaxDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SourceModule: Desc: SourceModule   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param APTranNo: Desc: APTranNo   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceRef: Desc: InvoiceRef   Required: True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param Voided: Desc: Voided   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/TaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TaxDtls_Company_SourceModule_HeadNum_APTranNo_InvoiceNum_InvoiceRef_BankAcctID_TranNum_Voided_TaxCode_RateCode_ECAcquisitionSeq(Company, SourceModule, HeadNum, APTranNo, InvoiceNum, InvoiceRef, BankAcctID, TranNum, Voided, TaxCode, RateCode, ECAcquisitionSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TaxDtl for the service
   Description: Calls UpdateExt to update TaxDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TaxDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SourceModule: Desc: SourceModule   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param APTranNo: Desc: APTranNo   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceRef: Desc: InvoiceRef   Required: True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param Voided: Desc: Voided   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaxDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/TaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TaxDtls_Company_SourceModule_HeadNum_APTranNo_InvoiceNum_InvoiceRef_BankAcctID_TranNum_Voided_TaxCode_RateCode_ECAcquisitionSeq(Company, SourceModule, HeadNum, APTranNo, InvoiceNum, InvoiceRef, BankAcctID, TranNum, Voided, TaxCode, RateCode, ECAcquisitionSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TaxDtl item
   Description: Call UpdateExt to delete TaxDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TaxDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SourceModule: Desc: SourceModule   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param APTranNo: Desc: APTranNo   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceRef: Desc: InvoiceRef   Required: True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param Voided: Desc: Voided   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/TaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ARPNHeadTGLCs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ARPNHeadTGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ARPNHeadTGLCs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARPNHeadTGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPNHeadTGLCs",headers=creds) as resp:
           return await resp.json()

async def post_ARPNHeadTGLCs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ARPNHeadTGLCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ARPNHeadTGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ARPNHeadTGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPNHeadTGLCs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ARPNHeadTGLCs_Company_GroupID_HeadNum_TGLCTranNum(Company, GroupID, HeadNum, TGLCTranNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ARPNHeadTGLC item
   Description: Calls GetByID to retrieve the ARPNHeadTGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ARPNHeadTGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param TGLCTranNum: Desc: TGLCTranNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ARPNHeadTGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPNHeadTGLCs(" + Company + "," + GroupID + "," + HeadNum + "," + TGLCTranNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ARPNHeadTGLCs_Company_GroupID_HeadNum_TGLCTranNum(Company, GroupID, HeadNum, TGLCTranNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ARPNHeadTGLC for the service
   Description: Calls UpdateExt to update ARPNHeadTGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ARPNHeadTGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param TGLCTranNum: Desc: TGLCTranNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ARPNHeadTGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPNHeadTGLCs(" + Company + "," + GroupID + "," + HeadNum + "," + TGLCTranNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ARPNHeadTGLCs_Company_GroupID_HeadNum_TGLCTranNum(Company, GroupID, HeadNum, TGLCTranNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ARPNHeadTGLC item
   Description: Call UpdateExt to delete ARPNHeadTGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ARPNHeadTGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param TGLCTranNum: Desc: TGLCTranNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPNHeadTGLCs(" + Company + "," + GroupID + "," + HeadNum + "," + TGLCTranNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_ARPNHeadAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ARPNHeadAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ARPNHeadAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARPNHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPNHeadAttches",headers=creds) as resp:
           return await resp.json()

async def post_ARPNHeadAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ARPNHeadAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ARPNHeadAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ARPNHeadAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPNHeadAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ARPNHeadAttches_Company_GroupID_HeadNum_DrawingSeq(Company, GroupID, HeadNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ARPNHeadAttch item
   Description: Calls GetByID to retrieve the ARPNHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ARPNHeadAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ARPNHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPNHeadAttches(" + Company + "," + GroupID + "," + HeadNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ARPNHeadAttches_Company_GroupID_HeadNum_DrawingSeq(Company, GroupID, HeadNum, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ARPNHeadAttch for the service
   Description: Calls UpdateExt to update ARPNHeadAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ARPNHeadAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ARPNHeadAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPNHeadAttches(" + Company + "," + GroupID + "," + HeadNum + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ARPNHeadAttches_Company_GroupID_HeadNum_DrawingSeq(Company, GroupID, HeadNum, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ARPNHeadAttch item
   Description: Call UpdateExt to delete ARPNHeadAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ARPNHeadAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPNHeadAttches(" + Company + "," + GroupID + "," + HeadNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ARPNLists(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ARPNLists items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ARPNLists
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARPNListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPNLists",headers=creds) as resp:
           return await resp.json()

async def post_ARPNLists(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ARPNLists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ARPNListRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ARPNListRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPNLists", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ARPNLists_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ARPNList item
   Description: Calls GetByID to retrieve the ARPNList item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ARPNList
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ARPNListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPNLists(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ARPNLists_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ARPNList for the service
   Description: Calls UpdateExt to update ARPNList. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ARPNList
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ARPNListRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPNLists(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ARPNLists_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ARPNList item
   Description: Call UpdateExt to delete ARPNList item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ARPNList
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/ARPNLists(" + SysRowID + ")",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/LegalNumGenOpts",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/LegalNumGenOpts", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
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
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", json=requestBody,headers=creds) as resp:
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARPNHeadListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseARPNHead, whereClauseARPNHeadAttch, whereClauseBankTran, whereClauseBankTranTaxDtl, whereClauseBankTranTGLC, whereClauseARPNDtl, whereClauseTaxDtl, whereClauseARPNHeadTGLC, whereClauseARPNList, whereClauseLegalNumGenOpts, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "whereClauseARPNHead=" + whereClauseARPNHead
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseARPNHeadAttch=" + whereClauseARPNHeadAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseBankTran=" + whereClauseBankTran
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseBankTranTaxDtl=" + whereClauseBankTranTaxDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseBankTranTGLC=" + whereClauseBankTranTGLC
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseARPNDtl=" + whereClauseARPNDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseTaxDtl=" + whereClauseTaxDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseARPNHeadTGLC=" + whereClauseARPNHeadTGLC
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseARPNList=" + whereClauseARPNList
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(groupID, headNum, epicorHeaders = None):
   """  
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
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "groupID=" + groupID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "headNum=" + headNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetAvailTranDocTypes(epicorHeaders = None):
   """  
   Summary: Invoke method GetAvailTranDocTypes
   Description: GetAvailTranDocTypes
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   Description: GetCodeDescList
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BatchGenPIs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BatchGenPIs
   OperationID: BatchGenPIs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BatchGenPIs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BatchGenPIs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CancelGenPI(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CancelGenPI
   Description: CancelGenPI
   OperationID: CancelGenPI
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CancelGenPI_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CancelGenPI_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCurGroupID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCurGroupID
   Description: ChangeCurGroupID
   OperationID: ChangeCurGroupID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCurGroupID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCurGroupID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTranAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTranAmt
   Description: This method updates the BankTran amounts when the adjustment amount changes or
the currency switch toggles.
   OperationID: ChangeTranAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTranAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTranAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPNoteExisted(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPNoteExisted
   Description: CheckPNoteExisted
   OperationID: CheckPNoteExisted
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPNoteExisted_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPNoteExisted_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPNotesExistTracker(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPNotesExistTracker
   Description: Checks to see if any AR Promissory Notes exist for a given promissory note ID
regardless of customer number or PI type
   OperationID: CheckPNotesExistTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPNotesExistTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPNotesExistTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateARPNMove(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateARPNMove
   Description: CreateARPNMove
   OperationID: CreateARPNMove
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateARPNMove_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateARPNMove_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DelARPNHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DelARPNHead
   Description: Delete the AR Payment Instrument
   OperationID: DelARPNHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DelARPNHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DelARPNHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeletePICashGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeletePICashGroup
   Description: This method deletes a CashGrp from AR Invoice Entry
   OperationID: DeletePICashGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeletePICashGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeletePICashGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeletePNbyID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeletePNbyID
   Description: DeletePNbyID
   OperationID: DeletePNbyID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeletePNbyID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeletePNbyID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeletePNotes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeletePNotes
   Description: DeletePNotes
   OperationID: DeletePNotes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeletePNotes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeletePNotes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteZeroAmtTaxRec(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteZeroAmtTaxRec
   Description: This method deletes TaxDtl records which have zero amounts
Since Payments TAx logic calculates tax conditionally only for the first tax line the payment could have multiple zero tax records.
   OperationID: DeleteZeroAmtTaxRec
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteZeroAmtTaxRec_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteZeroAmtTaxRec_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_KineticFillPNSummary(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method KineticFillPNSummary
   Description: Method to call when obtaining the payment schedule for the invoice header.
   OperationID: KineticFillPNSummary
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/KineticFillPNSummary_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/KineticFillPNSummary_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FillPNSummary(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FillPNSummary
   Description: Method to call when obtaining the payment schedule for the invoice header.
   OperationID: FillPNSummary
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FillPNSummary_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FillPNSummary_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateARPNDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateARPNDtl
   Description: This method combines the GetNewARPNDtl and Update() method into one routine
so that the user can run an "Auto Apply" cash receipt function
   OperationID: GenerateARPNDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateARPNDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateARPNDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateARPNDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateARPNDtls
   Description: This method combines the GetNewARPNDtl and Update() method into one routine
so that the user can run an "Auto Apply" cash receipt function
   OperationID: GenerateARPNDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateARPNDtls_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateARPNDtls_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetARPNList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetARPNList
   OperationID: GetARPNList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetARPNList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetARPNList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetARPNListTracker(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetARPNListTracker
   Description: Create a list of ARPN for a certail ARPromNoteID regardless of customer, type or post status
   OperationID: GetARPNListTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetARPNListTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetARPNListTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetARPNMove(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetARPNMove
   Description: Get the ARPNMove records for an ARPromissoryNote.
   OperationID: GetARPNMove
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetARPNMove_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetARPNMove_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetBankAcctInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetBankAcctInfo
   Description: This method is called when the BankAcctID field is modified
   OperationID: GetBankAcctInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBankAcctInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBankAcctInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetBankFeeDefaultAccount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetBankFeeDefaultAccount
   Description: This method is used to get the default account(s) for a Bank Fee
   OperationID: GetBankFeeDefaultAccount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBankFeeDefaultAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBankFeeDefaultAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetById4PITracker(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetById4PITracker
   Description: Procedure wrapper for procedure GetById for PI tracker to prevent removing ARPNHead when there is not
corresponded record in CashGrp table.(It was removed after posting in post_post file)
   OperationID: GetById4PITracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetById4PITracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetById4PITracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRows4Tracker(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows4Tracker
   Description: The method wrapper for the GetRows method for A/R Payment Instrument tracker to prevent removing ARPNHead when there is not
corresponded record in CashGrp table.
   OperationID: GetRows4Tracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRows4Tracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows4Tracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCurrencyCodeForBatch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCurrencyCodeForBatch
   OperationID: GetCurrencyCodeForBatch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCurrencyCodeForBatch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrencyCodeForBatch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCurrencyInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCurrencyInfo
   Description: This method is used when the Currency Code changes for Invoice payments only
   OperationID: GetCurrencyInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCurrencyInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrencyInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCurrencyInfoMaster(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCurrencyInfoMaster
   Description: This method is used when the Currency Code changes for Invoice payments only
   OperationID: GetCurrencyInfoMaster
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCurrencyInfoMaster_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrencyInfoMaster_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCustomerInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCustomerInfo
   Description: This method is called when the CustID field is modified
   OperationID: GetCustomerInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCustomerInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCustomerInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCustPIFlags(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCustPIFlags
   Description: This method gets the AutoGenPromNotes and DirectDebiting flags from the
Customer record. Also sets the flag hasBank to true if there are CustBank
records associated to the Customer and false if not.
   OperationID: GetCustPIFlags
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCustPIFlags_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCustPIFlags_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDtlInvoiceInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDtlInvoiceInfo
   Description: This method is called when the InvoiceNum field is modified
   OperationID: GetDtlInvoiceInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDtlInvoiceInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDtlInvoiceInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDtlLegalNumberInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDtlLegalNumberInfo
   Description: This method is called when the InvLegalNumber field is modified
   OperationID: GetDtlLegalNumberInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDtlLegalNumberInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDtlLegalNumberInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDtlTranAmtInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDtlTranAmtInfo
   Description: This method is run when the DocTranAmt field is modified
   OperationID: GetDtlTranAmtInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDtlTranAmtInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDtlTranAmtInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetExistingGenPI(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetExistingGenPI
   Description: This method is used to copy a generated ARPNHead
   OperationID: GetExistingGenPI
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetExistingGenPI_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetExistingGenPI_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetGLJrnDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetGLJrnDtl
   Description: Get the GLJrnDtl records for an ARPromissoryNote.
   OperationID: GetGLJrnDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetGLJrnDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGLJrnDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetGroupIDForPIWithHeadNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetGroupIDForPIWithHeadNum
   Description: This method will retrieve the GroupID for an ARPNHead record that's for the
ARPromNoteID supplied.
   OperationID: GetGroupIDForPIWithHeadNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetGroupIDForPIWithHeadNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGroupIDForPIWithHeadNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetGroupIDForPI(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetGroupIDForPI
   Description: This method will retrieve the GroupID for an ARPNHead record that's for the
ARPromNoteID supplied.
   OperationID: GetGroupIDForPI
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetGroupIDForPI_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGroupIDForPI_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetHdrInvoiceInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetHdrInvoiceInfo
   Description: This method will default customer information from an invoice.
   OperationID: GetHdrInvoiceInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetHdrInvoiceInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetHdrInvoiceInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetHdrLegalNumberInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetHdrLegalNumberInfo
   Description: This method will default customer information from an invoice.
   OperationID: GetHdrLegalNumberInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetHdrLegalNumberInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetHdrLegalNumberInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetHeadNumForPI(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetHeadNumForPI
   Description: This method will retrieve the HeadNum for an ARPNHead record that's for the
invoice number supplied.
   OperationID: GetHeadNumForPI
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetHeadNumForPI_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetHeadNumForPI_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetInvcsSinglGenPI(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetInvcsSinglGenPI
   Description: Retur list of open posted AR invoices for a specific Customer.
   OperationID: GetInvcsSinglGenPI
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInvcsSinglGenPI_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInvcsSinglGenPI_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLegalNumberInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetLegalNumberInfo
   Description: This method is called when the InvLegalNumber field is modified
   OperationID: GetLegalNumberInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLegalNumberInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLegalNumberInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewARPNHeadByGroupID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewARPNHeadByGroupID
   Description: GetNewARPNHeadByGroupID
   OperationID: GetNewARPNHeadByGroupID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewARPNHeadByGroupID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewARPNHeadByGroupID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewARPNHeadByInvoiceNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewARPNHeadByInvoiceNum
   Description: GetNewARPNHeadByInvoiceNum
   OperationID: GetNewARPNHeadByInvoiceNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewARPNHeadByInvoiceNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewARPNHeadByInvoiceNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewARPNHeadByInvoiceAndAccount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewARPNHeadByInvoiceAndAccount
   Description: GetNewARPNHeadByInvoiceNum
   OperationID: GetNewARPNHeadByInvoiceAndAccount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewARPNHeadByInvoiceAndAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewARPNHeadByInvoiceAndAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBankTranByHeadNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBankTranByHeadNum
   Description: GetNewBankTranByHeadNum
   OperationID: GetNewBankTranByHeadNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBankTranByHeadNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBankTranByHeadNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPITypePropByPMUID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPITypePropByPMUID
   OperationID: GetPITypePropByPMUID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPITypePropByPMUID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPITypePropByPMUID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPNotesByGroupID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPNotesByGroupID
   OperationID: GetPNotesByGroupID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPNotesByGroupID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPNotesByGroupID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPNotes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPNotes
   OperationID: GetPNotes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPNotes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPNotes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRateCodeInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRateCodeInfo
   Description: This method updates the dataset when the RateCode field changes
   OperationID: GetRateCodeInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRateCodeInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRateCodeInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsByGrpID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsByGrpID
   OperationID: GetRowsByGrpID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsByGrpID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsByGrpID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPNotesGenerated(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPNotesGenerated
   Description: Retrieves Payment Instruments which were created by Generation procedure.
   OperationID: GetPNotesGenerated
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPNotesGenerated_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPNotesGenerated_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsByGrpIDExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsByGrpIDExt
   Description: Retrieves list of Payment Instruments belong to gived Group
   OperationID: GetRowsByGrpIDExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsByGrpIDExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsByGrpIDExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSalesTaxInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSalesTaxInfo
   Description: This method updates the dataset when the TaxCode field changes
   OperationID: GetSalesTaxInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSalesTaxInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSalesTaxInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTaxableInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTaxableInfo
   Description: This method is called when the Taxable Amount Tax Percent or Fixed Amount is changed to
recalculate the Tax Total
   OperationID: GetTaxableInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTaxableInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTaxableInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTranAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTranAmt
   Description: This method upates the TranAmt/DocTranAmt field after the TranAmt, DocTranAmt or
ExchangeRate field is updated.  If BaseEntered flag is yes, the TranAmt and DocTranAmt
fields will be used to calculat the exchangeRate.  Otherwise, the TranAmt will be calculated
using the exchangeRate and DocTranAmt fields.
   OperationID: GetTranAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTranAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTranAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetUnapprovedPI(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetUnapprovedPI
   Description: This function will retrived existing Unapproved Stage PIs and pull them into the group to
be converted to Portfolio Stage PIs.
   OperationID: GetUnapprovedPI
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetUnapprovedPI_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetUnapprovedPI_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetUnapprovedPIwithCount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetUnapprovedPIwithCount
   Description: This function will retrived existing Unapproved Stage PIs and pull them into the group to
be converted to Portfolio Stage PIs.
   OperationID: GetUnapprovedPIwithCount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetUnapprovedPIwithCount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetUnapprovedPIwithCount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LeaveARPNHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LeaveARPNHead
   Description: This method checks calculates the GainLoss Adjustment record when finally
leaving a ARPNHead record after adding/updating all the ARPNDtl records
   OperationID: LeaveARPNHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveARPNHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveARPNHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MarkSent(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MarkSent
   Description: This method marks a Promissory Note as "Sent".
   OperationID: MarkSent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MarkSent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MarkSent_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MarkSigned(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MarkSigned
   Description: This method marks a Promissory Note as "Signed".
   OperationID: MarkSigned
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MarkSigned_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MarkSigned_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeBankFeeID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeBankFeeID
   Description: OnChangeBankFeeID
   OperationID: OnChangeBankFeeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeBankFeeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBankFeeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeBankAcctID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeBankAcctID
   Description: OnChangeBankAcctID
   OperationID: OnChangeBankAcctID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeBankAcctID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBankAcctID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeType
   Description: OnChangeType
   OperationID: OnChangeType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PostPIGroupWithoutGL(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PostPIGroupWithoutGL
   Description: PostPIGroupWithoutGL is to update ARPNMove records and delete CashGrp if all ARPNMove records were posted.
   OperationID: PostPIGroupWithoutGL
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PostPIGroupWithoutGL_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PostPIGroupWithoutGL_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PostPNWithoutGL(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PostPNWithoutGL
   OperationID: PostPNWithoutGL
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PostPNWithoutGL_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PostPNWithoutGL_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PrePostCheck(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PrePostCheck
   Description: PrePostCheck procedure checks if any related tax records have zero amounts.
   OperationID: PrePostCheck
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PrePostCheck_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrePostCheck_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RecalcBankTax(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RecalcBankTax
   Description: This method is called after the TaxAmt is changed to recalculate the doc or base tax amounts
   OperationID: RecalcBankTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RecalcBankTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RecalcBankTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetReadyToCalc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetReadyToCalc
   Description: CALCULATE VANTAGE\TAX CONNECT TAX CALCULATIONS UI NEEDS TO CALL A SAVE BEFORE CALLING THIS PROCEDURE
   OperationID: SetReadyToCalc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetReadyToCalc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetReadyToCalc_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SingleGenPIExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SingleGenPIExt
   Description: Generates Payment instruments for given invoises
   OperationID: SingleGenPIExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SingleGenPIExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SingleGenPIExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetEligibleInvcsForSinglGenPI(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetEligibleInvcsForSinglGenPI
   Description: Returns list of open posted AR invoices for a specific Customer which are eligible to PI generation
   OperationID: GetEligibleInvcsForSinglGenPI
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetEligibleInvcsForSinglGenPI_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEligibleInvcsForSinglGenPI_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SingleGenPI(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SingleGenPI
   OperationID: SingleGenPI
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SingleGenPI_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SingleGenPI_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateARPIType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateARPIType
   Description: ValidateARPIType
Used to validate whether PI type exists and is valid for AR Payment instrument.
   OperationID: ValidateARPIType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateARPIType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateARPIType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateDuplicatedARPromNoteID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateDuplicatedARPromNoteID
   Description: This Method validates wheter a promissory note id is duplicated.
0 = ok, 1= duplicate for other cust, 2=duplicate for current customer
   OperationID: ValidateDuplicatedARPromNoteID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateDuplicatedARPromNoteID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateDuplicatedARPromNoteID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_WriteXMLFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method WriteXMLFile
   Description: This method writes promissory note to file.
   OperationID: WriteXMLFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/WriteXMLFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/WriteXMLFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListCustom(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListCustom
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: GetListCustom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLegalNumGenOpts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetLegalNumGenOpts
   Description: Returns the legal number generation options.
   OperationID: GetLegalNumGenOpts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLegalNumGenOpts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLegalNumGenOpts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AssignLegalNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AssignLegalNumber
   Description: Assigns a legal number to the provided head number.
Validate header and legal number configuration exists, in other case throws an error.
   OperationID: AssignLegalNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AssignLegalNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssignLegalNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_VoidLegalNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method VoidLegalNumber
   Description: Voids the legal number.
   OperationID: VoidLegalNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VoidLegalNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidLegalNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreUpdate
   Description: This method will return a record in the LegalNumGenOpts data table if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewARPNHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewARPNHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewARPNHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewARPNHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewARPNHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewARPNHeadAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewARPNHeadAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewARPNHeadAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewARPNHeadAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewARPNHeadAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBankTran(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBankTran
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBankTran
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBankTran_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBankTran_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBankTranTaxDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBankTranTaxDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBankTranTaxDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBankTranTaxDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBankTranTaxDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBankTranTGLC(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBankTranTGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBankTranTGLC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBankTranTGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBankTranTGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewARPNDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewARPNDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewARPNDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewARPNDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewARPNDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTaxDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTaxDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTaxDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTaxDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaxDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewARPNHeadTGLC(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewARPNHeadTGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewARPNHeadTGLC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewARPNHeadTGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewARPNHeadTGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ARPNDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNHeadAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ARPNHeadAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNHeadListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ARPNHeadListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNHeadRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ARPNHeadRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNHeadTGLCRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ARPNHeadTGLCRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ARPNListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankTranRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_BankTranRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankTranTGLCRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_BankTranTGLCRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankTranTaxDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_BankTranTaxDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TaxDtlRow] = obj["value"]
      pass

class Erp_Tablesets_ARPNDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer Number  """  
      self.DiscountAmt:int = obj["DiscountAmt"]
      """  Discount Amount. Base Currency.  """  
      self.DocDiscountAmount:int = obj["DocDiscountAmount"]
      """  Discount Amount. Document Currency.  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """  Transaction Amount. Document Currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange Rate  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  Get Default Tax ID's flag.  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Posted to GL flag  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Reference to  invchead  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number  """  
      self.Posted:bool = obj["Posted"]
      """  Posted flag  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Rate Group code  """  
      self.RoundDiff:int = obj["RoundDiff"]
      """  Rounding Difference  """  
      self.Rpt1DiscountAmt:int = obj["Rpt1DiscountAmt"]
      """  Discount Amount. Report Currency 1.  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Transaction Amount. Report Currency 1.  """  
      self.Rpt2DiscountAmt:int = obj["Rpt2DiscountAmt"]
      """  Discount Amount. Report Currency 2.  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Transaction Amount. Report Currency 2.  """  
      self.Rpt3DiscountAmt:int = obj["Rpt3DiscountAmt"]
      """  Discount Amount. Report Currency 3.  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Transaction Amount. Report Currency 3.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Tax Liability  """  
      self.TranAmt:int = obj["TranAmt"]
      """  Transaction Amount  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction Date  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing transaction entry the user establishes a "Group ID". All transactions belong to a group. This current GroupID is assigned by the user.  Once created, it cannot be changed.  The Group ID is used to Selectively print and post the transactions.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  The foreign key that relates this detail record to a ARPNHead record. Duplicated from ARPNHead.HeadNum when record is created. Not applicable to user interface.  """  
      self.InvoiceRef:int = obj["InvoiceRef"]
      """  Applicable to CMemo transaction types only. The "Apply Credit Memo" program creates two CashDtl records for each invoice that a credit memo is applied to. One record for the <credit> to the invoice and a second record for the debit to the credit memo. In the first record this field is the InvoiceNum of the Credit memo. In the second record it is the InvoiceNum of the invoice that the credit memo was applied to.  """  
      self.DNAmount:int = obj["DNAmount"]
      """  The total debit note value applied for the invoice selected for the payment during the payment transaction.  """  
      self.DocDnAmount:int = obj["DocDnAmount"]
      """  The total debit note value applied for the invoice selected for the payment during the payment transaction.  """  
      self.Rpt1DnAmount:int = obj["Rpt1DnAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt2DnAmount:int = obj["Rpt2DnAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt3DnAmount:int = obj["Rpt3DnAmount"]
      """  Reporting currency value of this field  """  
      self.TranType:str = obj["TranType"]
      """   Identifies the type of transaction. Adjust = Adjustment, CMemo = Credit Memo Transfer, PrePay = Pre Payment, MisPay = Misc Payment, PayInv = Payment on Invoices. This is  duplicated from the CashHead.TranType, not user maintainable.
Note: For currency gain/loss it will be "Adjust". Both the Debit/Credit GL# will be used. Debit is A/R account. Credit is gain/loss account.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The unique identifier of the fiscal calendar.  """  
      self.DocSelfAssessAmt:int = obj["DocSelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Tax Amount in the vendors currency.  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period for the transaction. Not directly entered by the user. Duplicated from the CashBatc.FiscalPeriod at time of posting.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year. This is not entered by the user on each record. Instead as part of the posting process it is duplicated in from the CashBatc.FiscalYear. Therefore each batch is posted to a single fiscal period.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal Year Suffix.  """  
      self.Reference:str = obj["Reference"]
      """  Allows user to enter a short descriptive reference for the transaction. This is useful with Miscellaneous Cash Receipts.  """  
      self.Rpt1SelfAssessAmt:int = obj["Rpt1SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt2SelfAssessAmt:int = obj["Rpt2SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt3SelfAssessAmt:int = obj["Rpt3SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.SelfAssessAmt:int = obj["SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Total Tax Amount.  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.GainLossType:str = obj["GainLossType"]
      """  "R" for realized or "U" for unrealized Gain/Loss  """  
      self.ReverseGL:bool = obj["ReverseGL"]
      """  Indicates if it's a reversing Gain/Loss adjustment  """  
      self.RevalueDate:str = obj["RevalueDate"]
      """  Revaluation date that generated the gain/loss record  """  
      self.RevalueBal:int = obj["RevalueBal"]
      """  PI Balance at the time of revaluation  """  
      self.DocRevalueBal:int = obj["DocRevalueBal"]
      """  Document currency PI Balance at the time of revaluation  """  
      self.Rpt1RevalueBal:int = obj["Rpt1RevalueBal"]
      """  Reporting currency PI Balance at the time of revaluation  """  
      self.Rpt2RevalueBal:int = obj["Rpt2RevalueBal"]
      """  Reporting currency PI Balance at the time of revaluation  """  
      self.Rpt3RevalueBal:int = obj["Rpt3RevalueBal"]
      """  Reporting currency PI Balance at the time of revaluation  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type for the record.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      self.DocInvoiceAmt:int = obj["DocInvoiceAmt"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CurrencyDescription:str = obj["CurrencyDescription"]
      self.BaseCurrDesc:str = obj["BaseCurrDesc"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.DocInvoiceBal:int = obj["DocInvoiceBal"]
      self.InvTermsCode:str = obj["InvTermsCode"]
      self.InvDiscountDate:str = obj["InvDiscountDate"]
      self.InvDueDate:str = obj["InvDueDate"]
      self.DocNetCash:int = obj["DocNetCash"]
      self.DocNewBalance:int = obj["DocNewBalance"]
      self.InvLockRate:bool = obj["InvLockRate"]
      self.InvoiceBal:int = obj["InvoiceBal"]
      self.NewBalance:int = obj["NewBalance"]
      self.NetCash:int = obj["NetCash"]
      self.GainLossAmt:int = obj["GainLossAmt"]
      self.ApplyDate:str = obj["ApplyDate"]
      self.BillConNumber:int = obj["BillConNumber"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.DispGLAcct:str = obj["DispGLAcct"]
      self.DispTranAmt:int = obj["DispTranAmt"]
      self.DocDispTranAmt:int = obj["DocDispTranAmt"]
      self.DocSelfAssessTax:int = obj["DocSelfAssessTax"]
      self.DocWithholdTax:int = obj["DocWithholdTax"]
      self.FullyPaid:bool = obj["FullyPaid"]
      self.InvExchRate:int = obj["InvExchRate"]
      self.InvLegalNumber:str = obj["InvLegalNumber"]
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      self.InvXRateLabel:str = obj["InvXRateLabel"]
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.LegalNumStyle:str = obj["LegalNumStyle"]
      self.OldGainLoss:int = obj["OldGainLoss"]
      self.PostToGL:bool = obj["PostToGL"]
      self.SelfAssessTax:int = obj["SelfAssessTax"]
      self.SoldToCustID:str = obj["SoldToCustID"]
      self.SoldToCustNum:int = obj["SoldToCustNum"]
      self.SoldToCustomerName:str = obj["SoldToCustomerName"]
      self.WithholdTax:int = obj["WithholdTax"]
      self.XRateLabel:str = obj["XRateLabel"]
      self.Rpt1NewBalance:int = obj["Rpt1NewBalance"]
      self.Rpt3NewBalance:int = obj["Rpt3NewBalance"]
      self.Rpt1DispTranAmt:int = obj["Rpt1DispTranAmt"]
      self.Rpt2DispTranAmt:int = obj["Rpt2DispTranAmt"]
      self.Rpt3DispTranAmt:int = obj["Rpt3DispTranAmt"]
      self.Rpt1OldGainLoss:int = obj["Rpt1OldGainLoss"]
      self.Rpt2OldGainLoss:int = obj["Rpt2OldGainLoss"]
      self.Rpt3OldGainLoss:int = obj["Rpt3OldGainLoss"]
      self.Rpt1GainLossAmt:int = obj["Rpt1GainLossAmt"]
      self.Rpt2GainLossAmt:int = obj["Rpt2GainLossAmt"]
      self.Rpt3GainLossAmt:int = obj["Rpt3GainLossAmt"]
      self.Rpt1InvoiceAmt:int = obj["Rpt1InvoiceAmt"]
      self.Rpt2InvoiceAmt:int = obj["Rpt2InvoiceAmt"]
      self.Rpt3InvoiceAmt:int = obj["Rpt3InvoiceAmt"]
      self.Rpt1InvoiceBal:int = obj["Rpt1InvoiceBal"]
      self.Rpt2InvoiceBal:int = obj["Rpt2InvoiceBal"]
      self.Rpt3InvoiceBal:int = obj["Rpt3InvoiceBal"]
      self.Rpt2NewBalance:int = obj["Rpt2NewBalance"]
      self.Rpt1NetCash:int = obj["Rpt1NetCash"]
      self.Rpt2NetCash:int = obj["Rpt2NetCash"]
      self.Rpt3NetCash:int = obj["Rpt3NetCash"]
      self.InvoicePosted:bool = obj["InvoicePosted"]
      self.CurGroupID:str = obj["CurGroupID"]
      self.BitFlag:int = obj["BitFlag"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.InvoiceNumTermsCode:str = obj["InvoiceNumTermsCode"]
      self.InvoiceNumCardMemberName:str = obj["InvoiceNumCardMemberName"]
      self.TaxRgnDescription:str = obj["TaxRgnDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ARPNHeadAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.GroupID:str = obj["GroupID"]
      self.HeadNum:int = obj["HeadNum"]
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

class Erp_Tablesets_ARPNHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TranAmt:int = obj["TranAmt"]
      """  Transaction Amount  """  
      self.AppliedAmt:int = obj["AppliedAmt"]
      """  Applied Amount  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Bank Account ID  """  
      self.BankAmount:int = obj["BankAmount"]
      """  Bank Amount  """  
      self.BankSlip:str = obj["BankSlip"]
      """  Bank Slip Number of the promissory note.  """  
      self.BaseAmount:int = obj["BaseAmount"]
      """  Base Amount  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  When creating a new CashBdtl, the next available # is assigned by the system.  The system generates a number by finding the last CashBdtl of a cashbhed and uses its CashBookLine + 1. Not directly entered by the user.  """  
      self.CompBankAcctID:str = obj["CompBankAcctID"]
      """  Company Bank Account ID  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.CustBankAcctID:str = obj["CustBankAcctID"]
      """  Customer Bank Account ID  """  
      self.CustID:str = obj["CustID"]
      """  Customer ID  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer Number  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.DiscountAmt:int = obj["DiscountAmt"]
      """  Discount Amount. Base Currency.  """  
      self.DocAppliedAmt:int = obj["DocAppliedAmt"]
      """  Applied Amount. Document Currency.  """  
      self.DocUnAppliedAmt:int = obj["DocUnAppliedAmt"]
      """  Unapplied Amount. Document Currency.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Tax Amount. Document Currency.  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """  Transaction Amount. Document Currency.  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  Withholding Amount. Document Currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange Rate  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  Get Default Tax ID's flag.  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Posted to GL flag  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number  """  
      self.Paid:bool = obj["Paid"]
      """  Paid flag  """  
      self.Posted:bool = obj["Posted"]
      """  Posted flag  """  
      self.ProcessCard:str = obj["ProcessCard"]
      """  Process Card  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Rate Group code  """  
      self.RecalcBeforePost:bool = obj["RecalcBeforePost"]
      """  Recalculated before posting.  """  
      self.Rpt1AppliedAmt:int = obj["Rpt1AppliedAmt"]
      """  Applied Amount. Report Currency 1.  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Tax Amount. Report Currency 1.  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Transaction Amount. Report Currency 1.  """  
      self.Rpt1UnappliedAmt:int = obj["Rpt1UnappliedAmt"]
      """  Unapplied Amount. Report Currency 1.  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Withholding Amount. Report Currency 1.  """  
      self.Rpt2AppliedAmt:int = obj["Rpt2AppliedAmt"]
      """  Applied Amount. Report Currency 2.  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Tax Amount. Report Currency 2.  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Transaction Amount. Report Currency 2.  """  
      self.Rpt2UnappliedAmt:int = obj["Rpt2UnappliedAmt"]
      """  Unapplied Amount. Report Currency 2.  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Withholding Amount. Report Currency 2.  """  
      self.Rpt3AppliedAmt:int = obj["Rpt3AppliedAmt"]
      """  Applied Amount. Report Currency 3.  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Tax Amount. Report Currency 3.  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Transaction Amount. Report Currency 3.  """  
      self.Rpt3UnappliedAmt:int = obj["Rpt3UnappliedAmt"]
      """  Unapplied Amount. Report Currency 3.  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Withholding Amount. Report Currency 3.  """  
      self.Signed:bool = obj["Signed"]
      """  Signed flag  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Tax Amount. Base Currency.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Tax Liability  """  
      self.TotalARAmt:int = obj["TotalARAmt"]
      """  Total AR Amount  """  
      self.TransDate:str = obj["TransDate"]
      """  Transaction Date  """  
      self.UnappliedAmt:int = obj["UnappliedAmt"]
      """  Unapplied Amount. Base Currency.  """  
      self.Voided:bool = obj["Voided"]
      """  Voided Flag  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  Withholding Amount. Base Currency.  """  
      self.CompanyName:str = obj["CompanyName"]
      """  Company Name  """  
      self.CompanyAddr1:str = obj["CompanyAddr1"]
      """  First company address line.  """  
      self.CompanyAddr2:str = obj["CompanyAddr2"]
      """  Second company address line.  """  
      self.CompanyAddr3:str = obj["CompanyAddr3"]
      """  Third company address line.  """  
      self.CompanyCity:str = obj["CompanyCity"]
      """  Company City portion of the address.  """  
      self.CompanyState:str = obj["CompanyState"]
      """  Company State portion of the address.  """  
      self.CompanyPostalCode:str = obj["CompanyPostalCode"]
      """  Company Postal Code or Zip Code portion of the address.  """  
      self.CompanyCountry:str = obj["CompanyCountry"]
      """  Company Country portion of the address.  """  
      self.CustomerName:str = obj["CustomerName"]
      """  Company Name  """  
      self.CustomerAddr1:str = obj["CustomerAddr1"]
      """  First customer address line.  """  
      self.CustomerAddr2:str = obj["CustomerAddr2"]
      """  Second customer address line.  """  
      self.CustomerAddr3:str = obj["CustomerAddr3"]
      """  Third customer address line.  """  
      self.CustomerState:str = obj["CustomerState"]
      """  Customer Stateportion of the address.  """  
      self.CustomerPostalCode:str = obj["CustomerPostalCode"]
      """  Customer City portion of the address.  """  
      self.CustomerCity:str = obj["CustomerCity"]
      """  Customer Postal Code or Zip Code portion of the address.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing transaction entry the user establishes a "Group ID". All transactions belong to a group. This current GroupID is assigned by the user.  Once created, it cannot be changed.  The Group ID is used to Selectively print and post the transactions.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  An integer automatically assigned by the system using the database sequence called "CashHeadSeq". Which along with company and BatchID creates a unique key for the record. This is for internal control only the user never needs to reference.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Reference to  invchead  """  
      self.ARPromNoteID:str = obj["ARPromNoteID"]
      """  AR Payment Instrument ID  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year. This is not entered by the user on each record. Duplicated in from the CashGroup.FiscalYear. Therefore each batch is posted to a single fiscal period.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period for the transaction. Not directly entered by the user. Duplicated from the CashGroup.FiscalPeriod.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The unique identifier of the fiscal calendar.  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  """  
      self.TranType:str = obj["TranType"]
      """  Transaction Type  """  
      self.Sent:bool = obj["Sent"]
      """  Sent Flag  """  
      self.Type:str = obj["Type"]
      """  Type  """  
      self.IssueDate:str = obj["IssueDate"]
      """  Issue Date  """  
      self.DueDate:str = obj["DueDate"]
      """  Due date of the promissory note.  """  
      self.CompBankBranchCode:str = obj["CompBankBranchCode"]
      """  Bank/Branch Code for company's bank.  """  
      self.CompIBANCode:str = obj["CompIBANCode"]
      """  IBANCode for company's bank.  """  
      self.CustBankBranchCode:str = obj["CustBankBranchCode"]
      """  Bank/Branch Code for customer's bank.  """  
      self.CustIBANCode:str = obj["CustIBANCode"]
      """  IBAN Code for customer's bank.  """  
      self.AutoGenerated:bool = obj["AutoGenerated"]
      """  Indicates whether Payment Instrument was auto-generated from AR Invoice Entry.  """  
      self.DirectDeposit:bool = obj["DirectDeposit"]
      """  If true, indicates that Customer is flagged as Direct Deposit. Comes from field Customer.DirectDeposit.  """  
      self.ClearedAmt:int = obj["ClearedAmt"]
      """  Amount that the bank cleared the payment instrument for.  """  
      self.ClearedDate:str = obj["ClearedDate"]
      """  Date that the payment instrument was cleared in the system (System Set).  """  
      self.ClearedPending:bool = obj["ClearedPending"]
      """  Indicates that the payment instrument is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedPerson:str = obj["ClearedPerson"]
      """  Person who cleared the payment instrument (System Set).  """  
      self.ClearedPI:bool = obj["ClearedPI"]
      """  Indicates the Payment Instrument's cleared status.  When the Bank Statement is posted all Pending Transactions and Payment Instruments are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedStmtEndDate:str = obj["ClearedStmtEndDate"]
      """  End Date of the Statement that the payment instrument was cleared on.  """  
      self.ClearedTime:str = obj["ClearedTime"]
      """  Time that the payment instrument was cleared in the system - in HH:MM:SS format (System Set).  """  
      self.DocClearedAmt:int = obj["DocClearedAmt"]
      """  Amount that the bank cleared the check for.(Vendors Currency)  """  
      self.Rpt1ClearedAmt:int = obj["Rpt1ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2ClearedAmt:int = obj["Rpt2ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3ClearedAmt:int = obj["Rpt3ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  This field identifies a bankslip.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.DocumentPrinted:bool = obj["DocumentPrinted"]
      """  Indicates if the document has been printed.  """  
      self.CustCountryCode:int = obj["CustCountryCode"]
      """  Customer's country code  """  
      self.CustomerCountry:str = obj["CustomerCountry"]
      """  Customer country portion of the address.  """  
      self.PIStatus:str = obj["PIStatus"]
      """  Promissory Note Status  """  
      self.CurGroupID:str = obj["CurGroupID"]
      """  Current Group  """  
      self.PIStage:str = obj["PIStage"]
      """  Stage  """  
      self.ChgComment:str = obj["ChgComment"]
      """  Reason to change Company or Customer information  """  
      self.HoldReason:str = obj["HoldReason"]
      """  Hold from Application reason  """  
      self.LockRate:bool = obj["LockRate"]
      """  Lock Exchange Rate  """  
      self.ReferseRef:int = obj["ReferseRef"]
      """  Reference to reversed PI  """  
      self.ReverseDate:str = obj["ReverseDate"]
      """  Reverse Date  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BankClearedAmt:int = obj["BankClearedAmt"]
      """  BankClearedAmt  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.OnAccount:bool = obj["OnAccount"]
      """  OnAccount  """  
      self.DiscountCashDate:str = obj["DiscountCashDate"]
      """  DiscountCashDate  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.BaseCurrencyCode:str = obj["BaseCurrencyCode"]
      self.BaseCurrencyDesc:str = obj["BaseCurrencyDesc"]
      self.TermsDesc:str = obj["TermsDesc"]
      self.CurrencyDesc:str = obj["CurrencyDesc"]
      self.TotalCashReceived:int = obj["TotalCashReceived"]
      self.CompanyBankName:str = obj["CompanyBankName"]
      self.CompanyBankAcct:str = obj["CompanyBankAcct"]
      self.CompanyBankIdentifier:str = obj["CompanyBankIdentifier"]
      self.CustomerBankName:str = obj["CustomerBankName"]
      self.CustomerBankAcct:str = obj["CustomerBankAcct"]
      self.CustomerBankIdentifier:str = obj["CustomerBankIdentifier"]
      self.calcRate:bool = obj["calcRate"]
      """  Indicates if rate was calculates from TranAmt field instead of CurrExRate table  """  
      self.ApplyDate:str = obj["ApplyDate"]
      self.BankCurrencyCode:str = obj["BankCurrencyCode"]
      self.BankCurrSymbol:str = obj["BankCurrSymbol"]
      self.BillToName:str = obj["BillToName"]
      self.CreditHold:bool = obj["CreditHold"]
      """  Customer Credit Hold flag  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.DispGLAcct:str = obj["DispGLAcct"]
      """  Display GL Account  """  
      self.DocDiscount:int = obj["DocDiscount"]
      self.DocReceipt:int = obj["DocReceipt"]
      self.FullyPaid:bool = obj["FullyPaid"]
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.TotalRoundDiff:int = obj["TotalRoundDiff"]
      self.TranTaxAmt:int = obj["TranTaxAmt"]
      self.XRateLabel:str = obj["XRateLabel"]
      self.DocTranTaxAmt:int = obj["DocTranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.Rpt1TranTaxAmt:int = obj["Rpt1TranTaxAmt"]
      self.Rpt2TranTaxAmt:int = obj["Rpt2TranTaxAmt"]
      self.Rpt3TranTaxAmt:int = obj["Rpt3TranTaxAmt"]
      self.CompBankBranchCodeDesc:str = obj["CompBankBranchCodeDesc"]
      self.CustBankBranchCodeDesc:str = obj["CustBankBranchCodeDesc"]
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      """  Indicates if changes can occur after the document has been printed  """  
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      """  Indicates if assign legal number option is available.  """  
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      """  Indicates if the void legal number option is available  """  
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      """  Indicates if a legal number configuration exists for miscellaneous shipments  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      """  Indicates if TranDocTypeID is available for input.  """  
      self.PIStatusDesc:str = obj["PIStatusDesc"]
      self.PITypeInitiation:str = obj["PITypeInitiation"]
      """  like PIType.Initiation  """  
      self.DocGainLossReal:int = obj["DocGainLossReal"]
      self.DocGainLossUnreal:int = obj["DocGainLossUnreal"]
      self.GainLossReal:int = obj["GainLossReal"]
      self.GainLossUnreal:int = obj["GainLossUnreal"]
      self.Rpt1GainLossReal:int = obj["Rpt1GainLossReal"]
      self.Rpt1GainLossUnreal:int = obj["Rpt1GainLossUnreal"]
      self.Rpt2GainLossReal:int = obj["Rpt2GainLossReal"]
      self.Rpt2GainLossUnreal:int = obj["Rpt2GainLossUnreal"]
      self.Rpt3GainLossReal:int = obj["Rpt3GainLossReal"]
      self.Rpt3GainLossUnreal:int = obj["Rpt3GainLossUnreal"]
      self.RevalueDate:str = obj["RevalueDate"]
      self.DocDiscountAmt:int = obj["DocDiscountAmt"]
      self.Rpt1DiscountAmt:int = obj["Rpt1DiscountAmt"]
      self.Rpt2DiscountAmt:int = obj["Rpt2DiscountAmt"]
      self.Rpt3DiscountAmt:int = obj["Rpt3DiscountAmt"]
      self.Receipt:int = obj["Receipt"]
      self.Rpt1Receipt:int = obj["Rpt1Receipt"]
      self.Rpt2Receipt:int = obj["Rpt2Receipt"]
      self.Rpt3Receipt:int = obj["Rpt3Receipt"]
      self.BankAcctBankName:str = obj["BankAcctBankName"]
      """  The Bank's full name.  """  
      self.BankAcctDescription:str = obj["BankAcctDescription"]
      """  Full description of the bank account.  """  
      self.CashbookLineDescription:str = obj["CashbookLineDescription"]
      """  Description  """  
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CustNumName:str = obj["CustNumName"]
      """  The full name of the customer.  """  
      self.CustNumBTName:str = obj["CustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustNumCustID:str = obj["CustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.PIStatusStatusDesc:str = obj["PIStatusStatusDesc"]
      """  Status Description  """  
      self.PITypeDescription:str = obj["PITypeDescription"]
      """  Type Description  """  
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      """  Description  """  
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      """  Full description for the Tax Region.  """  
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      """  Description  """  
      self.BankRecGainLoss:int = obj["BankRecGainLoss"]
      self.DocBankRecGainLoss:int = obj["DocBankRecGainLoss"]
      self.Rpt1BankRecGainLoss:int = obj["Rpt1BankRecGainLoss"]
      self.Rpt2BankRecGainLoss:int = obj["Rpt2BankRecGainLoss"]
      self.Rpt3BankRecGainLoss:int = obj["Rpt3BankRecGainLoss"]
      self.BankTotalAmount:int = obj["BankTotalAmount"]
      self.StatusChgTranDocType:str = obj["StatusChgTranDocType"]
      self.StatusChgLegalNum:str = obj["StatusChgLegalNum"]
      self.ARPNDtlExists:bool = obj["ARPNDtlExists"]
      """  for kinetic purposes  """  
      self.ARPNDtlInvoicePosted:bool = obj["ARPNDtlInvoicePosted"]
      """  for kinetic purposes  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ARPNHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TranAmt:int = obj["TranAmt"]
      """  Transaction Amount  """  
      self.AppliedAmt:int = obj["AppliedAmt"]
      """  Applied Amount  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Bank Account ID  """  
      self.BankAmount:int = obj["BankAmount"]
      """  Bank Amount  """  
      self.BankSlip:str = obj["BankSlip"]
      """  Bank Slip Number of the promissory note.  """  
      self.BaseAmount:int = obj["BaseAmount"]
      """  Base Amount  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  When creating a new CashBdtl, the next available # is assigned by the system.  The system generates a number by finding the last CashBdtl of a cashbhed and uses its CashBookLine + 1. Not directly entered by the user.  """  
      self.CompBankAcctID:str = obj["CompBankAcctID"]
      """  Company Bank Account ID  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.CustBankAcctID:str = obj["CustBankAcctID"]
      """  Customer Bank Account ID  """  
      self.CustID:str = obj["CustID"]
      """  Customer ID  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer Number  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.DiscountAmt:int = obj["DiscountAmt"]
      """  Discount Amount. Base Currency.  """  
      self.DocAppliedAmt:int = obj["DocAppliedAmt"]
      """  Applied Amount. Document Currency.  """  
      self.DocUnAppliedAmt:int = obj["DocUnAppliedAmt"]
      """  Unapplied Amount. Document Currency.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Tax Amount. Document Currency.  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """  Transaction Amount. Document Currency.  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  Withholding Amount. Document Currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange Rate  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  Get Default Tax ID's flag.  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Posted to GL flag  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number  """  
      self.Paid:bool = obj["Paid"]
      """  Paid flag  """  
      self.Posted:bool = obj["Posted"]
      """  Posted flag  """  
      self.ProcessCard:str = obj["ProcessCard"]
      """  Process Card  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Rate Group code  """  
      self.RecalcBeforePost:bool = obj["RecalcBeforePost"]
      """  Recalculated before posting.  """  
      self.Rpt1AppliedAmt:int = obj["Rpt1AppliedAmt"]
      """  Applied Amount. Report Currency 1.  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Tax Amount. Report Currency 1.  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Transaction Amount. Report Currency 1.  """  
      self.Rpt1UnappliedAmt:int = obj["Rpt1UnappliedAmt"]
      """  Unapplied Amount. Report Currency 1.  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Withholding Amount. Report Currency 1.  """  
      self.Rpt2AppliedAmt:int = obj["Rpt2AppliedAmt"]
      """  Applied Amount. Report Currency 2.  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Tax Amount. Report Currency 2.  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Transaction Amount. Report Currency 2.  """  
      self.Rpt2UnappliedAmt:int = obj["Rpt2UnappliedAmt"]
      """  Unapplied Amount. Report Currency 2.  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Withholding Amount. Report Currency 2.  """  
      self.Rpt3AppliedAmt:int = obj["Rpt3AppliedAmt"]
      """  Applied Amount. Report Currency 3.  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Tax Amount. Report Currency 3.  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Transaction Amount. Report Currency 3.  """  
      self.Rpt3UnappliedAmt:int = obj["Rpt3UnappliedAmt"]
      """  Unapplied Amount. Report Currency 3.  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Withholding Amount. Report Currency 3.  """  
      self.Signed:bool = obj["Signed"]
      """  Signed flag  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Tax Amount. Base Currency.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Tax Liability  """  
      self.TotalARAmt:int = obj["TotalARAmt"]
      """  Total AR Amount  """  
      self.TransDate:str = obj["TransDate"]
      """  Transaction Date  """  
      self.UnappliedAmt:int = obj["UnappliedAmt"]
      """  Unapplied Amount. Base Currency.  """  
      self.Voided:bool = obj["Voided"]
      """  Voided Flag  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  Withholding Amount. Base Currency.  """  
      self.CompanyName:str = obj["CompanyName"]
      """  Company Name  """  
      self.CompanyAddr1:str = obj["CompanyAddr1"]
      """  First company address line.  """  
      self.CompanyAddr2:str = obj["CompanyAddr2"]
      """  Second company address line.  """  
      self.CompanyAddr3:str = obj["CompanyAddr3"]
      """  Third company address line.  """  
      self.CompanyCity:str = obj["CompanyCity"]
      """  Company City portion of the address.  """  
      self.CompanyState:str = obj["CompanyState"]
      """  Company State portion of the address.  """  
      self.CompanyPostalCode:str = obj["CompanyPostalCode"]
      """  Company Postal Code or Zip Code portion of the address.  """  
      self.CompanyCountry:str = obj["CompanyCountry"]
      """  Company Country portion of the address.  """  
      self.CustomerName:str = obj["CustomerName"]
      """  Company Name  """  
      self.CustomerAddr1:str = obj["CustomerAddr1"]
      """  First customer address line.  """  
      self.CustomerAddr2:str = obj["CustomerAddr2"]
      """  Second customer address line.  """  
      self.CustomerAddr3:str = obj["CustomerAddr3"]
      """  Third customer address line.  """  
      self.CustomerState:str = obj["CustomerState"]
      """  Customer Stateportion of the address.  """  
      self.CustomerPostalCode:str = obj["CustomerPostalCode"]
      """  Customer City portion of the address.  """  
      self.CustomerCity:str = obj["CustomerCity"]
      """  Customer Postal Code or Zip Code portion of the address.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing transaction entry the user establishes a "Group ID". All transactions belong to a group. This current GroupID is assigned by the user.  Once created, it cannot be changed.  The Group ID is used to Selectively print and post the transactions.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  An integer automatically assigned by the system using the database sequence called "CashHeadSeq". Which along with company and BatchID creates a unique key for the record. This is for internal control only the user never needs to reference.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Reference to  invchead  """  
      self.ARPromNoteID:str = obj["ARPromNoteID"]
      """  AR Payment Instrument ID  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year. This is not entered by the user on each record. Duplicated in from the CashGroup.FiscalYear. Therefore each batch is posted to a single fiscal period.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period for the transaction. Not directly entered by the user. Duplicated from the CashGroup.FiscalPeriod.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The unique identifier of the fiscal calendar.  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  """  
      self.TranType:str = obj["TranType"]
      """  Transaction Type  """  
      self.Sent:bool = obj["Sent"]
      """  Sent Flag  """  
      self.Type:str = obj["Type"]
      """  Type  """  
      self.IssueDate:str = obj["IssueDate"]
      """  Issue Date  """  
      self.DueDate:str = obj["DueDate"]
      """  Due date of the promissory note.  """  
      self.CompBankBranchCode:str = obj["CompBankBranchCode"]
      """  Bank/Branch Code for company's bank.  """  
      self.CompIBANCode:str = obj["CompIBANCode"]
      """  IBANCode for company's bank.  """  
      self.CustBankBranchCode:str = obj["CustBankBranchCode"]
      """  Bank/Branch Code for customer's bank.  """  
      self.CustIBANCode:str = obj["CustIBANCode"]
      """  IBAN Code for customer's bank.  """  
      self.AutoGenerated:bool = obj["AutoGenerated"]
      """  Indicates whether Payment Instrument was auto-generated from AR Invoice Entry.  """  
      self.DirectDeposit:bool = obj["DirectDeposit"]
      """  If true, indicates that Customer is flagged as Direct Deposit. Comes from field Customer.DirectDeposit.  """  
      self.ClearedAmt:int = obj["ClearedAmt"]
      """  Amount that the bank cleared the payment instrument for.  """  
      self.ClearedDate:str = obj["ClearedDate"]
      """  Date that the payment instrument was cleared in the system (System Set).  """  
      self.ClearedPending:bool = obj["ClearedPending"]
      """  Indicates that the payment instrument is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedPerson:str = obj["ClearedPerson"]
      """  Person who cleared the payment instrument (System Set).  """  
      self.ClearedPI:bool = obj["ClearedPI"]
      """  Indicates the Payment Instrument's cleared status.  When the Bank Statement is posted all Pending Transactions and Payment Instruments are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedStmtEndDate:str = obj["ClearedStmtEndDate"]
      """  End Date of the Statement that the payment instrument was cleared on.  """  
      self.ClearedTime:str = obj["ClearedTime"]
      """  Time that the payment instrument was cleared in the system - in HH:MM:SS format (System Set).  """  
      self.DocClearedAmt:int = obj["DocClearedAmt"]
      """  Amount that the bank cleared the check for.(Vendors Currency)  """  
      self.Rpt1ClearedAmt:int = obj["Rpt1ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2ClearedAmt:int = obj["Rpt2ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3ClearedAmt:int = obj["Rpt3ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  This field identifies a bankslip.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.DocumentPrinted:bool = obj["DocumentPrinted"]
      """  Indicates if the document has been printed.  """  
      self.CustCountryCode:int = obj["CustCountryCode"]
      """  Customer's country code  """  
      self.CustomerCountry:str = obj["CustomerCountry"]
      """  Customer country portion of the address.  """  
      self.PIStatus:str = obj["PIStatus"]
      """  Promissory Note Status  """  
      self.CurGroupID:str = obj["CurGroupID"]
      """  Current Group  """  
      self.PIStage:str = obj["PIStage"]
      """  Stage  """  
      self.ChgComment:str = obj["ChgComment"]
      """  Reason to change Company or Customer information  """  
      self.HoldReason:str = obj["HoldReason"]
      """  Hold from Application reason  """  
      self.LockRate:bool = obj["LockRate"]
      """  Lock Exchange Rate  """  
      self.ReferseRef:int = obj["ReferseRef"]
      """  Reference to reversed PI  """  
      self.ReverseDate:str = obj["ReverseDate"]
      """  Reverse Date  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BankClearedAmt:int = obj["BankClearedAmt"]
      """  BankClearedAmt  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.TotalBankFee:int = obj["TotalBankFee"]
      """  TotalBankFee  """  
      self.DocTotalBankFee:int = obj["DocTotalBankFee"]
      """  DocTotalBankFee  """  
      self.Rpt1TotalBankFee:int = obj["Rpt1TotalBankFee"]
      """  Rpt1TotalBankFee  """  
      self.Rpt2TotalBankFee:int = obj["Rpt2TotalBankFee"]
      """  Rpt2TotalBankFee  """  
      self.Rpt3TotalBankFee:int = obj["Rpt3TotalBankFee"]
      """  Rpt3TotalBankFee  """  
      self.OnAccount:bool = obj["OnAccount"]
      """  OnAccount  """  
      self.IssuerName:str = obj["IssuerName"]
      """  Issuer Name  """  
      self.SignedBy:str = obj["SignedBy"]
      """  Signed By  """  
      self.SignedDate:str = obj["SignedDate"]
      """  Signed Date  """  
      self.SigneeAddr1:str = obj["SigneeAddr1"]
      """  Signee Address 1  """  
      self.SigneeAddr2:str = obj["SigneeAddr2"]
      """  Signee Address 2  """  
      self.SigneeAddr3:str = obj["SigneeAddr3"]
      """  Signee Address 3  """  
      self.SigneeCity:str = obj["SigneeCity"]
      """  Signee City  """  
      self.SigneeState:str = obj["SigneeState"]
      """  Signee State  """  
      self.SigneeZip:str = obj["SigneeZip"]
      """  Signee Postal Code  """  
      self.SigneeCountryNum:int = obj["SigneeCountryNum"]
      """  Signee Country Number  """  
      self.SigneePhoneNum:str = obj["SigneePhoneNum"]
      """  Signee Phone  """  
      self.SigneeEMailAddress:str = obj["SigneeEMailAddress"]
      """  Signee Email Address  """  
      self.SigneeComment:str = obj["SigneeComment"]
      """  Signee Comment  """  
      self.DiscountChargeAmt:int = obj["DiscountChargeAmt"]
      """  DiscountChargeAmt  """  
      self.DocDiscountChargeAmt:int = obj["DocDiscountChargeAmt"]
      """  DocDiscountChargeAmt  """  
      self.Rpt1DiscountChargeAmt:int = obj["Rpt1DiscountChargeAmt"]
      """  Rpt1DiscountChargeAmt  """  
      self.Rpt2DiscountChargeAmt:int = obj["Rpt2DiscountChargeAmt"]
      """  Rpt2DiscountChargeAmt  """  
      self.Rpt3DiscountChargeAmt:int = obj["Rpt3DiscountChargeAmt"]
      """  Rpt3DiscountChargeAmt  """  
      self.SigneeBankName:str = obj["SigneeBankName"]
      """  Signee Bank Name  """  
      self.SigneeBankAcct:str = obj["SigneeBankAcct"]
      """  Signee Bank Account Number  """  
      self.SigneeBankIdentifier:str = obj["SigneeBankIdentifier"]
      """  Signee Bank Identifier  """  
      self.SigneeIBANCode:str = obj["SigneeIBANCode"]
      """  Signee IBAN Code  """  
      self.SigneeBankBranchCode:str = obj["SigneeBankBranchCode"]
      """  Signee Bank BranchCode  """  
      self.DiscountCashDate:str = obj["DiscountCashDate"]
      """  DiscountCashDate  """  
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      """  Indicates if changes can occur after the document has been printed  """  
      self.ApplyDate:str = obj["ApplyDate"]
      self.BankCurrencyCode:str = obj["BankCurrencyCode"]
      self.BankCurrSymbol:str = obj["BankCurrSymbol"]
      self.BankRecGainLoss:int = obj["BankRecGainLoss"]
      self.calcRate:bool = obj["calcRate"]
      """  Indicates if rate was calculates from TranAmt field instead of CurrExRate table  """  
      self.CompanyBankAcct:str = obj["CompanyBankAcct"]
      self.CompanyBankIdentifier:str = obj["CompanyBankIdentifier"]
      self.CompanyBankName:str = obj["CompanyBankName"]
      self.CompBankBranchCodeDesc:str = obj["CompBankBranchCodeDesc"]
      self.CreditHold:bool = obj["CreditHold"]
      """  Customer Credit Hold flag  """  
      self.CurrencyDesc:str = obj["CurrencyDesc"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CustBankBranchCodeDesc:str = obj["CustBankBranchCodeDesc"]
      self.CustomerBankAcct:str = obj["CustomerBankAcct"]
      self.CustomerBankIdentifier:str = obj["CustomerBankIdentifier"]
      self.CustomerBankName:str = obj["CustomerBankName"]
      self.DisableBankAcctIDPI:bool = obj["DisableBankAcctIDPI"]
      self.DisableBankAmt:bool = obj["DisableBankAmt"]
      """   The flag to indicate if BankClearedAmt is not available to make changes.
(If Bank currency equals transaction currency this flag is true)  """  
      self.DispGLAcct:str = obj["DispGLAcct"]
      """  Display GL Account  """  
      self.DocBankRecGainLoss:int = obj["DocBankRecGainLoss"]
      self.DocDiscount:int = obj["DocDiscount"]
      self.DocDiscountAmt:int = obj["DocDiscountAmt"]
      self.DocGainLossReal:int = obj["DocGainLossReal"]
      self.DocGainLossUnreal:int = obj["DocGainLossUnreal"]
      self.DocReceipt:int = obj["DocReceipt"]
      self.DocTranTaxAmt:int = obj["DocTranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      """  Indicates if assign legal number option is available.  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      """  Indicates if TranDocTypeID is available for input.  """  
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      """  Indicates if the void legal number option is available  """  
      self.FullyPaid:bool = obj["FullyPaid"]
      self.GainLossReal:int = obj["GainLossReal"]
      self.GainLossUnreal:int = obj["GainLossUnreal"]
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      """  Indicates if a legal number configuration exists for miscellaneous shipments  """  
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.PIStatusDesc:str = obj["PIStatusDesc"]
      self.PITypeInitiation:str = obj["PITypeInitiation"]
      """  like PIType.Initiation  """  
      self.Receipt:int = obj["Receipt"]
      self.RevalueDate:str = obj["RevalueDate"]
      self.Rpt1BankRecGainLoss:int = obj["Rpt1BankRecGainLoss"]
      self.Rpt1DiscountAmt:int = obj["Rpt1DiscountAmt"]
      self.Rpt1GainLossReal:int = obj["Rpt1GainLossReal"]
      self.Rpt1GainLossUnreal:int = obj["Rpt1GainLossUnreal"]
      self.Rpt1Receipt:int = obj["Rpt1Receipt"]
      self.Rpt1TranTaxAmt:int = obj["Rpt1TranTaxAmt"]
      self.Rpt2BankRecGainLoss:int = obj["Rpt2BankRecGainLoss"]
      self.Rpt2DiscountAmt:int = obj["Rpt2DiscountAmt"]
      self.Rpt2GainLossReal:int = obj["Rpt2GainLossReal"]
      self.Rpt2GainLossUnreal:int = obj["Rpt2GainLossUnreal"]
      self.Rpt2Receipt:int = obj["Rpt2Receipt"]
      self.Rpt2TranTaxAmt:int = obj["Rpt2TranTaxAmt"]
      self.Rpt3BankRecGainLoss:int = obj["Rpt3BankRecGainLoss"]
      self.Rpt3DiscountAmt:int = obj["Rpt3DiscountAmt"]
      self.Rpt3GainLossReal:int = obj["Rpt3GainLossReal"]
      self.Rpt3GainLossUnreal:int = obj["Rpt3GainLossUnreal"]
      self.Rpt3Receipt:int = obj["Rpt3Receipt"]
      self.Rpt3TranTaxAmt:int = obj["Rpt3TranTaxAmt"]
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.StatusChgLegalNum:str = obj["StatusChgLegalNum"]
      self.StatusChgTranDocType:str = obj["StatusChgTranDocType"]
      self.TermsDesc:str = obj["TermsDesc"]
      self.TotalCashReceived:int = obj["TotalCashReceived"]
      self.TotalRoundDiff:int = obj["TotalRoundDiff"]
      self.TranTaxAmt:int = obj["TranTaxAmt"]
      self.TypeDesc:str = obj["TypeDesc"]
      self.XRateLabel:str = obj["XRateLabel"]
      self.BankTotalAmount:int = obj["BankTotalAmount"]
      self.BaseCurrencyCode:str = obj["BaseCurrencyCode"]
      self.BaseCurrencyDesc:str = obj["BaseCurrencyDesc"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.BillToName:str = obj["BillToName"]
      self.DocDiscountedAmt:int = obj["DocDiscountedAmt"]
      self.ARPNDtlExists:bool = obj["ARPNDtlExists"]
      """  for kinetic purposes  """  
      self.ARPNDtlInvoicePosted:bool = obj["ARPNDtlInvoicePosted"]
      """  for kinetic purposes  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctDescription:str = obj["BankAcctDescription"]
      self.BankAcctBankName:str = obj["BankAcctBankName"]
      self.CashbookLineDescription:str = obj["CashbookLineDescription"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CustNumInactive:bool = obj["CustNumInactive"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.PIStatusStatusDesc:str = obj["PIStatusStatusDesc"]
      self.PITypeDescription:str = obj["PITypeDescription"]
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ARPNHeadTGLCRow:
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
      self.HeadNum:int = obj["HeadNum"]
      """  HeadNum of ARPNHead  """  
      self.GroupID:str = obj["GroupID"]
      """  GroupID of ARPNHead  """  
      self.BitFlag:int = obj["BitFlag"]
      self.COADescription:str = obj["COADescription"]
      self.GLAccountGLAcctDisp:str = obj["GLAccountGLAcctDisp"]
      self.GLAccountAccountDesc:str = obj["GLAccountAccountDesc"]
      self.GLAccountGLShortAcct:str = obj["GLAccountGLShortAcct"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ARPNListRow:
   def __init__(self, obj):
      self.ARPromNoteID:str = obj["ARPromNoteID"]
      self.Company:str = obj["Company"]
      self.CurGroupID:str = obj["CurGroupID"]
      self.CustID:str = obj["CustID"]
      self.GroupID:str = obj["GroupID"]
      self.HeadNum:int = obj["HeadNum"]
      self.PIStage:str = obj["PIStage"]
      self.PIStatus:str = obj["PIStatus"]
      self.TranAmt:int = obj["TranAmt"]
      self.Type:str = obj["Type"]
      self.Selected:bool = obj["Selected"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BankTranRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Relates record to a BankAcct.  """  
      self.TranNum:int = obj["TranNum"]
      """  Unique ID of the Transaction.  """  
      self.TranDate:str = obj["TranDate"]
      """  Date that the transaction took place.  """  
      self.TranAmt:int = obj["TranAmt"]
      """  Amount of the Transaction  """  
      self.TranRef:str = obj["TranRef"]
      """  Transaction Reference  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Indicates that the Transaction (not cleared variance) has been posted to G/L.  When the Bank Statement is posted all Non-G/L Posted adjustments for the bank are posted to G/L using the Bank Account's Cash and Bank Fee Accounts. G/L Posted Transactions cannot be deleted. (System Set)  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  Person who entered the transaction (System Set).  """  
      self.EntryDate:str = obj["EntryDate"]
      """  Date that the Transaction was entered into the system (System Set).  """  
      self.EntryTime:str = obj["EntryTime"]
      """  Time that the transaction was entered into the system - in HH:MM:SS format (System Set).  """  
      self.TranCleared:bool = obj["TranCleared"]
      """  Indicates the transaction's cleared status.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.TranClearPending:bool = obj["TranClearPending"]
      """  Indicates that the transaction is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.TranClearedAmt:int = obj["TranClearedAmt"]
      """  Amount that the Transaction was cleared for.  """  
      self.TranClearedPerson:str = obj["TranClearedPerson"]
      """  Person who cleared the transaction (System Set).  """  
      self.TranClearedDate:str = obj["TranClearedDate"]
      """  Date that the Transaction was cleared in the system (System Set).  """  
      self.TranClearedTime:str = obj["TranClearedTime"]
      """  Time that the transaction was cleared in the system - in HH:MM:SS format (System Set).  """  
      self.BankSlip:str = obj["BankSlip"]
      """  The identifier of the Bank Slip document (bank statement) on which this transaction was cleared by the bank. This is updated via the bank reconciliation process.  This is also written to the related GLJrnDtl records.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal year that entry applies to.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period the transaction was posted to. Only pertains to when posted to GL.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  Journal Number of related GLJrnDtl.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Journal Code of the related GLJrnDtl.  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """  Document amount of the Transaction  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange rate that is used for this bank transaction.  """  
      self.DocTranClearedAmt:int = obj["DocTranClearedAmt"]
      """  Document amount that the Transaction was cleared for.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry "group" that the transaction is assigned to.  All transactions belong to a "Group."  It is assigned to the record during creation using the "current group" that the user is signed into.  It cannot be changed.  The GroupID is used to selectively print and post the transactions.  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  This field identifies a bankslip.  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  This field identifies a line of a bankslip.  """  
      self.GLRefType:str = obj["GLRefType"]
      """  Link to the related GLRefTyp.RefType.  """  
      self.GLRefCode:str = obj["GLRefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.GLRefCodeDesc:str = obj["GLRefCodeDesc"]
      """  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TranClearedAmt:int = obj["Rpt1TranClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TranClearedAmt:int = obj["Rpt2TranClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TranClearedAmt:int = obj["Rpt3TranClearedAmt"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix that entry applies to.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.BankFeeID:str = obj["BankFeeID"]
      """  Unique ID of the Fee  """  
      self.BankFeeAmt:int = obj["BankFeeAmt"]
      """  The Fee amount; this amount plus the Fee tax amount will compose the total of the charge on the statement  """  
      self.BankFeeTaxAmt:int = obj["BankFeeTaxAmt"]
      """  The Tax Amount that has been charged to the fee  """  
      self.DocBankFeeAmt:int = obj["DocBankFeeAmt"]
      """  The Fee amount in Base Currency  """  
      self.DocBankFeeTaxAmt:int = obj["DocBankFeeTaxAmt"]
      """  The Tax Amount that has been charged to the fee in Base Currency  """  
      self.Rpt1BankFeeAmt:int = obj["Rpt1BankFeeAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2BankFeeAmt:int = obj["Rpt2BankFeeAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3BankFeeAmt:int = obj["Rpt3BankFeeAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1BankFeeTaxAmt:int = obj["Rpt1BankFeeTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2BankFeeTaxAmt:int = obj["Rpt2BankFeeTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3BankFeeTaxAmt:int = obj["Rpt3BankFeeTaxAmt"]
      """  Reporting currency value of this field  """  
      self.SourceModule:str = obj["SourceModule"]
      """   Used for Bank Fee Functionality, indicates the module that created this BankFee.  This is assigned by the system.
Values can be; AR, AP and BA.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  Consecutive from the AP and AR transactions, this field is used to identify the AP or AR transaction that created this Bank Fee  """  
      self.Voided:bool = obj["Voided"]
      """  Indiates if the BankTran has been voided.  The TranNum field will be the same as the original transaction  """  
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
      """  Bank Balance at the time of revaluation  """  
      self.DocRevalueBal:int = obj["DocRevalueBal"]
      """  Document currency Bank Balance at the time of revaluation  """  
      self.Rpt1RevalueBal:int = obj["Rpt1RevalueBal"]
      """  Reporting currency Bank Balance at the time of revaluation  """  
      self.Rpt2RevalueBal:int = obj["Rpt2RevalueBal"]
      """  Reporting currency Bank Balance at the time of revaluation  """  
      self.Rpt3RevalueBal:int = obj["Rpt3RevalueBal"]
      """  Reporting currency Bank Balance at the time of revaluation  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number for the record.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document for the record.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CNCFICode:str = obj["CNCFICode"]
      """  CNCFICode  """  
      self.CNToCFICode:str = obj["CNToCFICode"]
      """  CNToCFICode  """  
      self.BankRecGainLoss:int = obj["BankRecGainLoss"]
      """  BankRecGainLoss  """  
      self.Rpt1BankRecGainLoss:int = obj["Rpt1BankRecGainLoss"]
      """  Rpt1BankRecGainLoss  """  
      self.Rpt2BankRecGainLoss:int = obj["Rpt2BankRecGainLoss"]
      """  Rpt2BankRecGainLoss  """  
      self.Rpt3BankRecGainLoss:int = obj["Rpt3BankRecGainLoss"]
      """  Rpt3BankRecGainLoss  """  
      self.BalanceUpdated:int = obj["BalanceUpdated"]
      """  BalanceUpdated  """  
      self.DocBankRecGainLoss:int = obj["DocBankRecGainLoss"]
      """  DocBankRecGainLoss  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.BankBatchExcluded:bool = obj["BankBatchExcluded"]
      """  Indicates that transaction is currently excluded from batch in Bank Statement Processing.  """  
      self.BankBatchSysRowID:str = obj["BankBatchSysRowID"]
      """  BankBatchSysRowID  """  
      self.ABTUID:str = obj["ABTUID"]
      """  ABTUID  """  
      self.Plant:str = obj["Plant"]
      """  Multi-Site related Site  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for BASE  """  
      self.CNCFICodeDescription:str = obj["CNCFICodeDescription"]
      self.CRCurrCode:str = obj["CRCurrCode"]
      """  Cash Receipt currency code  """  
      self.CRRateGrpCode:str = obj["CRRateGrpCode"]
      """  Cash Receipt Rate group code  """  
      self.CRTranAmt:int = obj["CRTranAmt"]
      """  Cash Receipt Tran amount  """  
      self.CRTranClearedAmt:int = obj["CRTranClearedAmt"]
      """  Cash Receipt Transaction Cleared Amount  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      """  Currency Switch  """  
      self.DisableBankAmt:bool = obj["DisableBankAmt"]
      """   The flag to indicate if BankClearedAmt is not available to make changes.
(If Bank currency equals transaction currency this flag is true)  """  
      self.DispAmtReverse:bool = obj["DispAmtReverse"]
      """  The flag to indicate if the Display amount is supposed to be reversed  """  
      self.DispDocTranAmt:int = obj["DispDocTranAmt"]
      self.DispDocTranClearedAmt:int = obj["DispDocTranClearedAmt"]
      self.DispTranAmt:int = obj["DispTranAmt"]
      self.DispTranClearedAmt:int = obj["DispTranClearedAmt"]
      self.InternalDate:str = obj["InternalDate"]
      """  Used for tree structure/parent view definition in Petty Cash Entry  """  
      self.IsFiltered:bool = obj["IsFiltered"]
      self.IsLockedBankRec:bool = obj["IsLockedBankRec"]
      """  Indicates if the record is locked by review journal for bank reconciliation  """  
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.LegalNumStyle:str = obj["LegalNumStyle"]
      """  Indicates if the legal number is manually generated or system generated  """  
      self.RefCodeStatus:str = obj["RefCodeStatus"]
      """  Indicates if Reference Code is (M)andatory, (O)ptional, (E)xcluded or Blank.  Enable Reference Code if "M" or "O".  """  
      self.Rpt1DispTranAmt:int = obj["Rpt1DispTranAmt"]
      self.Rpt1DispTranClearedAmt:int = obj["Rpt1DispTranClearedAmt"]
      self.Rpt2DispTranAmt:int = obj["Rpt2DispTranAmt"]
      self.Rpt2DispTranClearedAmt:int = obj["Rpt2DispTranClearedAmt"]
      self.Rpt3DispTranAmt:int = obj["Rpt3DispTranAmt"]
      self.Rpt3DispTranClearedAmt:int = obj["Rpt3DispTranClearedAmt"]
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      self.GLAccount:str = obj["GLAccount"]
      """  Display GL Account  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      self.BankFeeIDDescription:str = obj["BankFeeIDDescription"]
      self.BankFeeIDTaxCode:str = obj["BankFeeIDTaxCode"]
      self.CashbookLineDescription:str = obj["CashbookLineDescription"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BankTranTGLCRow:
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
      """  GroupID for relation to BankTran  """  
      self.HeadNum:int = obj["HeadNum"]
      self.InternalDate:str = obj["InternalDate"]
      """  Used for tree structure/parent view definition in Petty Cash Entry  """  
      self.PCashDeskID:str = obj["PCashDeskID"]
      self.PCashRefNum:int = obj["PCashRefNum"]
      self.Voided:bool = obj["Voided"]
      """  Voided flag for relation to BankTran  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID for relation to BankTran  """  
      self.BitFlag:int = obj["BitFlag"]
      self.COADescription:str = obj["COADescription"]
      self.GLAccountGLShortAcct:str = obj["GLAccountGLShortAcct"]
      self.GLAccountGLAcctDisp:str = obj["GLAccountGLAcctDisp"]
      self.GLAccountAccountDesc:str = obj["GLAccountAccountDesc"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BankTranTaxDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SourceModule:str = obj["SourceModule"]
      """   Indicates the module that created this tax detail.  This is assigned by the system.
Values can be; AR, AP.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  HeadNum  """  
      self.APTranNo:int = obj["APTranNo"]
      """  Integer assigned by the system copied from APTran.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  Taxable amount for this invoice. Manually entered if the currency is the base currency.  """  
      self.DocTaxableAmt:int = obj["DocTaxableAmt"]
      """  Taxable amount for this invoice in foreign currency. Manually entered.  """  
      self.Percent:int = obj["Percent"]
      """  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount. Manually entered if the currency is the base currency.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount in foreign currency. Manually entered.  """  
      self.ReverseCharge:bool = obj["ReverseCharge"]
      """  Reverse Charge.  """  
      self.Rpt1TaxableAmt:int = obj["Rpt1TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxableAmt:int = obj["Rpt2TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxableAmt:int = obj["Rpt3TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.RateCode:str = obj["RateCode"]
      """  Rate Code  """  
      self.CollectionType:int = obj["CollectionType"]
      """  Collection Type  """  
      self.Timing:int = obj["Timing"]
      """  Timing of when to report taxes  """  
      self.ExemptType:int = obj["ExemptType"]
      """  Exemption Type  """  
      self.ExemptPercent:int = obj["ExemptPercent"]
      """  Exemption Percent  """  
      self.ResolutionNum:str = obj["ResolutionNum"]
      """  Resolution Number  """  
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
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  The open A/R invoice # that the transaction applies against. Not used by the MisPay trantype. In the case of PayInv, or CMemo transaction this must be a valid InvcHead record where InvcHead.CreditMemo = No. In case of "Adjust" transactions this can be either a invoice or a credit memo reference. Note: The "Apply Credit Memo" program automatically creates an additional CashDtl records for each invoice to which the credit memo is applied.  In this additional record this field contains the credit memo's number.  """  
      self.InvoiceRef:int = obj["InvoiceRef"]
      """  Applicable to CMemo transaction types only. The "Apply Credit Memo" program creates two CashDtl records for each invoice that a credit memo is applied to. One record for the <credit> to the invoice and a second record for the debit to the credit memo. In the first record this field is the InvoiceNum of the Credit memo. In the second record it is the InvoiceNum of the invoice that the credit memo was applied to.  """  
      self.ECAcquisitionSeq:int = obj["ECAcquisitionSeq"]
      """   Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.
NOTE:  This field is now used in VAT Reverse Charge logic.  If an invoice line is marked for Reverse Charge, a second line is created just like in the ECAcquisition logic. To distinguish the two scenarios, the ReverseCharge flag will be set to true if the second line is for Reverse Charge.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Relates record to a BankAcct.  """  
      self.TranNum:int = obj["TranNum"]
      """  Unique ID of the Transaction.  """  
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
      self.Manual:bool = obj["Manual"]
      """  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  """  
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
      self.DiscTaxAdj:int = obj["DiscTaxAdj"]
      """  Discount Tax Adjustment  """  
      self.DocDiscTaxAdj:int = obj["DocDiscTaxAdj"]
      """  Discount Tax Adjustment in foreign currency.  """  
      self.Rpt1DiscTaxAdj:int = obj["Rpt1DiscTaxAdj"]
      """  Reporting currency value of this field  """  
      self.Rpt2DiscTaxAdj:int = obj["Rpt2DiscTaxAdj"]
      """  Reporting currency value of this field  """  
      self.Rpt3DiscTaxAdj:int = obj["Rpt3DiscTaxAdj"]
      """  Reporting currency value of this field  """  
      self.DiscTaxableAdj:int = obj["DiscTaxableAdj"]
      """  Discount Taxable Adjustment  """  
      self.DocDiscTaxableAdj:int = obj["DocDiscTaxableAdj"]
      """  Discount Taxable Adjustment in foreign currency.  """  
      self.Rpt1DiscTaxableAdj:int = obj["Rpt1DiscTaxableAdj"]
      """  Reporting currency value of this field  """  
      self.Rpt2DiscTaxableAdj:int = obj["Rpt2DiscTaxableAdj"]
      """  Reporting currency value of this field  """  
      self.Rpt3DiscTaxableAdj:int = obj["Rpt3DiscTaxableAdj"]
      """  Reporting currency value of this field  """  
      self.TextCode:str = obj["TextCode"]
      """  Unique Identifier for Legal Text  """  
      self.Voided:bool = obj["Voided"]
      """  Indicates if transaction was voided.  The rest of the unique key will contain the original transaction values (like APTran)  """  
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
      self.DiscTaxAdjVar:int = obj["DiscTaxAdjVar"]
      """  Discount Tax Adjustment Variance  """  
      self.DocDiscTaxAdjVar:int = obj["DocDiscTaxAdjVar"]
      """  Discount Tax Adjustment Variance  """  
      self.Rpt1DiscTaxAdjVar:int = obj["Rpt1DiscTaxAdjVar"]
      """  Reporting currency value of this field  """  
      self.Rpt2DiscTaxAdjVar:int = obj["Rpt2DiscTaxAdjVar"]
      """  Reporting currency value of this field  """  
      self.Rpt3DiscTaxAdjVar:int = obj["Rpt3DiscTaxAdjVar"]
      """  Reporting currency value of this field  """  
      self.PCashDeskID:str = obj["PCashDeskID"]
      """  Unique identifier of Petty Cash Desk  """  
      self.PCashRefNum:int = obj["PCashRefNum"]
      """  Reference Number, unique identifier of Petty Cash Document  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AGOrigTaxableAmt:int = obj["AGOrigTaxableAmt"]
      """  AGOrigTaxableAmt  """  
      self.GainLoss:int = obj["GainLoss"]
      """  GainLoss  """  
      self.DocGainLoss:int = obj["DocGainLoss"]
      """  DocGainLoss  """  
      self.Rpt1GainLoss:int = obj["Rpt1GainLoss"]
      """  Rpt1GainLoss  """  
      self.Rpt2GainLoss:int = obj["Rpt2GainLoss"]
      """  Rpt2GainLoss  """  
      self.Rpt3GainLoss:int = obj["Rpt3GainLoss"]
      """  Rpt3GainLoss  """  
      self.CNCFICode:str = obj["CNCFICode"]
      """  CNCFICode  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  APInvoiceNum  """  
      self.TranType:str = obj["TranType"]
      """  TranType  """  
      self.MovementNum:int = obj["MovementNum"]
      """  MovementNum  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.CNCFICodeDescription:str = obj["CNCFICodeDescription"]
      self.CTDescription:str = obj["CTDescription"]
      self.DisableManual:bool = obj["DisableManual"]
      """  Flag to indicate if Manual checkbox should be disabled  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry "group" that the transaction is assigned to.  All transactions belong to a "Group."  It is assigned to the record during creation using the "current group" that the user is signed into.  It cannot be changed.  The GroupID is used to selectively print and post the transactions.  """  
      self.InternalDate:str = obj["InternalDate"]
      """  Used for tree structure/parent view definition in Petty Cash Entry  """  
      self.IsFiltered:bool = obj["IsFiltered"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.BitFlag:int = obj["BitFlag"]
      self.RateCodeDescription:str = obj["RateCodeDescription"]
      self.TaxCodeDescription:str = obj["TaxCodeDescription"]
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

class Erp_Tablesets_TaxDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SourceModule:str = obj["SourceModule"]
      """   Indicates the module that created this tax detail.  This is assigned by the system.
Values can be; AR, AP.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  HeadNum  """  
      self.APTranNo:int = obj["APTranNo"]
      """  Integer assigned by the system copied from APTran.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  Taxable amount for this invoice. Manually entered if the currency is the base currency.  """  
      self.DocTaxableAmt:int = obj["DocTaxableAmt"]
      """  Taxable amount for this invoice in foreign currency. Manually entered.  """  
      self.Percent:int = obj["Percent"]
      """  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount. Manually entered if the currency is the base currency.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount in foreign currency. Manually entered.  """  
      self.ReverseCharge:bool = obj["ReverseCharge"]
      """  Reverse Charge.  """  
      self.Rpt1TaxableAmt:int = obj["Rpt1TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxableAmt:int = obj["Rpt2TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxableAmt:int = obj["Rpt3TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.RateCode:str = obj["RateCode"]
      """  Rate Code  """  
      self.CollectionType:int = obj["CollectionType"]
      """  Collection Type  """  
      self.Timing:int = obj["Timing"]
      """  Timing of when to report taxes  """  
      self.ExemptType:int = obj["ExemptType"]
      """  Exemption Type  """  
      self.ExemptPercent:int = obj["ExemptPercent"]
      """  Exemption Percent  """  
      self.ResolutionNum:str = obj["ResolutionNum"]
      """  Resolution Number  """  
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
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  The open A/R invoice # that the transaction applies against. Not used by the MisPay trantype. In the case of PayInv, or CMemo transaction this must be a valid InvcHead record where InvcHead.CreditMemo = No. In case of "Adjust" transactions this can be either a invoice or a credit memo reference. Note: The "Apply Credit Memo" program automatically creates an additional CashDtl records for each invoice to which the credit memo is applied.  In this additional record this field contains the credit memo's number.  """  
      self.InvoiceRef:int = obj["InvoiceRef"]
      """  Applicable to CMemo transaction types only. The "Apply Credit Memo" program creates two CashDtl records for each invoice that a credit memo is applied to. One record for the <credit> to the invoice and a second record for the debit to the credit memo. In the first record this field is the InvoiceNum of the Credit memo. In the second record it is the InvoiceNum of the invoice that the credit memo was applied to.  """  
      self.ECAcquisitionSeq:int = obj["ECAcquisitionSeq"]
      """   Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.
NOTE:  This field is now used in VAT Reverse Charge logic.  If an invoice line is marked for Reverse Charge, a second line is created just like in the ECAcquisition logic. To distinguish the two scenarios, the ReverseCharge flag will be set to true if the second line is for Reverse Charge.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Relates record to a BankAcct.  """  
      self.TranNum:int = obj["TranNum"]
      """  Unique ID of the Transaction.  """  
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
      self.Manual:bool = obj["Manual"]
      """  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  """  
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
      self.DiscTaxAdj:int = obj["DiscTaxAdj"]
      """  Discount Tax Adjustment  """  
      self.DocDiscTaxAdj:int = obj["DocDiscTaxAdj"]
      """  Discount Tax Adjustment in foreign currency.  """  
      self.Rpt1DiscTaxAdj:int = obj["Rpt1DiscTaxAdj"]
      """  Reporting currency value of this field  """  
      self.Rpt2DiscTaxAdj:int = obj["Rpt2DiscTaxAdj"]
      """  Reporting currency value of this field  """  
      self.Rpt3DiscTaxAdj:int = obj["Rpt3DiscTaxAdj"]
      """  Reporting currency value of this field  """  
      self.DiscTaxableAdj:int = obj["DiscTaxableAdj"]
      """  Discount Taxable Adjustment  """  
      self.DocDiscTaxableAdj:int = obj["DocDiscTaxableAdj"]
      """  Discount Taxable Adjustment in foreign currency.  """  
      self.Rpt1DiscTaxableAdj:int = obj["Rpt1DiscTaxableAdj"]
      """  Reporting currency value of this field  """  
      self.Rpt2DiscTaxableAdj:int = obj["Rpt2DiscTaxableAdj"]
      """  Reporting currency value of this field  """  
      self.Rpt3DiscTaxableAdj:int = obj["Rpt3DiscTaxableAdj"]
      """  Reporting currency value of this field  """  
      self.TextCode:str = obj["TextCode"]
      """  Unique Identifier for Legal Text  """  
      self.Voided:bool = obj["Voided"]
      """  Indicates if transaction was voided.  The rest of the unique key will contain the original transaction values (like APTran)  """  
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
      self.DiscTaxAdjVar:int = obj["DiscTaxAdjVar"]
      """  Discount Tax Adjustment Variance  """  
      self.DocDiscTaxAdjVar:int = obj["DocDiscTaxAdjVar"]
      """  Discount Tax Adjustment Variance  """  
      self.Rpt1DiscTaxAdjVar:int = obj["Rpt1DiscTaxAdjVar"]
      """  Reporting currency value of this field  """  
      self.Rpt2DiscTaxAdjVar:int = obj["Rpt2DiscTaxAdjVar"]
      """  Reporting currency value of this field  """  
      self.Rpt3DiscTaxAdjVar:int = obj["Rpt3DiscTaxAdjVar"]
      """  Reporting currency value of this field  """  
      self.PCashDeskID:str = obj["PCashDeskID"]
      """  Unique identifier of Petty Cash Desk  """  
      self.PCashRefNum:int = obj["PCashRefNum"]
      """  Reference Number, unique identifier of Petty Cash Document  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AGOrigTaxableAmt:int = obj["AGOrigTaxableAmt"]
      """  AGOrigTaxableAmt  """  
      self.GainLoss:int = obj["GainLoss"]
      """  GainLoss  """  
      self.DocGainLoss:int = obj["DocGainLoss"]
      """  DocGainLoss  """  
      self.Rpt1GainLoss:int = obj["Rpt1GainLoss"]
      """  Rpt1GainLoss  """  
      self.Rpt2GainLoss:int = obj["Rpt2GainLoss"]
      """  Rpt2GainLoss  """  
      self.Rpt3GainLoss:int = obj["Rpt3GainLoss"]
      """  Rpt3GainLoss  """  
      self.CNCFICode:str = obj["CNCFICode"]
      """  CNCFICode  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  APInvoiceNum  """  
      self.TranType:str = obj["TranType"]
      """  TranType  """  
      self.MovementNum:int = obj["MovementNum"]
      """  MovementNum  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.CNCFICodeDescription:str = obj["CNCFICodeDescription"]
      self.CTDescription:str = obj["CTDescription"]
      self.DisableManual:bool = obj["DisableManual"]
      """  Flag to indicate if Manual checkbos should be Read Only  """  
      self.GroupID:str = obj["GroupID"]
      """  Group ID - used to link to Cash Head  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.DedTaxChanged:bool = obj["DedTaxChanged"]
      """  The flag to indicate if the user changed Deductible Tax amount on manually updated tax record  """  
      self.EnableTax:bool = obj["EnableTax"]
      self.BitFlag:int = obj["BitFlag"]
      self.RateCodeDescription:str = obj["RateCodeDescription"]
      self.TaxCodeDescription:str = obj["TaxCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AssignLegalNumber_input:
   """ Required : 
   ds
   groupID
   headNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      """  ARPN group identifier.  """  
      self.headNum:int = obj["headNum"]
      """  ARPN header number.  """  
      pass

class AssignLegalNumber_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      self.legalNumMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class BatchGenPIs_input:
   """ Required : 
   ipCutOffDate
   ipPIStatus
   ipPmntMeth
   ipGroupID
   ipCurrencyCode
   """  
   def __init__(self, obj):
      self.ipCutOffDate:str = obj["ipCutOffDate"]
      """  ipCutOffDate  """  
      self.ipPIStatus:str = obj["ipPIStatus"]
      """  ipPIStatus  """  
      self.ipPmntMeth:str = obj["ipPmntMeth"]
      """  ipPmntMeth  """  
      self.ipGroupID:str = obj["ipGroupID"]
      """  ipGroupID  """  
      self.ipCurrencyCode:str = obj["ipCurrencyCode"]
      """  ipCurrencyCode  """  
      pass

class BatchGenPIs_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["returnObj"]
      pass

class CancelGenPI_input:
   """ Required : 
   ipARPNID
   ipInvoiceNum
   """  
   def __init__(self, obj):
      self.ipARPNID:str = obj["ipARPNID"]
      self.ipInvoiceNum:int = obj["ipInvoiceNum"]
      pass

class CancelGenPI_output:
   def __init__(self, obj):
      pass

class ChangeCurGroupID_input:
   """ Required : 
   ipHeadNum
   ipID
   ipCustID
   ipCurGroupID
   ipNewPIType
   """  
   def __init__(self, obj):
      self.ipHeadNum:int = obj["ipHeadNum"]
      self.ipID:str = obj["ipID"]
      self.ipCustID:str = obj["ipCustID"]
      self.ipCurGroupID:str = obj["ipCurGroupID"]
      self.ipNewPIType:str = obj["ipNewPIType"]
      pass

class ChangeCurGroupID_output:
   def __init__(self, obj):
      pass

class ChangeTranAmt_input:
   """ Required : 
   ipTranAmtType
   proposedTranAmt
   ds
   """  
   def __init__(self, obj):
      self.ipTranAmtType:str = obj["ipTranAmtType"]
      """  Indicate which of the transaction amount is changed.
            Valid values are: 'B' for Base Tran Amount and 'D' for Doc Tran Amount  """  
      self.proposedTranAmt:int = obj["proposedTranAmt"]
      """  The proposed Transaction Amount  """  
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

class ChangeTranAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckDocumentIsLocked_input:
   """ Required : 
   keyValue
   keyValue2
   """  
   def __init__(self, obj):
      self.keyValue:str = obj["keyValue"]
      """  GroupID  """  
      self.keyValue2:str = obj["keyValue2"]
      """  HeadNum  """  
      pass

class CheckDocumentIsLocked_output:
   def __init__(self, obj):
      pass

class CheckPNoteExisted_input:
   """ Required : 
   ipPIType
   ipID
   ipCustID
   """  
   def __init__(self, obj):
      self.ipPIType:str = obj["ipPIType"]
      self.ipID:str = obj["ipID"]
      self.ipCustID:str = obj["ipCustID"]
      pass

class CheckPNoteExisted_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opRet:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckPNotesExistTracker_input:
   """ Required : 
   ipID
   fromTracker
   """  
   def __init__(self, obj):
      self.ipID:str = obj["ipID"]
      """  ipID  """  
      self.fromTracker:bool = obj["fromTracker"]
      """  Indicates if the method was called from the Tracker or the Update program  """  
      pass

class CheckPNotesExistTracker_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opRet:str = obj["parameters"]
      self.headNum:int = obj["parameters"]
      self.groupID:str = obj["parameters"]
      self.custID:str = obj["parameters"]
      self.type:str = obj["parameters"]
      pass

      """  output parameters  """  

class CreateARPNMove_input:
   """ Required : 
   ipGroupID
   ipHeadNum
   ipCurGroupID
   ipPIStatus
   ipPIType
   ipPIStage
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      self.ipHeadNum:int = obj["ipHeadNum"]
      self.ipCurGroupID:str = obj["ipCurGroupID"]
      self.ipPIStatus:str = obj["ipPIStatus"]
      self.ipPIType:str = obj["ipPIType"]
      self.ipPIStage:str = obj["ipPIStage"]
      pass

class CreateARPNMove_output:
   def __init__(self, obj):
      pass

class DelARPNHead_input:
   """ Required : 
   ipGroupID
   ipHeadNum
   ipdelHead
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      self.ipHeadNum:int = obj["ipHeadNum"]
      self.ipdelHead:bool = obj["ipdelHead"]
      pass

class DelARPNHead_output:
   def __init__(self, obj):
      pass

class DeleteByID_input:
   """ Required : 
   groupID
   headNum
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      self.headNum:int = obj["headNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeletePICashGroup_input:
   """ Required : 
   groupID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      """  Cash Group ID  """  
      pass

class DeletePICashGroup_output:
   def __init__(self, obj):
      pass

class DeletePNbyID_input:
   """ Required : 
   ipGroupID
   ipHeadNum
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      self.ipHeadNum:int = obj["ipHeadNum"]
      pass

class DeletePNbyID_output:
   def __init__(self, obj):
      pass

class DeletePNotes_input:
   """ Required : 
   ipGroupID
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      pass

class DeletePNotes_output:
   def __init__(self, obj):
      pass

class DeleteZeroAmtTaxRec_input:
   """ Required : 
   postGroupID
   """  
   def __init__(self, obj):
      self.postGroupID:str = obj["postGroupID"]
      """  The Group ID of the Group to post  """  
      pass

class DeleteZeroAmtTaxRec_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_ARPNDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer Number  """  
      self.DiscountAmt:int = obj["DiscountAmt"]
      """  Discount Amount. Base Currency.  """  
      self.DocDiscountAmount:int = obj["DocDiscountAmount"]
      """  Discount Amount. Document Currency.  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """  Transaction Amount. Document Currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange Rate  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  Get Default Tax ID's flag.  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Posted to GL flag  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Reference to  invchead  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number  """  
      self.Posted:bool = obj["Posted"]
      """  Posted flag  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Rate Group code  """  
      self.RoundDiff:int = obj["RoundDiff"]
      """  Rounding Difference  """  
      self.Rpt1DiscountAmt:int = obj["Rpt1DiscountAmt"]
      """  Discount Amount. Report Currency 1.  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Transaction Amount. Report Currency 1.  """  
      self.Rpt2DiscountAmt:int = obj["Rpt2DiscountAmt"]
      """  Discount Amount. Report Currency 2.  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Transaction Amount. Report Currency 2.  """  
      self.Rpt3DiscountAmt:int = obj["Rpt3DiscountAmt"]
      """  Discount Amount. Report Currency 3.  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Transaction Amount. Report Currency 3.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Tax Liability  """  
      self.TranAmt:int = obj["TranAmt"]
      """  Transaction Amount  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction Date  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing transaction entry the user establishes a "Group ID". All transactions belong to a group. This current GroupID is assigned by the user.  Once created, it cannot be changed.  The Group ID is used to Selectively print and post the transactions.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  The foreign key that relates this detail record to a ARPNHead record. Duplicated from ARPNHead.HeadNum when record is created. Not applicable to user interface.  """  
      self.InvoiceRef:int = obj["InvoiceRef"]
      """  Applicable to CMemo transaction types only. The "Apply Credit Memo" program creates two CashDtl records for each invoice that a credit memo is applied to. One record for the <credit> to the invoice and a second record for the debit to the credit memo. In the first record this field is the InvoiceNum of the Credit memo. In the second record it is the InvoiceNum of the invoice that the credit memo was applied to.  """  
      self.DNAmount:int = obj["DNAmount"]
      """  The total debit note value applied for the invoice selected for the payment during the payment transaction.  """  
      self.DocDnAmount:int = obj["DocDnAmount"]
      """  The total debit note value applied for the invoice selected for the payment during the payment transaction.  """  
      self.Rpt1DnAmount:int = obj["Rpt1DnAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt2DnAmount:int = obj["Rpt2DnAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt3DnAmount:int = obj["Rpt3DnAmount"]
      """  Reporting currency value of this field  """  
      self.TranType:str = obj["TranType"]
      """   Identifies the type of transaction. Adjust = Adjustment, CMemo = Credit Memo Transfer, PrePay = Pre Payment, MisPay = Misc Payment, PayInv = Payment on Invoices. This is  duplicated from the CashHead.TranType, not user maintainable.
Note: For currency gain/loss it will be "Adjust". Both the Debit/Credit GL# will be used. Debit is A/R account. Credit is gain/loss account.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The unique identifier of the fiscal calendar.  """  
      self.DocSelfAssessAmt:int = obj["DocSelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Tax Amount in the vendors currency.  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period for the transaction. Not directly entered by the user. Duplicated from the CashBatc.FiscalPeriod at time of posting.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year. This is not entered by the user on each record. Instead as part of the posting process it is duplicated in from the CashBatc.FiscalYear. Therefore each batch is posted to a single fiscal period.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal Year Suffix.  """  
      self.Reference:str = obj["Reference"]
      """  Allows user to enter a short descriptive reference for the transaction. This is useful with Miscellaneous Cash Receipts.  """  
      self.Rpt1SelfAssessAmt:int = obj["Rpt1SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt2SelfAssessAmt:int = obj["Rpt2SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt3SelfAssessAmt:int = obj["Rpt3SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.SelfAssessAmt:int = obj["SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Total Tax Amount.  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.GainLossType:str = obj["GainLossType"]
      """  "R" for realized or "U" for unrealized Gain/Loss  """  
      self.ReverseGL:bool = obj["ReverseGL"]
      """  Indicates if it's a reversing Gain/Loss adjustment  """  
      self.RevalueDate:str = obj["RevalueDate"]
      """  Revaluation date that generated the gain/loss record  """  
      self.RevalueBal:int = obj["RevalueBal"]
      """  PI Balance at the time of revaluation  """  
      self.DocRevalueBal:int = obj["DocRevalueBal"]
      """  Document currency PI Balance at the time of revaluation  """  
      self.Rpt1RevalueBal:int = obj["Rpt1RevalueBal"]
      """  Reporting currency PI Balance at the time of revaluation  """  
      self.Rpt2RevalueBal:int = obj["Rpt2RevalueBal"]
      """  Reporting currency PI Balance at the time of revaluation  """  
      self.Rpt3RevalueBal:int = obj["Rpt3RevalueBal"]
      """  Reporting currency PI Balance at the time of revaluation  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type for the record.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      self.DocInvoiceAmt:int = obj["DocInvoiceAmt"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CurrencyDescription:str = obj["CurrencyDescription"]
      self.BaseCurrDesc:str = obj["BaseCurrDesc"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.DocInvoiceBal:int = obj["DocInvoiceBal"]
      self.InvTermsCode:str = obj["InvTermsCode"]
      self.InvDiscountDate:str = obj["InvDiscountDate"]
      self.InvDueDate:str = obj["InvDueDate"]
      self.DocNetCash:int = obj["DocNetCash"]
      self.DocNewBalance:int = obj["DocNewBalance"]
      self.InvLockRate:bool = obj["InvLockRate"]
      self.InvoiceBal:int = obj["InvoiceBal"]
      self.NewBalance:int = obj["NewBalance"]
      self.NetCash:int = obj["NetCash"]
      self.GainLossAmt:int = obj["GainLossAmt"]
      self.ApplyDate:str = obj["ApplyDate"]
      self.BillConNumber:int = obj["BillConNumber"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.DispGLAcct:str = obj["DispGLAcct"]
      self.DispTranAmt:int = obj["DispTranAmt"]
      self.DocDispTranAmt:int = obj["DocDispTranAmt"]
      self.DocSelfAssessTax:int = obj["DocSelfAssessTax"]
      self.DocWithholdTax:int = obj["DocWithholdTax"]
      self.FullyPaid:bool = obj["FullyPaid"]
      self.InvExchRate:int = obj["InvExchRate"]
      self.InvLegalNumber:str = obj["InvLegalNumber"]
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      self.InvXRateLabel:str = obj["InvXRateLabel"]
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.LegalNumStyle:str = obj["LegalNumStyle"]
      self.OldGainLoss:int = obj["OldGainLoss"]
      self.PostToGL:bool = obj["PostToGL"]
      self.SelfAssessTax:int = obj["SelfAssessTax"]
      self.SoldToCustID:str = obj["SoldToCustID"]
      self.SoldToCustNum:int = obj["SoldToCustNum"]
      self.SoldToCustomerName:str = obj["SoldToCustomerName"]
      self.WithholdTax:int = obj["WithholdTax"]
      self.XRateLabel:str = obj["XRateLabel"]
      self.Rpt1NewBalance:int = obj["Rpt1NewBalance"]
      self.Rpt3NewBalance:int = obj["Rpt3NewBalance"]
      self.Rpt1DispTranAmt:int = obj["Rpt1DispTranAmt"]
      self.Rpt2DispTranAmt:int = obj["Rpt2DispTranAmt"]
      self.Rpt3DispTranAmt:int = obj["Rpt3DispTranAmt"]
      self.Rpt1OldGainLoss:int = obj["Rpt1OldGainLoss"]
      self.Rpt2OldGainLoss:int = obj["Rpt2OldGainLoss"]
      self.Rpt3OldGainLoss:int = obj["Rpt3OldGainLoss"]
      self.Rpt1GainLossAmt:int = obj["Rpt1GainLossAmt"]
      self.Rpt2GainLossAmt:int = obj["Rpt2GainLossAmt"]
      self.Rpt3GainLossAmt:int = obj["Rpt3GainLossAmt"]
      self.Rpt1InvoiceAmt:int = obj["Rpt1InvoiceAmt"]
      self.Rpt2InvoiceAmt:int = obj["Rpt2InvoiceAmt"]
      self.Rpt3InvoiceAmt:int = obj["Rpt3InvoiceAmt"]
      self.Rpt1InvoiceBal:int = obj["Rpt1InvoiceBal"]
      self.Rpt2InvoiceBal:int = obj["Rpt2InvoiceBal"]
      self.Rpt3InvoiceBal:int = obj["Rpt3InvoiceBal"]
      self.Rpt2NewBalance:int = obj["Rpt2NewBalance"]
      self.Rpt1NetCash:int = obj["Rpt1NetCash"]
      self.Rpt2NetCash:int = obj["Rpt2NetCash"]
      self.Rpt3NetCash:int = obj["Rpt3NetCash"]
      self.InvoicePosted:bool = obj["InvoicePosted"]
      self.CurGroupID:str = obj["CurGroupID"]
      self.BitFlag:int = obj["BitFlag"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.InvoiceNumTermsCode:str = obj["InvoiceNumTermsCode"]
      self.InvoiceNumCardMemberName:str = obj["InvoiceNumCardMemberName"]
      self.TaxRgnDescription:str = obj["TaxRgnDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ARPNHeadAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.GroupID:str = obj["GroupID"]
      self.HeadNum:int = obj["HeadNum"]
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

class Erp_Tablesets_ARPNHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TranAmt:int = obj["TranAmt"]
      """  Transaction Amount  """  
      self.AppliedAmt:int = obj["AppliedAmt"]
      """  Applied Amount  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Bank Account ID  """  
      self.BankAmount:int = obj["BankAmount"]
      """  Bank Amount  """  
      self.BankSlip:str = obj["BankSlip"]
      """  Bank Slip Number of the promissory note.  """  
      self.BaseAmount:int = obj["BaseAmount"]
      """  Base Amount  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  When creating a new CashBdtl, the next available # is assigned by the system.  The system generates a number by finding the last CashBdtl of a cashbhed and uses its CashBookLine + 1. Not directly entered by the user.  """  
      self.CompBankAcctID:str = obj["CompBankAcctID"]
      """  Company Bank Account ID  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.CustBankAcctID:str = obj["CustBankAcctID"]
      """  Customer Bank Account ID  """  
      self.CustID:str = obj["CustID"]
      """  Customer ID  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer Number  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.DiscountAmt:int = obj["DiscountAmt"]
      """  Discount Amount. Base Currency.  """  
      self.DocAppliedAmt:int = obj["DocAppliedAmt"]
      """  Applied Amount. Document Currency.  """  
      self.DocUnAppliedAmt:int = obj["DocUnAppliedAmt"]
      """  Unapplied Amount. Document Currency.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Tax Amount. Document Currency.  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """  Transaction Amount. Document Currency.  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  Withholding Amount. Document Currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange Rate  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  Get Default Tax ID's flag.  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Posted to GL flag  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number  """  
      self.Paid:bool = obj["Paid"]
      """  Paid flag  """  
      self.Posted:bool = obj["Posted"]
      """  Posted flag  """  
      self.ProcessCard:str = obj["ProcessCard"]
      """  Process Card  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Rate Group code  """  
      self.RecalcBeforePost:bool = obj["RecalcBeforePost"]
      """  Recalculated before posting.  """  
      self.Rpt1AppliedAmt:int = obj["Rpt1AppliedAmt"]
      """  Applied Amount. Report Currency 1.  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Tax Amount. Report Currency 1.  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Transaction Amount. Report Currency 1.  """  
      self.Rpt1UnappliedAmt:int = obj["Rpt1UnappliedAmt"]
      """  Unapplied Amount. Report Currency 1.  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Withholding Amount. Report Currency 1.  """  
      self.Rpt2AppliedAmt:int = obj["Rpt2AppliedAmt"]
      """  Applied Amount. Report Currency 2.  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Tax Amount. Report Currency 2.  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Transaction Amount. Report Currency 2.  """  
      self.Rpt2UnappliedAmt:int = obj["Rpt2UnappliedAmt"]
      """  Unapplied Amount. Report Currency 2.  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Withholding Amount. Report Currency 2.  """  
      self.Rpt3AppliedAmt:int = obj["Rpt3AppliedAmt"]
      """  Applied Amount. Report Currency 3.  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Tax Amount. Report Currency 3.  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Transaction Amount. Report Currency 3.  """  
      self.Rpt3UnappliedAmt:int = obj["Rpt3UnappliedAmt"]
      """  Unapplied Amount. Report Currency 3.  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Withholding Amount. Report Currency 3.  """  
      self.Signed:bool = obj["Signed"]
      """  Signed flag  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Tax Amount. Base Currency.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Tax Liability  """  
      self.TotalARAmt:int = obj["TotalARAmt"]
      """  Total AR Amount  """  
      self.TransDate:str = obj["TransDate"]
      """  Transaction Date  """  
      self.UnappliedAmt:int = obj["UnappliedAmt"]
      """  Unapplied Amount. Base Currency.  """  
      self.Voided:bool = obj["Voided"]
      """  Voided Flag  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  Withholding Amount. Base Currency.  """  
      self.CompanyName:str = obj["CompanyName"]
      """  Company Name  """  
      self.CompanyAddr1:str = obj["CompanyAddr1"]
      """  First company address line.  """  
      self.CompanyAddr2:str = obj["CompanyAddr2"]
      """  Second company address line.  """  
      self.CompanyAddr3:str = obj["CompanyAddr3"]
      """  Third company address line.  """  
      self.CompanyCity:str = obj["CompanyCity"]
      """  Company City portion of the address.  """  
      self.CompanyState:str = obj["CompanyState"]
      """  Company State portion of the address.  """  
      self.CompanyPostalCode:str = obj["CompanyPostalCode"]
      """  Company Postal Code or Zip Code portion of the address.  """  
      self.CompanyCountry:str = obj["CompanyCountry"]
      """  Company Country portion of the address.  """  
      self.CustomerName:str = obj["CustomerName"]
      """  Company Name  """  
      self.CustomerAddr1:str = obj["CustomerAddr1"]
      """  First customer address line.  """  
      self.CustomerAddr2:str = obj["CustomerAddr2"]
      """  Second customer address line.  """  
      self.CustomerAddr3:str = obj["CustomerAddr3"]
      """  Third customer address line.  """  
      self.CustomerState:str = obj["CustomerState"]
      """  Customer Stateportion of the address.  """  
      self.CustomerPostalCode:str = obj["CustomerPostalCode"]
      """  Customer City portion of the address.  """  
      self.CustomerCity:str = obj["CustomerCity"]
      """  Customer Postal Code or Zip Code portion of the address.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing transaction entry the user establishes a "Group ID". All transactions belong to a group. This current GroupID is assigned by the user.  Once created, it cannot be changed.  The Group ID is used to Selectively print and post the transactions.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  An integer automatically assigned by the system using the database sequence called "CashHeadSeq". Which along with company and BatchID creates a unique key for the record. This is for internal control only the user never needs to reference.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Reference to  invchead  """  
      self.ARPromNoteID:str = obj["ARPromNoteID"]
      """  AR Payment Instrument ID  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year. This is not entered by the user on each record. Duplicated in from the CashGroup.FiscalYear. Therefore each batch is posted to a single fiscal period.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period for the transaction. Not directly entered by the user. Duplicated from the CashGroup.FiscalPeriod.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The unique identifier of the fiscal calendar.  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  """  
      self.TranType:str = obj["TranType"]
      """  Transaction Type  """  
      self.Sent:bool = obj["Sent"]
      """  Sent Flag  """  
      self.Type:str = obj["Type"]
      """  Type  """  
      self.IssueDate:str = obj["IssueDate"]
      """  Issue Date  """  
      self.DueDate:str = obj["DueDate"]
      """  Due date of the promissory note.  """  
      self.CompBankBranchCode:str = obj["CompBankBranchCode"]
      """  Bank/Branch Code for company's bank.  """  
      self.CompIBANCode:str = obj["CompIBANCode"]
      """  IBANCode for company's bank.  """  
      self.CustBankBranchCode:str = obj["CustBankBranchCode"]
      """  Bank/Branch Code for customer's bank.  """  
      self.CustIBANCode:str = obj["CustIBANCode"]
      """  IBAN Code for customer's bank.  """  
      self.AutoGenerated:bool = obj["AutoGenerated"]
      """  Indicates whether Payment Instrument was auto-generated from AR Invoice Entry.  """  
      self.DirectDeposit:bool = obj["DirectDeposit"]
      """  If true, indicates that Customer is flagged as Direct Deposit. Comes from field Customer.DirectDeposit.  """  
      self.ClearedAmt:int = obj["ClearedAmt"]
      """  Amount that the bank cleared the payment instrument for.  """  
      self.ClearedDate:str = obj["ClearedDate"]
      """  Date that the payment instrument was cleared in the system (System Set).  """  
      self.ClearedPending:bool = obj["ClearedPending"]
      """  Indicates that the payment instrument is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedPerson:str = obj["ClearedPerson"]
      """  Person who cleared the payment instrument (System Set).  """  
      self.ClearedPI:bool = obj["ClearedPI"]
      """  Indicates the Payment Instrument's cleared status.  When the Bank Statement is posted all Pending Transactions and Payment Instruments are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedStmtEndDate:str = obj["ClearedStmtEndDate"]
      """  End Date of the Statement that the payment instrument was cleared on.  """  
      self.ClearedTime:str = obj["ClearedTime"]
      """  Time that the payment instrument was cleared in the system - in HH:MM:SS format (System Set).  """  
      self.DocClearedAmt:int = obj["DocClearedAmt"]
      """  Amount that the bank cleared the check for.(Vendors Currency)  """  
      self.Rpt1ClearedAmt:int = obj["Rpt1ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2ClearedAmt:int = obj["Rpt2ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3ClearedAmt:int = obj["Rpt3ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  This field identifies a bankslip.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.DocumentPrinted:bool = obj["DocumentPrinted"]
      """  Indicates if the document has been printed.  """  
      self.CustCountryCode:int = obj["CustCountryCode"]
      """  Customer's country code  """  
      self.CustomerCountry:str = obj["CustomerCountry"]
      """  Customer country portion of the address.  """  
      self.PIStatus:str = obj["PIStatus"]
      """  Promissory Note Status  """  
      self.CurGroupID:str = obj["CurGroupID"]
      """  Current Group  """  
      self.PIStage:str = obj["PIStage"]
      """  Stage  """  
      self.ChgComment:str = obj["ChgComment"]
      """  Reason to change Company or Customer information  """  
      self.HoldReason:str = obj["HoldReason"]
      """  Hold from Application reason  """  
      self.LockRate:bool = obj["LockRate"]
      """  Lock Exchange Rate  """  
      self.ReferseRef:int = obj["ReferseRef"]
      """  Reference to reversed PI  """  
      self.ReverseDate:str = obj["ReverseDate"]
      """  Reverse Date  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BankClearedAmt:int = obj["BankClearedAmt"]
      """  BankClearedAmt  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.OnAccount:bool = obj["OnAccount"]
      """  OnAccount  """  
      self.DiscountCashDate:str = obj["DiscountCashDate"]
      """  DiscountCashDate  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.BaseCurrencyCode:str = obj["BaseCurrencyCode"]
      self.BaseCurrencyDesc:str = obj["BaseCurrencyDesc"]
      self.TermsDesc:str = obj["TermsDesc"]
      self.CurrencyDesc:str = obj["CurrencyDesc"]
      self.TotalCashReceived:int = obj["TotalCashReceived"]
      self.CompanyBankName:str = obj["CompanyBankName"]
      self.CompanyBankAcct:str = obj["CompanyBankAcct"]
      self.CompanyBankIdentifier:str = obj["CompanyBankIdentifier"]
      self.CustomerBankName:str = obj["CustomerBankName"]
      self.CustomerBankAcct:str = obj["CustomerBankAcct"]
      self.CustomerBankIdentifier:str = obj["CustomerBankIdentifier"]
      self.calcRate:bool = obj["calcRate"]
      """  Indicates if rate was calculates from TranAmt field instead of CurrExRate table  """  
      self.ApplyDate:str = obj["ApplyDate"]
      self.BankCurrencyCode:str = obj["BankCurrencyCode"]
      self.BankCurrSymbol:str = obj["BankCurrSymbol"]
      self.BillToName:str = obj["BillToName"]
      self.CreditHold:bool = obj["CreditHold"]
      """  Customer Credit Hold flag  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.DispGLAcct:str = obj["DispGLAcct"]
      """  Display GL Account  """  
      self.DocDiscount:int = obj["DocDiscount"]
      self.DocReceipt:int = obj["DocReceipt"]
      self.FullyPaid:bool = obj["FullyPaid"]
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.TotalRoundDiff:int = obj["TotalRoundDiff"]
      self.TranTaxAmt:int = obj["TranTaxAmt"]
      self.XRateLabel:str = obj["XRateLabel"]
      self.DocTranTaxAmt:int = obj["DocTranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.Rpt1TranTaxAmt:int = obj["Rpt1TranTaxAmt"]
      self.Rpt2TranTaxAmt:int = obj["Rpt2TranTaxAmt"]
      self.Rpt3TranTaxAmt:int = obj["Rpt3TranTaxAmt"]
      self.CompBankBranchCodeDesc:str = obj["CompBankBranchCodeDesc"]
      self.CustBankBranchCodeDesc:str = obj["CustBankBranchCodeDesc"]
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      """  Indicates if changes can occur after the document has been printed  """  
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      """  Indicates if assign legal number option is available.  """  
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      """  Indicates if the void legal number option is available  """  
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      """  Indicates if a legal number configuration exists for miscellaneous shipments  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      """  Indicates if TranDocTypeID is available for input.  """  
      self.PIStatusDesc:str = obj["PIStatusDesc"]
      self.PITypeInitiation:str = obj["PITypeInitiation"]
      """  like PIType.Initiation  """  
      self.DocGainLossReal:int = obj["DocGainLossReal"]
      self.DocGainLossUnreal:int = obj["DocGainLossUnreal"]
      self.GainLossReal:int = obj["GainLossReal"]
      self.GainLossUnreal:int = obj["GainLossUnreal"]
      self.Rpt1GainLossReal:int = obj["Rpt1GainLossReal"]
      self.Rpt1GainLossUnreal:int = obj["Rpt1GainLossUnreal"]
      self.Rpt2GainLossReal:int = obj["Rpt2GainLossReal"]
      self.Rpt2GainLossUnreal:int = obj["Rpt2GainLossUnreal"]
      self.Rpt3GainLossReal:int = obj["Rpt3GainLossReal"]
      self.Rpt3GainLossUnreal:int = obj["Rpt3GainLossUnreal"]
      self.RevalueDate:str = obj["RevalueDate"]
      self.DocDiscountAmt:int = obj["DocDiscountAmt"]
      self.Rpt1DiscountAmt:int = obj["Rpt1DiscountAmt"]
      self.Rpt2DiscountAmt:int = obj["Rpt2DiscountAmt"]
      self.Rpt3DiscountAmt:int = obj["Rpt3DiscountAmt"]
      self.Receipt:int = obj["Receipt"]
      self.Rpt1Receipt:int = obj["Rpt1Receipt"]
      self.Rpt2Receipt:int = obj["Rpt2Receipt"]
      self.Rpt3Receipt:int = obj["Rpt3Receipt"]
      self.BankAcctBankName:str = obj["BankAcctBankName"]
      """  The Bank's full name.  """  
      self.BankAcctDescription:str = obj["BankAcctDescription"]
      """  Full description of the bank account.  """  
      self.CashbookLineDescription:str = obj["CashbookLineDescription"]
      """  Description  """  
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CustNumName:str = obj["CustNumName"]
      """  The full name of the customer.  """  
      self.CustNumBTName:str = obj["CustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustNumCustID:str = obj["CustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.PIStatusStatusDesc:str = obj["PIStatusStatusDesc"]
      """  Status Description  """  
      self.PITypeDescription:str = obj["PITypeDescription"]
      """  Type Description  """  
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      """  Description  """  
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      """  Full description for the Tax Region.  """  
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      """  Description  """  
      self.BankRecGainLoss:int = obj["BankRecGainLoss"]
      self.DocBankRecGainLoss:int = obj["DocBankRecGainLoss"]
      self.Rpt1BankRecGainLoss:int = obj["Rpt1BankRecGainLoss"]
      self.Rpt2BankRecGainLoss:int = obj["Rpt2BankRecGainLoss"]
      self.Rpt3BankRecGainLoss:int = obj["Rpt3BankRecGainLoss"]
      self.BankTotalAmount:int = obj["BankTotalAmount"]
      self.StatusChgTranDocType:str = obj["StatusChgTranDocType"]
      self.StatusChgLegalNum:str = obj["StatusChgLegalNum"]
      self.ARPNDtlExists:bool = obj["ARPNDtlExists"]
      """  for kinetic purposes  """  
      self.ARPNDtlInvoicePosted:bool = obj["ARPNDtlInvoicePosted"]
      """  for kinetic purposes  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ARPNHeadListTableset:
   def __init__(self, obj):
      self.ARPNHeadList:list[Erp_Tablesets_ARPNHeadListRow] = obj["ARPNHeadList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ARPNHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TranAmt:int = obj["TranAmt"]
      """  Transaction Amount  """  
      self.AppliedAmt:int = obj["AppliedAmt"]
      """  Applied Amount  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Bank Account ID  """  
      self.BankAmount:int = obj["BankAmount"]
      """  Bank Amount  """  
      self.BankSlip:str = obj["BankSlip"]
      """  Bank Slip Number of the promissory note.  """  
      self.BaseAmount:int = obj["BaseAmount"]
      """  Base Amount  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  When creating a new CashBdtl, the next available # is assigned by the system.  The system generates a number by finding the last CashBdtl of a cashbhed and uses its CashBookLine + 1. Not directly entered by the user.  """  
      self.CompBankAcctID:str = obj["CompBankAcctID"]
      """  Company Bank Account ID  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.CustBankAcctID:str = obj["CustBankAcctID"]
      """  Customer Bank Account ID  """  
      self.CustID:str = obj["CustID"]
      """  Customer ID  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer Number  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.DiscountAmt:int = obj["DiscountAmt"]
      """  Discount Amount. Base Currency.  """  
      self.DocAppliedAmt:int = obj["DocAppliedAmt"]
      """  Applied Amount. Document Currency.  """  
      self.DocUnAppliedAmt:int = obj["DocUnAppliedAmt"]
      """  Unapplied Amount. Document Currency.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Tax Amount. Document Currency.  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """  Transaction Amount. Document Currency.  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  Withholding Amount. Document Currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange Rate  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  Get Default Tax ID's flag.  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Posted to GL flag  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number  """  
      self.Paid:bool = obj["Paid"]
      """  Paid flag  """  
      self.Posted:bool = obj["Posted"]
      """  Posted flag  """  
      self.ProcessCard:str = obj["ProcessCard"]
      """  Process Card  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Rate Group code  """  
      self.RecalcBeforePost:bool = obj["RecalcBeforePost"]
      """  Recalculated before posting.  """  
      self.Rpt1AppliedAmt:int = obj["Rpt1AppliedAmt"]
      """  Applied Amount. Report Currency 1.  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Tax Amount. Report Currency 1.  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Transaction Amount. Report Currency 1.  """  
      self.Rpt1UnappliedAmt:int = obj["Rpt1UnappliedAmt"]
      """  Unapplied Amount. Report Currency 1.  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Withholding Amount. Report Currency 1.  """  
      self.Rpt2AppliedAmt:int = obj["Rpt2AppliedAmt"]
      """  Applied Amount. Report Currency 2.  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Tax Amount. Report Currency 2.  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Transaction Amount. Report Currency 2.  """  
      self.Rpt2UnappliedAmt:int = obj["Rpt2UnappliedAmt"]
      """  Unapplied Amount. Report Currency 2.  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Withholding Amount. Report Currency 2.  """  
      self.Rpt3AppliedAmt:int = obj["Rpt3AppliedAmt"]
      """  Applied Amount. Report Currency 3.  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Tax Amount. Report Currency 3.  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Transaction Amount. Report Currency 3.  """  
      self.Rpt3UnappliedAmt:int = obj["Rpt3UnappliedAmt"]
      """  Unapplied Amount. Report Currency 3.  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Withholding Amount. Report Currency 3.  """  
      self.Signed:bool = obj["Signed"]
      """  Signed flag  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Tax Amount. Base Currency.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Tax Liability  """  
      self.TotalARAmt:int = obj["TotalARAmt"]
      """  Total AR Amount  """  
      self.TransDate:str = obj["TransDate"]
      """  Transaction Date  """  
      self.UnappliedAmt:int = obj["UnappliedAmt"]
      """  Unapplied Amount. Base Currency.  """  
      self.Voided:bool = obj["Voided"]
      """  Voided Flag  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  Withholding Amount. Base Currency.  """  
      self.CompanyName:str = obj["CompanyName"]
      """  Company Name  """  
      self.CompanyAddr1:str = obj["CompanyAddr1"]
      """  First company address line.  """  
      self.CompanyAddr2:str = obj["CompanyAddr2"]
      """  Second company address line.  """  
      self.CompanyAddr3:str = obj["CompanyAddr3"]
      """  Third company address line.  """  
      self.CompanyCity:str = obj["CompanyCity"]
      """  Company City portion of the address.  """  
      self.CompanyState:str = obj["CompanyState"]
      """  Company State portion of the address.  """  
      self.CompanyPostalCode:str = obj["CompanyPostalCode"]
      """  Company Postal Code or Zip Code portion of the address.  """  
      self.CompanyCountry:str = obj["CompanyCountry"]
      """  Company Country portion of the address.  """  
      self.CustomerName:str = obj["CustomerName"]
      """  Company Name  """  
      self.CustomerAddr1:str = obj["CustomerAddr1"]
      """  First customer address line.  """  
      self.CustomerAddr2:str = obj["CustomerAddr2"]
      """  Second customer address line.  """  
      self.CustomerAddr3:str = obj["CustomerAddr3"]
      """  Third customer address line.  """  
      self.CustomerState:str = obj["CustomerState"]
      """  Customer Stateportion of the address.  """  
      self.CustomerPostalCode:str = obj["CustomerPostalCode"]
      """  Customer City portion of the address.  """  
      self.CustomerCity:str = obj["CustomerCity"]
      """  Customer Postal Code or Zip Code portion of the address.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing transaction entry the user establishes a "Group ID". All transactions belong to a group. This current GroupID is assigned by the user.  Once created, it cannot be changed.  The Group ID is used to Selectively print and post the transactions.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  An integer automatically assigned by the system using the database sequence called "CashHeadSeq". Which along with company and BatchID creates a unique key for the record. This is for internal control only the user never needs to reference.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Reference to  invchead  """  
      self.ARPromNoteID:str = obj["ARPromNoteID"]
      """  AR Payment Instrument ID  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year. This is not entered by the user on each record. Duplicated in from the CashGroup.FiscalYear. Therefore each batch is posted to a single fiscal period.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period for the transaction. Not directly entered by the user. Duplicated from the CashGroup.FiscalPeriod.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The unique identifier of the fiscal calendar.  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  """  
      self.TranType:str = obj["TranType"]
      """  Transaction Type  """  
      self.Sent:bool = obj["Sent"]
      """  Sent Flag  """  
      self.Type:str = obj["Type"]
      """  Type  """  
      self.IssueDate:str = obj["IssueDate"]
      """  Issue Date  """  
      self.DueDate:str = obj["DueDate"]
      """  Due date of the promissory note.  """  
      self.CompBankBranchCode:str = obj["CompBankBranchCode"]
      """  Bank/Branch Code for company's bank.  """  
      self.CompIBANCode:str = obj["CompIBANCode"]
      """  IBANCode for company's bank.  """  
      self.CustBankBranchCode:str = obj["CustBankBranchCode"]
      """  Bank/Branch Code for customer's bank.  """  
      self.CustIBANCode:str = obj["CustIBANCode"]
      """  IBAN Code for customer's bank.  """  
      self.AutoGenerated:bool = obj["AutoGenerated"]
      """  Indicates whether Payment Instrument was auto-generated from AR Invoice Entry.  """  
      self.DirectDeposit:bool = obj["DirectDeposit"]
      """  If true, indicates that Customer is flagged as Direct Deposit. Comes from field Customer.DirectDeposit.  """  
      self.ClearedAmt:int = obj["ClearedAmt"]
      """  Amount that the bank cleared the payment instrument for.  """  
      self.ClearedDate:str = obj["ClearedDate"]
      """  Date that the payment instrument was cleared in the system (System Set).  """  
      self.ClearedPending:bool = obj["ClearedPending"]
      """  Indicates that the payment instrument is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedPerson:str = obj["ClearedPerson"]
      """  Person who cleared the payment instrument (System Set).  """  
      self.ClearedPI:bool = obj["ClearedPI"]
      """  Indicates the Payment Instrument's cleared status.  When the Bank Statement is posted all Pending Transactions and Payment Instruments are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedStmtEndDate:str = obj["ClearedStmtEndDate"]
      """  End Date of the Statement that the payment instrument was cleared on.  """  
      self.ClearedTime:str = obj["ClearedTime"]
      """  Time that the payment instrument was cleared in the system - in HH:MM:SS format (System Set).  """  
      self.DocClearedAmt:int = obj["DocClearedAmt"]
      """  Amount that the bank cleared the check for.(Vendors Currency)  """  
      self.Rpt1ClearedAmt:int = obj["Rpt1ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2ClearedAmt:int = obj["Rpt2ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3ClearedAmt:int = obj["Rpt3ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  This field identifies a bankslip.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.DocumentPrinted:bool = obj["DocumentPrinted"]
      """  Indicates if the document has been printed.  """  
      self.CustCountryCode:int = obj["CustCountryCode"]
      """  Customer's country code  """  
      self.CustomerCountry:str = obj["CustomerCountry"]
      """  Customer country portion of the address.  """  
      self.PIStatus:str = obj["PIStatus"]
      """  Promissory Note Status  """  
      self.CurGroupID:str = obj["CurGroupID"]
      """  Current Group  """  
      self.PIStage:str = obj["PIStage"]
      """  Stage  """  
      self.ChgComment:str = obj["ChgComment"]
      """  Reason to change Company or Customer information  """  
      self.HoldReason:str = obj["HoldReason"]
      """  Hold from Application reason  """  
      self.LockRate:bool = obj["LockRate"]
      """  Lock Exchange Rate  """  
      self.ReferseRef:int = obj["ReferseRef"]
      """  Reference to reversed PI  """  
      self.ReverseDate:str = obj["ReverseDate"]
      """  Reverse Date  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BankClearedAmt:int = obj["BankClearedAmt"]
      """  BankClearedAmt  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.TotalBankFee:int = obj["TotalBankFee"]
      """  TotalBankFee  """  
      self.DocTotalBankFee:int = obj["DocTotalBankFee"]
      """  DocTotalBankFee  """  
      self.Rpt1TotalBankFee:int = obj["Rpt1TotalBankFee"]
      """  Rpt1TotalBankFee  """  
      self.Rpt2TotalBankFee:int = obj["Rpt2TotalBankFee"]
      """  Rpt2TotalBankFee  """  
      self.Rpt3TotalBankFee:int = obj["Rpt3TotalBankFee"]
      """  Rpt3TotalBankFee  """  
      self.OnAccount:bool = obj["OnAccount"]
      """  OnAccount  """  
      self.IssuerName:str = obj["IssuerName"]
      """  Issuer Name  """  
      self.SignedBy:str = obj["SignedBy"]
      """  Signed By  """  
      self.SignedDate:str = obj["SignedDate"]
      """  Signed Date  """  
      self.SigneeAddr1:str = obj["SigneeAddr1"]
      """  Signee Address 1  """  
      self.SigneeAddr2:str = obj["SigneeAddr2"]
      """  Signee Address 2  """  
      self.SigneeAddr3:str = obj["SigneeAddr3"]
      """  Signee Address 3  """  
      self.SigneeCity:str = obj["SigneeCity"]
      """  Signee City  """  
      self.SigneeState:str = obj["SigneeState"]
      """  Signee State  """  
      self.SigneeZip:str = obj["SigneeZip"]
      """  Signee Postal Code  """  
      self.SigneeCountryNum:int = obj["SigneeCountryNum"]
      """  Signee Country Number  """  
      self.SigneePhoneNum:str = obj["SigneePhoneNum"]
      """  Signee Phone  """  
      self.SigneeEMailAddress:str = obj["SigneeEMailAddress"]
      """  Signee Email Address  """  
      self.SigneeComment:str = obj["SigneeComment"]
      """  Signee Comment  """  
      self.DiscountChargeAmt:int = obj["DiscountChargeAmt"]
      """  DiscountChargeAmt  """  
      self.DocDiscountChargeAmt:int = obj["DocDiscountChargeAmt"]
      """  DocDiscountChargeAmt  """  
      self.Rpt1DiscountChargeAmt:int = obj["Rpt1DiscountChargeAmt"]
      """  Rpt1DiscountChargeAmt  """  
      self.Rpt2DiscountChargeAmt:int = obj["Rpt2DiscountChargeAmt"]
      """  Rpt2DiscountChargeAmt  """  
      self.Rpt3DiscountChargeAmt:int = obj["Rpt3DiscountChargeAmt"]
      """  Rpt3DiscountChargeAmt  """  
      self.SigneeBankName:str = obj["SigneeBankName"]
      """  Signee Bank Name  """  
      self.SigneeBankAcct:str = obj["SigneeBankAcct"]
      """  Signee Bank Account Number  """  
      self.SigneeBankIdentifier:str = obj["SigneeBankIdentifier"]
      """  Signee Bank Identifier  """  
      self.SigneeIBANCode:str = obj["SigneeIBANCode"]
      """  Signee IBAN Code  """  
      self.SigneeBankBranchCode:str = obj["SigneeBankBranchCode"]
      """  Signee Bank BranchCode  """  
      self.DiscountCashDate:str = obj["DiscountCashDate"]
      """  DiscountCashDate  """  
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      """  Indicates if changes can occur after the document has been printed  """  
      self.ApplyDate:str = obj["ApplyDate"]
      self.BankCurrencyCode:str = obj["BankCurrencyCode"]
      self.BankCurrSymbol:str = obj["BankCurrSymbol"]
      self.BankRecGainLoss:int = obj["BankRecGainLoss"]
      self.calcRate:bool = obj["calcRate"]
      """  Indicates if rate was calculates from TranAmt field instead of CurrExRate table  """  
      self.CompanyBankAcct:str = obj["CompanyBankAcct"]
      self.CompanyBankIdentifier:str = obj["CompanyBankIdentifier"]
      self.CompanyBankName:str = obj["CompanyBankName"]
      self.CompBankBranchCodeDesc:str = obj["CompBankBranchCodeDesc"]
      self.CreditHold:bool = obj["CreditHold"]
      """  Customer Credit Hold flag  """  
      self.CurrencyDesc:str = obj["CurrencyDesc"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CustBankBranchCodeDesc:str = obj["CustBankBranchCodeDesc"]
      self.CustomerBankAcct:str = obj["CustomerBankAcct"]
      self.CustomerBankIdentifier:str = obj["CustomerBankIdentifier"]
      self.CustomerBankName:str = obj["CustomerBankName"]
      self.DisableBankAcctIDPI:bool = obj["DisableBankAcctIDPI"]
      self.DisableBankAmt:bool = obj["DisableBankAmt"]
      """   The flag to indicate if BankClearedAmt is not available to make changes.
(If Bank currency equals transaction currency this flag is true)  """  
      self.DispGLAcct:str = obj["DispGLAcct"]
      """  Display GL Account  """  
      self.DocBankRecGainLoss:int = obj["DocBankRecGainLoss"]
      self.DocDiscount:int = obj["DocDiscount"]
      self.DocDiscountAmt:int = obj["DocDiscountAmt"]
      self.DocGainLossReal:int = obj["DocGainLossReal"]
      self.DocGainLossUnreal:int = obj["DocGainLossUnreal"]
      self.DocReceipt:int = obj["DocReceipt"]
      self.DocTranTaxAmt:int = obj["DocTranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      """  Indicates if assign legal number option is available.  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      """  Indicates if TranDocTypeID is available for input.  """  
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      """  Indicates if the void legal number option is available  """  
      self.FullyPaid:bool = obj["FullyPaid"]
      self.GainLossReal:int = obj["GainLossReal"]
      self.GainLossUnreal:int = obj["GainLossUnreal"]
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      """  Indicates if a legal number configuration exists for miscellaneous shipments  """  
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.PIStatusDesc:str = obj["PIStatusDesc"]
      self.PITypeInitiation:str = obj["PITypeInitiation"]
      """  like PIType.Initiation  """  
      self.Receipt:int = obj["Receipt"]
      self.RevalueDate:str = obj["RevalueDate"]
      self.Rpt1BankRecGainLoss:int = obj["Rpt1BankRecGainLoss"]
      self.Rpt1DiscountAmt:int = obj["Rpt1DiscountAmt"]
      self.Rpt1GainLossReal:int = obj["Rpt1GainLossReal"]
      self.Rpt1GainLossUnreal:int = obj["Rpt1GainLossUnreal"]
      self.Rpt1Receipt:int = obj["Rpt1Receipt"]
      self.Rpt1TranTaxAmt:int = obj["Rpt1TranTaxAmt"]
      self.Rpt2BankRecGainLoss:int = obj["Rpt2BankRecGainLoss"]
      self.Rpt2DiscountAmt:int = obj["Rpt2DiscountAmt"]
      self.Rpt2GainLossReal:int = obj["Rpt2GainLossReal"]
      self.Rpt2GainLossUnreal:int = obj["Rpt2GainLossUnreal"]
      self.Rpt2Receipt:int = obj["Rpt2Receipt"]
      self.Rpt2TranTaxAmt:int = obj["Rpt2TranTaxAmt"]
      self.Rpt3BankRecGainLoss:int = obj["Rpt3BankRecGainLoss"]
      self.Rpt3DiscountAmt:int = obj["Rpt3DiscountAmt"]
      self.Rpt3GainLossReal:int = obj["Rpt3GainLossReal"]
      self.Rpt3GainLossUnreal:int = obj["Rpt3GainLossUnreal"]
      self.Rpt3Receipt:int = obj["Rpt3Receipt"]
      self.Rpt3TranTaxAmt:int = obj["Rpt3TranTaxAmt"]
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.StatusChgLegalNum:str = obj["StatusChgLegalNum"]
      self.StatusChgTranDocType:str = obj["StatusChgTranDocType"]
      self.TermsDesc:str = obj["TermsDesc"]
      self.TotalCashReceived:int = obj["TotalCashReceived"]
      self.TotalRoundDiff:int = obj["TotalRoundDiff"]
      self.TranTaxAmt:int = obj["TranTaxAmt"]
      self.TypeDesc:str = obj["TypeDesc"]
      self.XRateLabel:str = obj["XRateLabel"]
      self.BankTotalAmount:int = obj["BankTotalAmount"]
      self.BaseCurrencyCode:str = obj["BaseCurrencyCode"]
      self.BaseCurrencyDesc:str = obj["BaseCurrencyDesc"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.BillToName:str = obj["BillToName"]
      self.DocDiscountedAmt:int = obj["DocDiscountedAmt"]
      self.ARPNDtlExists:bool = obj["ARPNDtlExists"]
      """  for kinetic purposes  """  
      self.ARPNDtlInvoicePosted:bool = obj["ARPNDtlInvoicePosted"]
      """  for kinetic purposes  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctDescription:str = obj["BankAcctDescription"]
      self.BankAcctBankName:str = obj["BankAcctBankName"]
      self.CashbookLineDescription:str = obj["CashbookLineDescription"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CustNumInactive:bool = obj["CustNumInactive"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.PIStatusStatusDesc:str = obj["PIStatusStatusDesc"]
      self.PITypeDescription:str = obj["PITypeDescription"]
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ARPNHeadTGLCRow:
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
      self.HeadNum:int = obj["HeadNum"]
      """  HeadNum of ARPNHead  """  
      self.GroupID:str = obj["GroupID"]
      """  GroupID of ARPNHead  """  
      self.BitFlag:int = obj["BitFlag"]
      self.COADescription:str = obj["COADescription"]
      self.GLAccountGLAcctDisp:str = obj["GLAccountGLAcctDisp"]
      self.GLAccountAccountDesc:str = obj["GLAccountAccountDesc"]
      self.GLAccountGLShortAcct:str = obj["GLAccountGLShortAcct"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ARPNListRow:
   def __init__(self, obj):
      self.ARPromNoteID:str = obj["ARPromNoteID"]
      self.Company:str = obj["Company"]
      self.CurGroupID:str = obj["CurGroupID"]
      self.CustID:str = obj["CustID"]
      self.GroupID:str = obj["GroupID"]
      self.HeadNum:int = obj["HeadNum"]
      self.PIStage:str = obj["PIStage"]
      self.PIStatus:str = obj["PIStatus"]
      self.TranAmt:int = obj["TranAmt"]
      self.Type:str = obj["Type"]
      self.Selected:bool = obj["Selected"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ARPNMoveRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  An integer automatically assigned by the system using the database sequence called "CheckHedSeq". Which along with company and GroupID creates a unique key for the record. This is for internal control only the user never needs to reference.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing invoices to be entered, the user establishes a Group ID. All invoices belong to a group until the group is posted. The Group ID is assigned by the user.  The Group ID is used to selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  """  
      self.Seq:int = obj["Seq"]
      """  Movement Order  """  
      self.CurGroupID:str = obj["CurGroupID"]
      """  Current Group ID  """  
      self.PIStatus:str = obj["PIStatus"]
      """  Status  """  
      self.PIStage:str = obj["PIStage"]
      """  Stage  """  
      self.Posted:bool = obj["Posted"]
      """  Posted  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Date created  """  
      self.CreateUser:str = obj["CreateUser"]
      """  Created By User  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.Type:str = obj["Type"]
      """  Move Type  """  
      self.Comment:str = obj["Comment"]
      """  Comment  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction Date  """  
      self.CreateTime:int = obj["CreateTime"]
      """  Creation Time  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type for the record.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EndorsedAPPNGroupID:str = obj["EndorsedAPPNGroupID"]
      """  Reference to Endorsed AP PI GroupID.  """  
      self.EndorsedAPPNHeadNum:int = obj["EndorsedAPPNHeadNum"]
      """  Reference to Endorsed AP PI HeadNum.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.PIStatusDesc:str = obj["PIStatusDesc"]
      """  PI status description  """  
      self.PostErrMess:str = obj["PostErrMess"]
      """  Posting Error Message  """  
      self.PostToGL:bool = obj["PostToGL"]
      """  Indicates if posting GL transactions.  """  
      self.TypeDesc:str = obj["TypeDesc"]
      """  PI Type description  """  
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.LegalNumStyle:str = obj["LegalNumStyle"]
      """  Indicates if the legal number is manually generated or system generated  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ARPNMoveTableset:
   def __init__(self, obj):
      self.ARPNMove:list[Erp_Tablesets_ARPNMoveRow] = obj["ARPNMove"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ARPromissoryNotesTableset:
   def __init__(self, obj):
      self.ARPNHead:list[Erp_Tablesets_ARPNHeadRow] = obj["ARPNHead"]
      self.ARPNHeadAttch:list[Erp_Tablesets_ARPNHeadAttchRow] = obj["ARPNHeadAttch"]
      self.BankTran:list[Erp_Tablesets_BankTranRow] = obj["BankTran"]
      self.BankTranTaxDtl:list[Erp_Tablesets_BankTranTaxDtlRow] = obj["BankTranTaxDtl"]
      self.BankTranTGLC:list[Erp_Tablesets_BankTranTGLCRow] = obj["BankTranTGLC"]
      self.ARPNDtl:list[Erp_Tablesets_ARPNDtlRow] = obj["ARPNDtl"]
      self.TaxDtl:list[Erp_Tablesets_TaxDtlRow] = obj["TaxDtl"]
      self.ARPNHeadTGLC:list[Erp_Tablesets_ARPNHeadTGLCRow] = obj["ARPNHeadTGLC"]
      self.ARPNList:list[Erp_Tablesets_ARPNListRow] = obj["ARPNList"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_BankTranRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Relates record to a BankAcct.  """  
      self.TranNum:int = obj["TranNum"]
      """  Unique ID of the Transaction.  """  
      self.TranDate:str = obj["TranDate"]
      """  Date that the transaction took place.  """  
      self.TranAmt:int = obj["TranAmt"]
      """  Amount of the Transaction  """  
      self.TranRef:str = obj["TranRef"]
      """  Transaction Reference  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Indicates that the Transaction (not cleared variance) has been posted to G/L.  When the Bank Statement is posted all Non-G/L Posted adjustments for the bank are posted to G/L using the Bank Account's Cash and Bank Fee Accounts. G/L Posted Transactions cannot be deleted. (System Set)  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  Person who entered the transaction (System Set).  """  
      self.EntryDate:str = obj["EntryDate"]
      """  Date that the Transaction was entered into the system (System Set).  """  
      self.EntryTime:str = obj["EntryTime"]
      """  Time that the transaction was entered into the system - in HH:MM:SS format (System Set).  """  
      self.TranCleared:bool = obj["TranCleared"]
      """  Indicates the transaction's cleared status.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.TranClearPending:bool = obj["TranClearPending"]
      """  Indicates that the transaction is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.TranClearedAmt:int = obj["TranClearedAmt"]
      """  Amount that the Transaction was cleared for.  """  
      self.TranClearedPerson:str = obj["TranClearedPerson"]
      """  Person who cleared the transaction (System Set).  """  
      self.TranClearedDate:str = obj["TranClearedDate"]
      """  Date that the Transaction was cleared in the system (System Set).  """  
      self.TranClearedTime:str = obj["TranClearedTime"]
      """  Time that the transaction was cleared in the system - in HH:MM:SS format (System Set).  """  
      self.BankSlip:str = obj["BankSlip"]
      """  The identifier of the Bank Slip document (bank statement) on which this transaction was cleared by the bank. This is updated via the bank reconciliation process.  This is also written to the related GLJrnDtl records.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal year that entry applies to.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period the transaction was posted to. Only pertains to when posted to GL.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  Journal Number of related GLJrnDtl.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Journal Code of the related GLJrnDtl.  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """  Document amount of the Transaction  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange rate that is used for this bank transaction.  """  
      self.DocTranClearedAmt:int = obj["DocTranClearedAmt"]
      """  Document amount that the Transaction was cleared for.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry "group" that the transaction is assigned to.  All transactions belong to a "Group."  It is assigned to the record during creation using the "current group" that the user is signed into.  It cannot be changed.  The GroupID is used to selectively print and post the transactions.  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  This field identifies a bankslip.  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  This field identifies a line of a bankslip.  """  
      self.GLRefType:str = obj["GLRefType"]
      """  Link to the related GLRefTyp.RefType.  """  
      self.GLRefCode:str = obj["GLRefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.GLRefCodeDesc:str = obj["GLRefCodeDesc"]
      """  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TranClearedAmt:int = obj["Rpt1TranClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TranClearedAmt:int = obj["Rpt2TranClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TranClearedAmt:int = obj["Rpt3TranClearedAmt"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix that entry applies to.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.BankFeeID:str = obj["BankFeeID"]
      """  Unique ID of the Fee  """  
      self.BankFeeAmt:int = obj["BankFeeAmt"]
      """  The Fee amount; this amount plus the Fee tax amount will compose the total of the charge on the statement  """  
      self.BankFeeTaxAmt:int = obj["BankFeeTaxAmt"]
      """  The Tax Amount that has been charged to the fee  """  
      self.DocBankFeeAmt:int = obj["DocBankFeeAmt"]
      """  The Fee amount in Base Currency  """  
      self.DocBankFeeTaxAmt:int = obj["DocBankFeeTaxAmt"]
      """  The Tax Amount that has been charged to the fee in Base Currency  """  
      self.Rpt1BankFeeAmt:int = obj["Rpt1BankFeeAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2BankFeeAmt:int = obj["Rpt2BankFeeAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3BankFeeAmt:int = obj["Rpt3BankFeeAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1BankFeeTaxAmt:int = obj["Rpt1BankFeeTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2BankFeeTaxAmt:int = obj["Rpt2BankFeeTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3BankFeeTaxAmt:int = obj["Rpt3BankFeeTaxAmt"]
      """  Reporting currency value of this field  """  
      self.SourceModule:str = obj["SourceModule"]
      """   Used for Bank Fee Functionality, indicates the module that created this BankFee.  This is assigned by the system.
Values can be; AR, AP and BA.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  Consecutive from the AP and AR transactions, this field is used to identify the AP or AR transaction that created this Bank Fee  """  
      self.Voided:bool = obj["Voided"]
      """  Indiates if the BankTran has been voided.  The TranNum field will be the same as the original transaction  """  
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
      """  Bank Balance at the time of revaluation  """  
      self.DocRevalueBal:int = obj["DocRevalueBal"]
      """  Document currency Bank Balance at the time of revaluation  """  
      self.Rpt1RevalueBal:int = obj["Rpt1RevalueBal"]
      """  Reporting currency Bank Balance at the time of revaluation  """  
      self.Rpt2RevalueBal:int = obj["Rpt2RevalueBal"]
      """  Reporting currency Bank Balance at the time of revaluation  """  
      self.Rpt3RevalueBal:int = obj["Rpt3RevalueBal"]
      """  Reporting currency Bank Balance at the time of revaluation  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number for the record.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document for the record.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CNCFICode:str = obj["CNCFICode"]
      """  CNCFICode  """  
      self.CNToCFICode:str = obj["CNToCFICode"]
      """  CNToCFICode  """  
      self.BankRecGainLoss:int = obj["BankRecGainLoss"]
      """  BankRecGainLoss  """  
      self.Rpt1BankRecGainLoss:int = obj["Rpt1BankRecGainLoss"]
      """  Rpt1BankRecGainLoss  """  
      self.Rpt2BankRecGainLoss:int = obj["Rpt2BankRecGainLoss"]
      """  Rpt2BankRecGainLoss  """  
      self.Rpt3BankRecGainLoss:int = obj["Rpt3BankRecGainLoss"]
      """  Rpt3BankRecGainLoss  """  
      self.BalanceUpdated:int = obj["BalanceUpdated"]
      """  BalanceUpdated  """  
      self.DocBankRecGainLoss:int = obj["DocBankRecGainLoss"]
      """  DocBankRecGainLoss  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.BankBatchExcluded:bool = obj["BankBatchExcluded"]
      """  Indicates that transaction is currently excluded from batch in Bank Statement Processing.  """  
      self.BankBatchSysRowID:str = obj["BankBatchSysRowID"]
      """  BankBatchSysRowID  """  
      self.ABTUID:str = obj["ABTUID"]
      """  ABTUID  """  
      self.Plant:str = obj["Plant"]
      """  Multi-Site related Site  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for BASE  """  
      self.CNCFICodeDescription:str = obj["CNCFICodeDescription"]
      self.CRCurrCode:str = obj["CRCurrCode"]
      """  Cash Receipt currency code  """  
      self.CRRateGrpCode:str = obj["CRRateGrpCode"]
      """  Cash Receipt Rate group code  """  
      self.CRTranAmt:int = obj["CRTranAmt"]
      """  Cash Receipt Tran amount  """  
      self.CRTranClearedAmt:int = obj["CRTranClearedAmt"]
      """  Cash Receipt Transaction Cleared Amount  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      """  Currency Switch  """  
      self.DisableBankAmt:bool = obj["DisableBankAmt"]
      """   The flag to indicate if BankClearedAmt is not available to make changes.
(If Bank currency equals transaction currency this flag is true)  """  
      self.DispAmtReverse:bool = obj["DispAmtReverse"]
      """  The flag to indicate if the Display amount is supposed to be reversed  """  
      self.DispDocTranAmt:int = obj["DispDocTranAmt"]
      self.DispDocTranClearedAmt:int = obj["DispDocTranClearedAmt"]
      self.DispTranAmt:int = obj["DispTranAmt"]
      self.DispTranClearedAmt:int = obj["DispTranClearedAmt"]
      self.InternalDate:str = obj["InternalDate"]
      """  Used for tree structure/parent view definition in Petty Cash Entry  """  
      self.IsFiltered:bool = obj["IsFiltered"]
      self.IsLockedBankRec:bool = obj["IsLockedBankRec"]
      """  Indicates if the record is locked by review journal for bank reconciliation  """  
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.LegalNumStyle:str = obj["LegalNumStyle"]
      """  Indicates if the legal number is manually generated or system generated  """  
      self.RefCodeStatus:str = obj["RefCodeStatus"]
      """  Indicates if Reference Code is (M)andatory, (O)ptional, (E)xcluded or Blank.  Enable Reference Code if "M" or "O".  """  
      self.Rpt1DispTranAmt:int = obj["Rpt1DispTranAmt"]
      self.Rpt1DispTranClearedAmt:int = obj["Rpt1DispTranClearedAmt"]
      self.Rpt2DispTranAmt:int = obj["Rpt2DispTranAmt"]
      self.Rpt2DispTranClearedAmt:int = obj["Rpt2DispTranClearedAmt"]
      self.Rpt3DispTranAmt:int = obj["Rpt3DispTranAmt"]
      self.Rpt3DispTranClearedAmt:int = obj["Rpt3DispTranClearedAmt"]
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      self.GLAccount:str = obj["GLAccount"]
      """  Display GL Account  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      self.BankFeeIDDescription:str = obj["BankFeeIDDescription"]
      self.BankFeeIDTaxCode:str = obj["BankFeeIDTaxCode"]
      self.CashbookLineDescription:str = obj["CashbookLineDescription"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BankTranTGLCRow:
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
      """  GroupID for relation to BankTran  """  
      self.HeadNum:int = obj["HeadNum"]
      self.InternalDate:str = obj["InternalDate"]
      """  Used for tree structure/parent view definition in Petty Cash Entry  """  
      self.PCashDeskID:str = obj["PCashDeskID"]
      self.PCashRefNum:int = obj["PCashRefNum"]
      self.Voided:bool = obj["Voided"]
      """  Voided flag for relation to BankTran  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID for relation to BankTran  """  
      self.BitFlag:int = obj["BitFlag"]
      self.COADescription:str = obj["COADescription"]
      self.GLAccountGLShortAcct:str = obj["GLAccountGLShortAcct"]
      self.GLAccountGLAcctDisp:str = obj["GLAccountGLAcctDisp"]
      self.GLAccountAccountDesc:str = obj["GLAccountAccountDesc"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BankTranTaxDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SourceModule:str = obj["SourceModule"]
      """   Indicates the module that created this tax detail.  This is assigned by the system.
Values can be; AR, AP.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  HeadNum  """  
      self.APTranNo:int = obj["APTranNo"]
      """  Integer assigned by the system copied from APTran.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  Taxable amount for this invoice. Manually entered if the currency is the base currency.  """  
      self.DocTaxableAmt:int = obj["DocTaxableAmt"]
      """  Taxable amount for this invoice in foreign currency. Manually entered.  """  
      self.Percent:int = obj["Percent"]
      """  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount. Manually entered if the currency is the base currency.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount in foreign currency. Manually entered.  """  
      self.ReverseCharge:bool = obj["ReverseCharge"]
      """  Reverse Charge.  """  
      self.Rpt1TaxableAmt:int = obj["Rpt1TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxableAmt:int = obj["Rpt2TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxableAmt:int = obj["Rpt3TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.RateCode:str = obj["RateCode"]
      """  Rate Code  """  
      self.CollectionType:int = obj["CollectionType"]
      """  Collection Type  """  
      self.Timing:int = obj["Timing"]
      """  Timing of when to report taxes  """  
      self.ExemptType:int = obj["ExemptType"]
      """  Exemption Type  """  
      self.ExemptPercent:int = obj["ExemptPercent"]
      """  Exemption Percent  """  
      self.ResolutionNum:str = obj["ResolutionNum"]
      """  Resolution Number  """  
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
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  The open A/R invoice # that the transaction applies against. Not used by the MisPay trantype. In the case of PayInv, or CMemo transaction this must be a valid InvcHead record where InvcHead.CreditMemo = No. In case of "Adjust" transactions this can be either a invoice or a credit memo reference. Note: The "Apply Credit Memo" program automatically creates an additional CashDtl records for each invoice to which the credit memo is applied.  In this additional record this field contains the credit memo's number.  """  
      self.InvoiceRef:int = obj["InvoiceRef"]
      """  Applicable to CMemo transaction types only. The "Apply Credit Memo" program creates two CashDtl records for each invoice that a credit memo is applied to. One record for the <credit> to the invoice and a second record for the debit to the credit memo. In the first record this field is the InvoiceNum of the Credit memo. In the second record it is the InvoiceNum of the invoice that the credit memo was applied to.  """  
      self.ECAcquisitionSeq:int = obj["ECAcquisitionSeq"]
      """   Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.
NOTE:  This field is now used in VAT Reverse Charge logic.  If an invoice line is marked for Reverse Charge, a second line is created just like in the ECAcquisition logic. To distinguish the two scenarios, the ReverseCharge flag will be set to true if the second line is for Reverse Charge.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Relates record to a BankAcct.  """  
      self.TranNum:int = obj["TranNum"]
      """  Unique ID of the Transaction.  """  
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
      self.Manual:bool = obj["Manual"]
      """  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  """  
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
      self.DiscTaxAdj:int = obj["DiscTaxAdj"]
      """  Discount Tax Adjustment  """  
      self.DocDiscTaxAdj:int = obj["DocDiscTaxAdj"]
      """  Discount Tax Adjustment in foreign currency.  """  
      self.Rpt1DiscTaxAdj:int = obj["Rpt1DiscTaxAdj"]
      """  Reporting currency value of this field  """  
      self.Rpt2DiscTaxAdj:int = obj["Rpt2DiscTaxAdj"]
      """  Reporting currency value of this field  """  
      self.Rpt3DiscTaxAdj:int = obj["Rpt3DiscTaxAdj"]
      """  Reporting currency value of this field  """  
      self.DiscTaxableAdj:int = obj["DiscTaxableAdj"]
      """  Discount Taxable Adjustment  """  
      self.DocDiscTaxableAdj:int = obj["DocDiscTaxableAdj"]
      """  Discount Taxable Adjustment in foreign currency.  """  
      self.Rpt1DiscTaxableAdj:int = obj["Rpt1DiscTaxableAdj"]
      """  Reporting currency value of this field  """  
      self.Rpt2DiscTaxableAdj:int = obj["Rpt2DiscTaxableAdj"]
      """  Reporting currency value of this field  """  
      self.Rpt3DiscTaxableAdj:int = obj["Rpt3DiscTaxableAdj"]
      """  Reporting currency value of this field  """  
      self.TextCode:str = obj["TextCode"]
      """  Unique Identifier for Legal Text  """  
      self.Voided:bool = obj["Voided"]
      """  Indicates if transaction was voided.  The rest of the unique key will contain the original transaction values (like APTran)  """  
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
      self.DiscTaxAdjVar:int = obj["DiscTaxAdjVar"]
      """  Discount Tax Adjustment Variance  """  
      self.DocDiscTaxAdjVar:int = obj["DocDiscTaxAdjVar"]
      """  Discount Tax Adjustment Variance  """  
      self.Rpt1DiscTaxAdjVar:int = obj["Rpt1DiscTaxAdjVar"]
      """  Reporting currency value of this field  """  
      self.Rpt2DiscTaxAdjVar:int = obj["Rpt2DiscTaxAdjVar"]
      """  Reporting currency value of this field  """  
      self.Rpt3DiscTaxAdjVar:int = obj["Rpt3DiscTaxAdjVar"]
      """  Reporting currency value of this field  """  
      self.PCashDeskID:str = obj["PCashDeskID"]
      """  Unique identifier of Petty Cash Desk  """  
      self.PCashRefNum:int = obj["PCashRefNum"]
      """  Reference Number, unique identifier of Petty Cash Document  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AGOrigTaxableAmt:int = obj["AGOrigTaxableAmt"]
      """  AGOrigTaxableAmt  """  
      self.GainLoss:int = obj["GainLoss"]
      """  GainLoss  """  
      self.DocGainLoss:int = obj["DocGainLoss"]
      """  DocGainLoss  """  
      self.Rpt1GainLoss:int = obj["Rpt1GainLoss"]
      """  Rpt1GainLoss  """  
      self.Rpt2GainLoss:int = obj["Rpt2GainLoss"]
      """  Rpt2GainLoss  """  
      self.Rpt3GainLoss:int = obj["Rpt3GainLoss"]
      """  Rpt3GainLoss  """  
      self.CNCFICode:str = obj["CNCFICode"]
      """  CNCFICode  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  APInvoiceNum  """  
      self.TranType:str = obj["TranType"]
      """  TranType  """  
      self.MovementNum:int = obj["MovementNum"]
      """  MovementNum  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.CNCFICodeDescription:str = obj["CNCFICodeDescription"]
      self.CTDescription:str = obj["CTDescription"]
      self.DisableManual:bool = obj["DisableManual"]
      """  Flag to indicate if Manual checkbox should be disabled  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry "group" that the transaction is assigned to.  All transactions belong to a "Group."  It is assigned to the record during creation using the "current group" that the user is signed into.  It cannot be changed.  The GroupID is used to selectively print and post the transactions.  """  
      self.InternalDate:str = obj["InternalDate"]
      """  Used for tree structure/parent view definition in Petty Cash Entry  """  
      self.IsFiltered:bool = obj["IsFiltered"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.BitFlag:int = obj["BitFlag"]
      self.RateCodeDescription:str = obj["RateCodeDescription"]
      self.TaxCodeDescription:str = obj["TaxCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLJrnDtlMovTableset:
   def __init__(self, obj):
      self.GLJrnDtl:list[Erp_Tablesets_GLJrnDtlRow] = obj["GLJrnDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_GLJrnDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal year that entry applies to.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  Number that is assigned by the system. The Journal number is a way of relating the detail entries into a group that would normally balance.  The system assigns this number by finding  the journalnum of the last record for the fiscal year and adding one.  """  
      self.JournalLine:int = obj["JournalLine"]
      """  A system assigned number to which is used along with the company, FiscalYear and JournalNum to uniquely identify the record.  System determines number by reading last record for a specific Company/FiscalYear/JournalNum combination and adding 1.  """  
      self.Description:str = obj["Description"]
      """  Describes the journal transaction. Defaulted from GLJrnHed in journal entry program.  """  
      self.JEDate:str = obj["JEDate"]
      """  Date for this journal transaction entry.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period that this journal entry applies to.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry Group that the journal entry is assigned to. This field is not directly maintainable, it is assigned by the entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  """  
      self.PostedBy:str = obj["PostedBy"]
      """  User ID that posted this translation.  """  
      self.PostedDate:str = obj["PostedDate"]
      """  Date that this transaction was posted to the G/L files.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates if this entry has been posted to the G/L master balance files. Unposted entries are excluded from all G/L reports.  """  
      self.SourceModule:str = obj["SourceModule"]
      """   Indicates the module that created this journal entry.  This is assigned by the system.
Values can be; AR, AP, GL, PR.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  Vendor's invoice number.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  """  
      self.ARInvoiceNum:int = obj["ARInvoiceNum"]
      """  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctId of the BankAcct master that this check was drawn  against.  """  
      self.CheckNum:int = obj["CheckNum"]
      """  Check number.  """  
      self.CRHeadNum:int = obj["CRHeadNum"]
      """  Cash Receipts reference field.  """  
      self.Reverse:bool = obj["Reverse"]
      """  Indicates that the transaction is a reversing entry created during the journal entry post for GLJrnHed transactions when flagged as Reverse = YES.  """  
      self.BankTranNum:int = obj["BankTranNum"]
      """  Bank Transaction Number.  Used when a transaction is a direct transfer from one bank account to another.  """  
      self.BankSlip:str = obj["BankSlip"]
      """   The identifier of the Bank Slip document (bank statement).  The user enters a bank slip during the reconciliation process.  This is then written into the related GLJrnDtl records.
Pertains to transactions related to a bank (checks, receipts, transfers, adjustments)  """  
      self.RefType:str = obj["RefType"]
      """  Link to the related GLRefTyp.RefType.  """  
      self.RefCode:str = obj["RefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.ExtRefType:str = obj["ExtRefType"]
      """  Multi-Company G/L Reference Type from the external company.  This is used by the Multi-Company Journal.  """  
      self.ExtRefCode:str = obj["ExtRefCode"]
      """  Multi-Company G/L Reference Code from the external company.  This is used by the Multi-Company Journal.  """  
      self.GlbJournalNum:int = obj["GlbJournalNum"]
      """  The Journal Number assigned at the destination or target company when this Multi-Company Journal is created.  """  
      self.GlbJournalLine:int = obj["GlbJournalLine"]
      """  The Journal Line assigned at the destination or target company when this Multi-Company Journal is created.  """  
      self.GlbJournalCode:str = obj["GlbJournalCode"]
      """  Journal Code used by the Multi-Company Journal when it gets created at the target external company.  """  
      self.GlbVendorNum:int = obj["GlbVendorNum"]
      """  Global Vendor number.  Used by Multi-Company Journal.  """  
      self.GlbAPInvoiceNum:str = obj["GlbAPInvoiceNum"]
      """  Global AP Invoice identifier.  Used by Multi-Company Journal.  """  
      self.MultiCompany:bool = obj["MultiCompany"]
      """  Flag to indicate that a separate journal entry will be created at the target company for the Multi-Company G/L Account entered in this journal line.  """  
      self.Linked:bool = obj["Linked"]
      """  Linked to a Multi-Company Journal.  """  
      self.CommentText:str = obj["CommentText"]
      """  Extended text to describe the journal line entry.  Defaults from GLJrnHed.CommentText.  """  
      self.GlbCompanyID:str = obj["GlbCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.GlbFiscalYear:int = obj["GlbFiscalYear"]
      """  The fiscal year for this journal transaction header from the external company. Assigned from GLJrnGrp.FiscalYear.  """  
      self.GlbFiscalPeriod:int = obj["GlbFiscalPeriod"]
      """  Fiscal period from the external company that this journal entry applies to.  """  
      self.GlbGroupID:str = obj["GlbGroupID"]
      """  The data entry Group from the external company that the journal entry is assigned to.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  """  
      self.SegValue1:str = obj["SegValue1"]
      """  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  """  
      self.SegValue2:str = obj["SegValue2"]
      """  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  """  
      self.SegValue3:str = obj["SegValue3"]
      """  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.SegValue4:str = obj["SegValue4"]
      """  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.SegValue5:str = obj["SegValue5"]
      """  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.SegValue6:str = obj["SegValue6"]
      """  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  """  
      self.SegValue7:str = obj["SegValue7"]
      """  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.SegValue8:str = obj["SegValue8"]
      """  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.SegValue9:str = obj["SegValue9"]
      """  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.SegValue10:str = obj["SegValue10"]
      """  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.SegValue11:str = obj["SegValue11"]
      """  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.SegValue12:str = obj["SegValue12"]
      """  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.SegValue13:str = obj["SegValue13"]
      """  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.SegValue14:str = obj["SegValue14"]
      """  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.SegValue15:str = obj["SegValue15"]
      """  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.SegValue16:str = obj["SegValue16"]
      """  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.SegValue17:str = obj["SegValue17"]
      """  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.SegValue18:str = obj["SegValue18"]
      """  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.SegValue19:str = obj["SegValue19"]
      """  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.SegValue20:str = obj["SegValue20"]
      """  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.ExtGLAccount:str = obj["ExtGLAccount"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  """  
      self.ExtSegValue1:str = obj["ExtSegValue1"]
      """  External Segment Value 1  """  
      self.ExtSegValue2:str = obj["ExtSegValue2"]
      """  External Segment Value 2  """  
      self.ExtSegValue3:str = obj["ExtSegValue3"]
      """  External Segment Value 3  """  
      self.ExtSegValue4:str = obj["ExtSegValue4"]
      """  External Segment Value 4  """  
      self.ExtSegValue5:str = obj["ExtSegValue5"]
      """  External Segment Value 5  """  
      self.ExtSegValue6:str = obj["ExtSegValue6"]
      """  External Segment Value 6  """  
      self.ExtSegValue7:str = obj["ExtSegValue7"]
      """  External Segment Value 7  """  
      self.ExtSegValue8:str = obj["ExtSegValue8"]
      """  External Segment Value 8  """  
      self.ExtSegValue9:str = obj["ExtSegValue9"]
      """  External Segment Value 9  """  
      self.ExtSegValue10:str = obj["ExtSegValue10"]
      """  External Segment Value 10  """  
      self.ExtSegValue11:str = obj["ExtSegValue11"]
      """  External Segment Value 11  """  
      self.ExtSegValue12:str = obj["ExtSegValue12"]
      """  External Segment Value 12  """  
      self.ExtSegValue13:str = obj["ExtSegValue13"]
      """  External Segment Value 13  """  
      self.ExtSegValue14:str = obj["ExtSegValue14"]
      """  External Segment Value 14  """  
      self.ExtSegValue15:str = obj["ExtSegValue15"]
      """  External Segment Value 15  """  
      self.ExtSegValue16:str = obj["ExtSegValue16"]
      """  External Segment Value 16  """  
      self.ExtSegValue17:str = obj["ExtSegValue17"]
      """  External Segment Value 17  """  
      self.ExtSegValue18:str = obj["ExtSegValue18"]
      """  External Segment Value 18  """  
      self.ExtSegValue19:str = obj["ExtSegValue19"]
      """  External Segment Value 19  """  
      self.ExtSegValue20:str = obj["ExtSegValue20"]
      """  External Segment Value 20  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Date record was created  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the document currency.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number of source document  """  
      self.PerBalFlag:bool = obj["PerBalFlag"]
      """  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  """  
      self.TBFlag:bool = obj["TBFlag"]
      """  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  """  
      self.DailyBalFlag:bool = obj["DailyBalFlag"]
      """  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.GlbFiscalYearSuffix:str = obj["GlbFiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.GlbFiscalCalendarID:str = obj["GlbFiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.IntermediateProc:bool = obj["IntermediateProc"]
      """  Identifies the journal entry as one processed by consolidation posting mode where the data transfer is immediate and an intermediate book is used.  """  
      self.GenID:int = obj["GenID"]
      """  Internal system calculated sequence number not inteneded for external use.  """  
      self.SrcCompany:str = obj["SrcCompany"]
      """  Source Company Identifier.  Identifies the company where this GLJrnDtl originated from.  """  
      self.SrcBook:str = obj["SrcBook"]
      """  Unique Book Identifier  This is the book that is being consolidated into a target book.  """  
      self.SrcGLAccount:str = obj["SrcGLAccount"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  """  
      self.SrcJrnlCode:str = obj["SrcJrnlCode"]
      """  Source Journal Code  """  
      self.SrcJournalNum:int = obj["SrcJournalNum"]
      """  Source Journal Number  """  
      self.SrcJournalLine:int = obj["SrcJournalLine"]
      """  Source Journal Line  """  
      self.SrcType:str = obj["SrcType"]
      """   P = derived from Periodic Consolidation.
C = derived from GLJrnDtl via Continuous Consolidation.
A = derived from Advanced Allocations.  """  
      self.ABTUID:str = obj["ABTUID"]
      """  this field equas ABTUID which was created during posting  """  
      self.DebitAmount:int = obj["DebitAmount"]
      """  This field shows Debit value of transaction  """  
      self.CreditAmount:int = obj["CreditAmount"]
      """  This field shows Credit value of transaction  """  
      self.BookDebitAmount:int = obj["BookDebitAmount"]
      """  This field shows Debit value of transaction recalculated from DebitAmount according to Currency of mentioned Book  """  
      self.BookCreditAmount:int = obj["BookCreditAmount"]
      """  This field shows Credit value of transaction recalculated from CreditAmount according to Currency of mentioned Book  """  
      self.ParentRUID:str = obj["ParentRUID"]
      """  If the current line is reversal, then this field is used for link with original journal line. It equals SysRowID of original line.  """  
      self.HasReverseLine:bool = obj["HasReverseLine"]
      """  if has reverse line  """  
      self.BalanceAcct:str = obj["BalanceAcct"]
      """  This is the resolved balance account the period balance, currency balance and/or daily balance records were written under for this GL Journal Detail GL Account.  """  
      self.TrialAcct:str = obj["TrialAcct"]
      """  This is the resolved balance account the trial balance records were written under for this GL Journal Detail GL Account.  """  
      self.CorrAccUID:int = obj["CorrAccUID"]
      """  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  """  
      self.AllocationStamp:str = obj["AllocationStamp"]
      """  This is the last allocation stamp that affected this GLJrnDtl.  """  
      self.BatchID:str = obj["BatchID"]
      """  Identifies the allocation batch this journal entry was processed under.  """  
      self.AllocID:str = obj["AllocID"]
      """  This is the allocation id that processed this journal entry.  """  
      self.RunNbr:int = obj["RunNbr"]
      """  The allocation run number is a unique sequential number that identifies which run of an allocation batch this journal entry was created under.  """  
      self.AllocRunNbr:int = obj["AllocRunNbr"]
      """  Intended for internal use only.  Updated by the Advanced Allocations Engine.  This identifies the last allocation run number that used this GLJrnDtl as a source record.  """  
      self.AllocTgtNbr:int = obj["AllocTgtNbr"]
      """  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  """  
      self.AllocTgtSeq:int = obj["AllocTgtSeq"]
      """  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  """  
      self.ExtCOACode:str = obj["ExtCOACode"]
      """  External COA Code  """  
      self.MatchCode:str = obj["MatchCode"]
      """  MatchCode is used to match two or more journal detail records together.  """  
      self.MatchDate:str = obj["MatchDate"]
      """  MatchDate is set when the journal detail record is matched to other journal detail records.  """  
      self.Reconciled:bool = obj["Reconciled"]
      """  Indicates whether or not the transaction has been flagged as reconciled.  """  
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
      self.PaymentNumber:str = obj["PaymentNumber"]
      """  PaymentNumber  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Sequence:int = obj["Sequence"]
      """  Journal Sequence Number  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type  """  
      self.CustNum:int = obj["CustNum"]
      """  The Internal CustNum that ties back to the Customer master file.  """  
      self.CloseFiscalPeriod:int = obj["CloseFiscalPeriod"]
      """  CloseFiscalPeriod  """  
      self.SourcePlant:str = obj["SourcePlant"]
      """  SourcePlant  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.ExtSysType:str = obj["ExtSysType"]
      """  Used for integrations - system type for URL specified in ExtSysURL - B = BisTrack / L = LumberTrack / F = FiberTrack / blank = Building Supply  """  
      self.ExtSysURL:str = obj["ExtSysURL"]
      """  URL for drill back to an integrated external system  """  
      self.COOneTimeDesc:str = obj["COOneTimeDesc"]
      """   Colombia Loc field            
This field is used as external calculated only.  """  
      self.COOneTimeID:str = obj["COOneTimeID"]
      """   Colombia Loc field.           
This field is used as external calculated only.  """  
      self.DEACodeDesc:str = obj["DEACodeDesc"]
      """  DEA Code  """  
      self.DEAEndDate:str = obj["DEAEndDate"]
      """  DEA End Date  """  
      self.DEAStartDate:str = obj["DEAStartDate"]
      """  DEA Start Date  """  
      self.DeferredExp:bool = obj["DeferredExp"]
      """  Deferred Expense  """  
      self.Distributed:int = obj["Distributed"]
      """  DEA Distributed Amount  """  
      self.DocDistributed:int = obj["DocDistributed"]
      """  DEA Distributed Amount in Doc Currency  """  
      self.DocExpense:int = obj["DocExpense"]
      """  DEA Expense Amount in Doc Currency  """  
      self.DocRecognized:int = obj["DocRecognized"]
      """  DEA Recognized Amount in Doc Currency  """  
      self.DocRemaining:int = obj["DocRemaining"]
      """  DEA Remaining Amount in Doc Currency  """  
      self.DocUnrecognized:int = obj["DocUnrecognized"]
      """  DEA Unrecognized Amount in Doc Currency  """  
      self.EnableMultiCompany:bool = obj["EnableMultiCompany"]
      """  Flag to indicate if the MultiCompany check box needs to be enabled.  """  
      self.Expense:int = obj["Expense"]
      """  DEA Expense Amount  """  
      self.ExtRefAcctChart:str = obj["ExtRefAcctChart"]
      self.ExtRefAcctDept:str = obj["ExtRefAcctDept"]
      self.ExtRefAcctDiv:str = obj["ExtRefAcctDiv"]
      self.ExtRefCodeStatus:str = obj["ExtRefCodeStatus"]
      self.GLAcctDisp:str = obj["GLAcctDisp"]
      self.HeaderCommentText:str = obj["HeaderCommentText"]
      """  External field used in Journal Tracker and Chart tracker. Journal Comments tab.  """  
      self.LineReference:str = obj["LineReference"]
      """  Manual GL Journal Line Reference.  """  
      self.LineReferenceHolder:str = obj["LineReferenceHolder"]
      """  Manual GL Journal Line Reference Holder.  """  
      self.LineReferenceHolderName:str = obj["LineReferenceHolderName"]
      """  Manual GL Journal Line Reference Holder Name.  """  
      self.LineReferenceType:str = obj["LineReferenceType"]
      """  Manual GL Journal Line Reference Type.  """  
      self.MovementNum:int = obj["MovementNum"]
      self.OrigApplyDate:str = obj["OrigApplyDate"]
      """  Apply Date of the Original Transaction  """  
      self.OrigJrnlLine:int = obj["OrigJrnlLine"]
      """  Journal line of the original transaction that was reversed.  """  
      self.OrigJrnlNbr:int = obj["OrigJrnlNbr"]
      """  Journal number of the original transaction that was reversed.  """  
      self.OrigJrnlYear:int = obj["OrigJrnlYear"]
      """  Fiscal year of the original transaction that was reversed.  """  
      self.OrigJrnlYearSuffix:str = obj["OrigJrnlYearSuffix"]
      """  Fiscal year suffix of the original transaction that was reversed.  """  
      self.Recognized:int = obj["Recognized"]
      """  DEA Recognized Amount  """  
      self.RefAcctChart:str = obj["RefAcctChart"]
      self.RefAcctDept:str = obj["RefAcctDept"]
      self.RefAcctDiv:str = obj["RefAcctDiv"]
      self.RefCodeStatus:str = obj["RefCodeStatus"]
      self.Remaining:int = obj["Remaining"]
      """  DEA Remaining Amount  """  
      self.RevApplyDate:str = obj["RevApplyDate"]
      """  Apply date of the reversing transaction  """  
      self.RevJrnlLine:int = obj["RevJrnlLine"]
      """  Journal line of the latest journal entry made to reverse a transaction.  """  
      self.RevJrnlNbr:int = obj["RevJrnlNbr"]
      """  Journal number of the latest journal entry made to reverse a transaction.  """  
      self.RevJrnlYear:int = obj["RevJrnlYear"]
      """  Fiscal year of the latest journal entry made to reverse a transaction.  """  
      self.RevJrnlYearSuffix:str = obj["RevJrnlYearSuffix"]
      """  Fiscal year suffix of the latest journal entry made to reverse a transaction.  """  
      self.StatAmount:int = obj["StatAmount"]
      self.TotCredit:int = obj["TotCredit"]
      self.TotDebit:int = obj["TotDebit"]
      self.Unrecognized:int = obj["Unrecognized"]
      """  DEA Unrecognized Amount  """  
      self.BookCurrencyCode:str = obj["BookCurrencyCode"]
      self.BookCurrencySymbol:str = obj["BookCurrencySymbol"]
      self.EntityDescription:str = obj["EntityDescription"]
      """  Description of the entity the journal detail is for  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      self.GLAccountGLAcctDisp:str = obj["GLAccountGLAcctDisp"]
      self.GLAccountAccountDesc:str = obj["GLAccountAccountDesc"]
      self.GLAccountGLAccount:str = obj["GLAccountGLAccount"]
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      self.SrcGLAccountGLShortAcct:str = obj["SrcGLAccountGLShortAcct"]
      self.SrcGLAccountAccountDesc:str = obj["SrcGLAccountAccountDesc"]
      self.SrcGLAccountGLAcctDisp:str = obj["SrcGLAccountGLAcctDisp"]
      self.StatUOMStatUOMDesc:str = obj["StatUOMStatUOMDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_InvcHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenInvoice:bool = obj["OpenInvoice"]
      """  Indicates if invoice is "open".  """  
      self.ClosedDate:str = obj["ClosedDate"]
      """  The latest transaction date (CashDtl) which was available when the invoice was closed. This is used to improve record selection performance when selecting invoices that were open as of a certain date. (Used by the aged invoice report). This is updated during the CashReceipt posting process, Adjustment entry or Apply Credit memos programs..  """  
      self.CreditMemo:bool = obj["CreditMemo"]
      """   Indicates the type of document. Yes = Credit Memo No= Invoice. This value can't be changed after the record has been created.
Credit memos affect the way detail quantities and amounts are stored in the database. They will always be stored with a negative sign but will entered as a positive.
Credit Memos created by invoice entry also set the InvoiceSuffix field = "CM"  """  
      self.UnappliedCash:bool = obj["UnappliedCash"]
      """  An internal flag that represents Credit Memo was due to Unapplied Receipts. Created by the Cash Receipts Entry program.   This is only applicable with CreditMemo = Yes.  """  
      self.CheckRef:str = obj["CheckRef"]
      """   The Check reference number that the Unapplied Receipt Credit Memo was created from. Cash receipts entry sets this field equal to the CashHead.CheckRef when it creates the Unapplied Receipt Credit Memo.  Primarily used as a reference.
This is used when TranType = PrePay, MisPay or PayInv.  """  
      self.InvoiceSuffix:str = obj["InvoiceSuffix"]
      """  An internally assigned field that further identifies an invoice. This field will be displayed as a suffix to the invoice number.  The possible values are "CM" = Credit memo created by invoice entry, UR = Unapplied Receipt Credit Memo,  DN = Debit Note, and FC = Finance Charge invoice.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group that the invoice was associated with  during the data entry process. This field is not directly maintainable, it is assigned by the invoice entry program using the BatchID of the "current " batch that the user is working with.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates if this invoice has been Posted to the receivables file.    Only invoices that have been Posted (true) will be included as part of the open receivables, that is they will not appear on reports or inquiries other than those used within invoice entry. Otherwise they are considered as still being in data entry. This field is always "no" when the invoice is created. It is set to "yes"  by the  "Post function". Once an invoice is posted it can't be maintained via data entry.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  """  
      self.InvoiceType:str = obj["InvoiceType"]
      """  There are four types of invoices:  "Shp" = Invoice for Shipment, "Adv" = Advanced Billing, "Dep" = For Deposit Payments, "Mis" = Miscellaneous.  The setting of this field affects invoice entry:  "Shipments" - These are generated by the "Get Shipments function" and is not selectable directly by the user.  "Advanced"  - Must have a sales order reference. The detail lines on this type of invoice update the OrderDtl.AdvanceBillBal. Also the user indicates if this should be considered as deferred revenue. Which changes which G/L accounts are used for the line item credits.  "Deposit" - invoices are used to request a "deposit" on an order. A Sales Order is mandatory. No line items or Miscellaneous records are allowed. The user enters a flat amount on the header (InvcHead.PrePayAmt) which will be printed in the body of the invoice. This also updates the OrderHed.PrePayBal field.   "Miscellaneous" - These invoices may or may not reference a Sales Order.  If Invoice is generated in Project Billing then there are following options: "PFF" - Fixed Fee project;  "PCP" - Cost Plus project;  "PTM" - Time and Material project;  "PPP" - Progress Payment project.  """  
      self.DeferredRevenue:bool = obj["DeferredRevenue"]
      """  Only used when InvoiceType = "Adv" (Advanced Billing).  Indicates if the detail line amounts are to be considered as sales or deferred revenue.  If "No" then the G/L accounts on the detail lines are the Sales Accounts otherwise they will be set to the Deferred Revenue accounts established in the ARSyst/ARAcct files.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Sales Order #. This is a mandatory entry for all InvoiceType except "Miscellaneous". If entered it must be valid in the OrderHed file. The OrderHed supplies the invoice with many defaults, including; CustNum, PONum, TermsCode,  FOB, RepRate, RepSplit, SalesRepList, InvoiceComments  """  
      self.CustNum:int = obj["CustNum"]
      """  The CustNum field is the internal # that is used to link the invoice to the Customer master file.  This field is not directly maintained by the user.  In most cases it will be duplicated from the referenced OrderHed. For "Miscellaneous" invoices the user can enter either a Sales Order Number or a Customer ID which will supply the CustNum.  """  
      self.PONum:str = obj["PONum"]
      """  Customer's PO#.   This is a reference field which will be printed on the invoice. Defaults from the OrderHed.PONum.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  User ID that entered the invoice. This is not maintainable by the user.  """  
      self.FOB:str = obj["FOB"]
      """  Defaults from sales order ORderHed.FOB  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Contains the foreign key to the TERMS master file.  Defaults from OrderHed if OrderNum > 0 else from the Customer master. This IS A MANDATORY ENTRY. User maintainable via a combo-box for terms description.  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice date is duplicated from the InvcGrp record.  """  
      self.DueDate:str = obj["DueDate"]
      """  The due date of the earlist unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year is duplicated from the related InvcGrp or based on ShipDate of Packing Slip. This is also refreshed if the InvoiceDate is changed.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period of invoice. This is duplicated in from the InvcBatc or during the "get shipments" function it is determined based on the ShipDate of the packing slip or when the invoice date is changed. It is overrideable.  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Once posted, maintenance is not allowed.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to establish invoice comments about the overall order. These will copied into the Invoice detail file as defaults.  """  
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      """  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (InvcDtl) and of the miscellaneous charges/credits (InvcMisc) records.  This field has a true sign. (credit memos are negative).  """  
      self.DocInvoiceAmt:int = obj["DocInvoiceAmt"]
      """  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (InvcDtl) and of the miscellaneous charges/credits (InvcMisc) records.  This field has a true sign. (credit memos are negative).  """  
      self.InvoiceBal:int = obj["InvoiceBal"]
      """  Current outstanding balance. Carries a true sign. (Credit memos are negative).  """  
      self.DocInvoiceBal:int = obj["DocInvoiceBal"]
      """  Current outstanding balance. Carries a true sign. (Credit memos are negative).  """  
      self.UnpostedBal:int = obj["UnpostedBal"]
      """  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  """  
      self.DocUnpostedBal:int = obj["DocUnpostedBal"]
      """  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  """  
      self.DepositCredit:int = obj["DepositCredit"]
      """  Amount to be credited against the invoice total due to deposit payments against the sales order. This can be defaulted from OrderHed.DepositBal. This will be printed on the invoice as a separate line "Less Deposit of:"  This value updates the OrderHed.DepositBal. Do not allow OrderHed.DepositBal to become negative.  """  
      self.DocDepositCredit:int = obj["DocDepositCredit"]
      """  Amount to be credited against the invoice total due to deposit payments against the sales order. This can be defaulted from OrderHed.DepositBal. This will be printed on the invoice as a separate line "Less Deposit of:"  This value updates the OrderHed.DepositBal. Do not allow OrderHed.DepositBal to become negative.  """  
      self.SalesRepList:str = obj["SalesRepList"]
      """  Stores the Sales Rep Codes for the invoice. Up to five codes can be  established. This field is not directly maintainable.  Instead temp widgets are used for entry of each individual code and then put together as one comma delimited string field and assigned to this field.  This field will have a Word index, it then will make reporting and data base integrity checking much easier through the use of the "contains phrase" when retrieving records. These codes can be left blank or must be valid in the SalesRep master. The defaults are based on the OrderHed.SalesRepList if a valid Order is referenced or first one is defaulted from the Customer master if ship to is blank else from the ShipTo.  """  
      self.InvoiceRef:int = obj["InvoiceRef"]
      """   This field is maintainable/viewable only for Credit Memos. It represents the invoice # that this credit memo relates to. It can be left blank. If entered it must be a valid InvcHead record where the InvcHead.CreditMemo = No. This field is also used to order the invoices when printing aging reports. The idea is to be able to print the credit memos next to their corresponding invoice. Therefore, this field will always have a value.

For Invoices it is equal to the InvoiceNum.

For Credit memos where they are not related to an invoice it is also set equal to the credit memo's InvoiceNum. In this later case when InvcHead.Credit = Yes and InvcHead.InvoiceNum = InvcHead.InvoiceRef the InvoiceRef is reset to zero before being displayed, then when written back to the database it is set = to the InvoiceNum if the user did not enter a related invoice.  """  
      self.RefCancelled:int = obj["RefCancelled"]
      """  Value of this field is reference to invoice which has been cancelled by current invoice.  """  
      self.RefCancelledBy:int = obj["RefCancelledBy"]
      """  Value of this field is reference to invoice that cancelled this invoice.  """  
      self.StartUp:bool = obj["StartUp"]
      """  An internal flag to indicate if this invoice was created by the Open Invoice Load program.  These records are not maintainable/viewable via invoice entry.  """  
      self.PayDates:str = obj["PayDates"]
      """  Contains the "list" of due dates for the scheduled payments. Delimited by the character defined in the "List-Delim" variable.  """  
      self.PayAmounts:str = obj["PayAmounts"]
      """  The scheduled payment amounts. Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  """  
      self.DocPayAmounts:str = obj["DocPayAmounts"]
      """  The scheduled payment amounts. Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  """  
      self.PayDiscDate:str = obj["PayDiscDate"]
      """  Prompt payment discount date. This is calculated based on the Invoice date + Terms.DiscountDays. Not user maintainable. This will default into the cash receipt record if the scheduled due amount is being paid in full.  """  
      self.PayDiscAmt:int = obj["PayDiscAmt"]
      """  Amount of discount that would be given if paid on or before the specified PayDiscDate. Calculated using the Terms.DiscountPercent X Invoice total amount.  """  
      self.DocPayDiscAmt:int = obj["DocPayDiscAmt"]
      """  Amount of discount that would be given if paid on or before the specified PayDiscDate. Calculated using the Terms.DiscountPercent X Invoice total amount.  """  
      self.BillConNum:int = obj["BillConNum"]
      """  Contains the key  value for the Billing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMBCON as the default.  """  
      self.InvoiceHeld:bool = obj["InvoiceHeld"]
      """  Invoices that are within a data entry group can be put on "Hold". They will not be posted until InvoiceHeld=No.  This flag can be used for whatever the reason the user may wish to keep an invoice in a data entry group from being posted.  The Manufacturing System sets this flag when creating invoices for order line items which had been flagged for "Time & Material Invoicing" (OrderDtl.TMBilling)  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
      self.JournalNum:int = obj["JournalNum"]
      """   Journal number that invoice was posted to.  This can also be thought of as the Voucher Number. If ARSyst.ARVoucherInvoices = Yes then this value will be printed on the Invoice.
Note: applicable only when posted to G/L.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Journal that invoice was posted to.  """  
      self.LineType:str = obj["LineType"]
      """  Used to differentiate between invoiced with standard lines which are for parts "PART"  and lines for service calls  "CALL" .  """  
      self.RMANum:int = obj["RMANum"]
      """   The RMA number which generated this Credit Memo.
Note: This only applies to Credit Memos. 
It is assigned as part of the Request Credit process for an RMA and is not directly maintainable by Invoice Entry.  """  
      self.Plant:str = obj["Plant"]
      """  The Site that the invoice is relate to.  """  
      self.CardMemberName:str = obj["CardMemberName"]
      """  The member's name on the credit card.  """  
      self.CardNumber:str = obj["CardNumber"]
      """  The credit card account identifier.  """  
      self.CardType:str = obj["CardType"]
      """  A code assigned by the user to uniquely identify a Credit Card Type master. This can't be blank.  """  
      self.ExpirationMonth:int = obj["ExpirationMonth"]
      """  The expiration month of the credit card.  """  
      self.ExpirationYear:int = obj["ExpirationYear"]
      """  The expiration year of the credit card.  """  
      self.CardID:str = obj["CardID"]
      """  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention.  """  
      self.CardmemberReference:str = obj["CardmemberReference"]
      """  Up to 17 alphnumeric characters provided by customer. This is used to track information on customer spending (e.g., cost center, project code). This field is especially critical, since inaccurate information will affect the general ledger. If no reference number is provided, leave this field blank.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  External Identifier  """  
      self.XRefInvoiceNum:str = obj["XRefInvoiceNum"]
      """  Cross reference invoice number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  """  
      self.DepGainLoss:int = obj["DepGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.DNComments:str = obj["DNComments"]
      """  For the Debit Note invoices this field contains the detail comments for the Debit Note. For the regular invoices this field contains the list of Debit Notes related to this invoice.  """  
      self.DNCustNbr:str = obj["DNCustNbr"]
      """  For the Debit Note invoice this field contains A Debit Note number assigned by the customer. The Debit Note number is supposed to be unique for the customer.  """  
      self.DebitNote:bool = obj["DebitNote"]
      """   Indicates the type of documents. Yes = Debit Note. This value can't be changed (the record is created on Invoice payment posting).
Debit Notes  also have the InvoiceSuffix field = "DN".  """  
      self.SoldToCustNum:int = obj["SoldToCustNum"]
      """  This is populated from ShipHead.CustNum representing the Sold To customer.  """  
      self.Consolidated:bool = obj["Consolidated"]
      """  Default is false.  This is only set to true if this invoice was generated via Get Shipments and shipments were combined based on common Bill To customer.  This is used by ARInvoice Entry to properly enable/disable Bill To customer field (InvcHead.CustNum) and to identify the record as a consolidated Invoice.  """  
      self.BillToInvoiceAddress:bool = obj["BillToInvoiceAddress"]
      """  If InvcHead.CustNum (BillTo) is different from InvcHead.SoldToCustNum (SoldTo), then this field defaults to the CustBillTo (Alt BillTo). InvoiceAddress status and SoldToInvoiceAddress is set to the opposite status.  """  
      self.SoldToInvoiceAddress:bool = obj["SoldToInvoiceAddress"]
      """  Always the opposite status of BillToInvoiceAddress.  If true, Invoice address for printing will use the Bill To address on the Sold-to customer.  If false, will use the Bill To address of the Bill to customer.  """  
      self.ProcessCard:str = obj["ProcessCard"]
      """  Stores the encrypted credit card number  """  
      self.RepComm1:int = obj["RepComm1"]
      """  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  """  
      self.RepComm2:int = obj["RepComm2"]
      """  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  """  
      self.RepComm3:int = obj["RepComm3"]
      """  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  """  
      self.RepComm4:int = obj["RepComm4"]
      """  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  """  
      self.RepComm5:int = obj["RepComm5"]
      """  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  """  
      self.RepRate1:int = obj["RepRate1"]
      """  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  """  
      self.RepRate2:int = obj["RepRate2"]
      """  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  """  
      self.RepRate3:int = obj["RepRate3"]
      """  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  """  
      self.RepRate4:int = obj["RepRate4"]
      """  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  """  
      self.RepRate5:int = obj["RepRate5"]
      """  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  """  
      self.RepSales1:int = obj["RepSales1"]
      """  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  """  
      self.RepSales2:int = obj["RepSales2"]
      """  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  """  
      self.RepSales3:int = obj["RepSales3"]
      """  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  """  
      self.RepSales4:int = obj["RepSales4"]
      """  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  """  
      self.RepSales5:int = obj["RepSales5"]
      """  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  """  
      self.RepSplit1:int = obj["RepSplit1"]
      """  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  """  
      self.RepSplit2:int = obj["RepSplit2"]
      """  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  """  
      self.RepSplit3:int = obj["RepSplit3"]
      """  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  """  
      self.RepSplit4:int = obj["RepSplit4"]
      """  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  """  
      self.RepSplit5:int = obj["RepSplit5"]
      """  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  """  
      self.CMType:str = obj["CMType"]
      """  Indicates if the Credit Memo is for a Rebate  """  
      self.CCStreetAddr:str = obj["CCStreetAddr"]
      """  Address used during AVS validation for credit transactions  """  
      self.CCZip:str = obj["CCZip"]
      """  Zip used during AVS validation in credit transactions  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.EDIReady:bool = obj["EDIReady"]
      """  Defines if this document is marked as EDI Ready  """  
      self.RecalcBeforePost:bool = obj["RecalcBeforePost"]
      """  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  """  
      self.Rounding:int = obj["Rounding"]
      """  Rounding in Base is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  """  
      self.DocRounding:int = obj["DocRounding"]
      """  Rounding in Customer currency  """  
      self.Rpt1DepositCredit:int = obj["Rpt1DepositCredit"]
      """  Reporting currency value of this field  """  
      self.Rpt2DepositCredit:int = obj["Rpt2DepositCredit"]
      """  Reporting currency value of this field  """  
      self.Rpt3DepositCredit:int = obj["Rpt3DepositCredit"]
      """  Reporting currency value of this field  """  
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
      self.Rpt1PayAmounts:str = obj["Rpt1PayAmounts"]
      """  Reporting currency value of this field  """  
      self.Rpt2PayAmounts:str = obj["Rpt2PayAmounts"]
      """  Reporting currency value of this field  """  
      self.Rpt3PayAmounts:str = obj["Rpt3PayAmounts"]
      """  Reporting currency value of this field  """  
      self.Rpt1PayDiscAmt:int = obj["Rpt1PayDiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2PayDiscAmt:int = obj["Rpt2PayDiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3PayDiscAmt:int = obj["Rpt3PayDiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1Rounding:int = obj["Rpt1Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt2Rounding:int = obj["Rpt2Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt3Rounding:int = obj["Rpt3Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt1UnpostedBal:int = obj["Rpt1UnpostedBal"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnpostedBal:int = obj["Rpt2UnpostedBal"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnpostedBal:int = obj["Rpt3UnpostedBal"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.DocDepApplied:int = obj["DocDepApplied"]
      """  Amount of deposit applied  """  
      self.Rpt1DepGainLoss:int = obj["Rpt1DepGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.Rpt2DepGainLoss:int = obj["Rpt2DepGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.Rpt3DepGainLoss:int = obj["Rpt3DepGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  The date this invoice will get applied to the books when it is posted.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.TaxPoint:str = obj["TaxPoint"]
      """  Tax point  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Date Used to calculate Tax Rates  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Unique identifier of the Tax Region assigned by the user.  """  
      self.LastChrgCalcDate:str = obj["LastChrgCalcDate"]
      """  The last date finance/late charges have been calculated for this invoice.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.TotFinChrg:int = obj["TotFinChrg"]
      """  Total Finance Charge amount.  """  
      self.DocumentPrinted:bool = obj["DocumentPrinted"]
      """  Indicates if the document has been printed.  """  
      self.PayDiscDays:str = obj["PayDiscDays"]
      """  Contains the "list" of pay discount days for the scheduled discounts. Delimited by the character defined in the "List-Delim" variable.  """  
      self.PayDiscPer:str = obj["PayDiscPer"]
      """  The discount percents. Corresponds with the PayDisDays list. Delimited by the character defined in the "list-delim" variable.  """  
      self.BlockedFinChrg:bool = obj["BlockedFinChrg"]
      """  Blocks certain invoice from generating finance/later charge.  """  
      self.BlockedFinChrgReason:str = obj["BlockedFinChrgReason"]
      """  Reason why invoice has been blocked generating finance/later charge and only is enabled if the invoice is blocked.  """  
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
      self.BlockedRemLetters:bool = obj["BlockedRemLetters"]
      """  Blocks certain invoice from being printed on reminder letters.  """  
      self.PayDiscPartPay:bool = obj["PayDiscPartPay"]
      """  Field to define when apply the discount percentage, can be when invoice is paid in full or Cash amount  """  
      self.BlockedRemLettersReason:str = obj["BlockedRemLettersReason"]
      """  Reason why invoice has been blocked from being printed on reminder letters and only is enabled if the invoice is blocked.  """  
      self.ShipDate:str = obj["ShipDate"]
      """  The actual ship date for the packing slip. Default as system date.  """  
      self.CurrRateDate:str = obj["CurrRateDate"]
      """  Currency Rate Date  """  
      self.PIPayment:str = obj["PIPayment"]
      """   Indicates if the invoice has been paid by a Payment Instrument.
Values:
blank = Not linked to a Payment Instrument
"O" = Paid by outstanding Payment Instrument
"C" = Paid by colledted Payment instument  """  
      self.PMUID:int = obj["PMUID"]
      """  Unique identifier of the payment method  """  
      self.UseAltBillTo:bool = obj["UseAltBillTo"]
      """  If TRUE taxes will be calculated based on the Alternate Bill To, if FALSE it will proceed normally.  """  
      self.InPrice:bool = obj["InPrice"]
      """  Indicates that the tax is included in the unit price  """  
      self.CorrectionInv:bool = obj["CorrectionInv"]
      """  Will be se to Yes if the Invoice was created by the Correction (Reversing) logic.  """  
      self.TaxRateGrpCode:str = obj["TaxRateGrpCode"]
      """  Tax Rate Group Code  """  
      self.LockTaxRate:bool = obj["LockTaxRate"]
      """  Locks Tax Rate and allows user to edit the tax exchange rate  """  
      self.SEBankRef:str = obj["SEBankRef"]
      """  Sweden Finland Localization field - Banking Reference  """  
      self.GUITaxTypeCode:str = obj["GUITaxTypeCode"]
      """  Government Uniform Invoice Tax Type Code (Taiwan Localization field)  """  
      self.GUIFormatCode:str = obj["GUIFormatCode"]
      """  Government Uniform Invoice Format Code (Taiwan Localization field)  """  
      self.GUIDeductCode:str = obj["GUIDeductCode"]
      """  Government Uniform Invoice Deduct Code (Taiwan Localization field)  """  
      self.ReversalDocAmount:int = obj["ReversalDocAmount"]
      """  Reversal Doucment Amount  """  
      self.OrigDueDate:str = obj["OrigDueDate"]
      """  Original Due Date at posting time  """  
      self.HeadNum:int = obj["HeadNum"]
      """  The reference to CashHead.HeadNum.Used in deposit invoices  """  
      self.ARLOCID:str = obj["ARLOCID"]
      """  Letter of Credit ID.  """  
      self.ContractRef:str = obj["ContractRef"]
      """  The free text field which can contain reference (such as Contract)  """  
      self.OurBank:str = obj["OurBank"]
      """  Bank for Cash receipts. For Shipment Invoices it comes from Packing Slip. For Deposit Invoices created based on deposit payments it is actual bank money are received to. For other  Invoice types, default comes from 1) Sales Order 2) Bill To Customer 3) System default (Company).  """  
      self.ContractDate:str = obj["ContractDate"]
      """  Addition to Contract  """  
      self.PBProjectID:str = obj["PBProjectID"]
      """  If the invoice was generated in Project Billing then it is reference to the project.  """  
      self.DepositAmt:int = obj["DepositAmt"]
      """  Deposit amount is transaction amount of deposit payment  """  
      self.GUIExportBillNumber:str = obj["GUIExportBillNumber"]
      """   Taiwan Localization
Export Bill Number  """  
      self.DocDepositAmt:int = obj["DocDepositAmt"]
      """  Deposit amount is transaction amount of deposit payment in document currency  """  
      self.GUIDateOfExport:str = obj["GUIDateOfExport"]
      """   Taiwan Localization
Date of Export  """  
      self.Rpt1DepositAmt:int = obj["Rpt1DepositAmt"]
      """  Deposit amount is transaction amount of deposit payment in Rpt1 currency  """  
      self.GUIExportType:str = obj["GUIExportType"]
      """   Taiwan Localization
Export Type  """  
      self.Rpt2DepositAmt:int = obj["Rpt2DepositAmt"]
      """  Deposit amount is transaction amount of deposit payment in Rpt2 currency  """  
      self.GUIExportMark:str = obj["GUIExportMark"]
      """   Taiwan Localization
Export Mark  """  
      self.Rpt3DepositAmt:int = obj["Rpt3DepositAmt"]
      """  Deposit amount is transaction amount of deposit payment in Rpt23currency  """  
      self.GUIExportBillType:str = obj["GUIExportBillType"]
      """   Taiwan Localization
Export Bill Type  """  
      self.DepUnallocatedAmt:int = obj["DepUnallocatedAmt"]
      """  Deposit unallocated amount in base currency  """  
      self.SummarizationDate:str = obj["SummarizationDate"]
      """  Day when a company sums up accounts receivables for each customer.  """  
      self.DocDepUnallocatedAmt:int = obj["DocDepUnallocatedAmt"]
      """  Deposit unallocated amount in document currency  """  
      self.BillingDate:str = obj["BillingDate"]
      """  Date when a company bills the customer  """  
      self.Rpt1DepUnallocatedAmt:int = obj["Rpt1DepUnallocatedAmt"]
      """  Deposit unallocated amount in Rpt1 currency  """  
      self.BillingNumber:str = obj["BillingNumber"]
      """  Billing Number to be generated from Legal Numbering upon printing of billing statement.  """  
      self.Rpt2DepUnallocatedAmt:int = obj["Rpt2DepUnallocatedAmt"]
      """  Deposit unallocated amount in Rpt2 currency  """  
      self.ReadyToBill:bool = obj["ReadyToBill"]
      """  Only records ready to bill will be printed in the Billing Statement  """  
      self.Rpt3DepUnallocatedAmt:int = obj["Rpt3DepUnallocatedAmt"]
      """  Deposit unallocated amount in Rpt3 currency  """  
      self.OvrDefTaxDate:bool = obj["OvrDefTaxDate"]
      """  Flag to indicate if the DefTaxDate will be overwritten when Tax Point change on Invoice Header.  """  
      self.XRefContractNum:str = obj["XRefContractNum"]
      """  Cross Reference Contract Number.  """  
      self.XRefContractDate:str = obj["XRefContractDate"]
      """  Cross Reference Contract Date.  """  
      self.MainSite:bool = obj["MainSite"]
      """  Main Site  """  
      self.SiteCode:str = obj["SiteCode"]
      """  Site Code  """  
      self.BranchID:str = obj["BranchID"]
      """  Branch ID  """  
      self.CustAgentName:str = obj["CustAgentName"]
      """  Customer Agent Name  """  
      self.CustAgentTaxRegNo:str = obj["CustAgentTaxRegNo"]
      """  Customer Agent Tax Region Number  """  
      self.ExportType:str = obj["ExportType"]
      """  Export Type: 0-No Export, 1-Normal Export(S04), 2-Material Export(S05), 3-Service Export(S06)  """  
      self.ExportReportNo:str = obj["ExportReportNo"]
      """  Export Report Number  """  
      self.RealEstateNo:str = obj["RealEstateNo"]
      """  Real Estate Number  """  
      self.Excluded:bool = obj["Excluded"]
      """  Excluded  """  
      self.Deferred:bool = obj["Deferred"]
      """  Deferred  """  
      self.CycleCode:str = obj["CycleCode"]
      """  CycleCode  """  
      self.Duration:int = obj["Duration"]
      """  Duration  """  
      self.EndDate:str = obj["EndDate"]
      """  EndDate  """  
      self.MaxValueAmt:int = obj["MaxValueAmt"]
      """  MaxValueAmt  """  
      self.DocMaxValueAmt:int = obj["DocMaxValueAmt"]
      """  DocMaxValueAmt  """  
      self.Rpt1MaxValueAmt:int = obj["Rpt1MaxValueAmt"]
      """  Rpt1MaxValueAmt  """  
      self.Rpt2MaxValueAmt:int = obj["Rpt2MaxValueAmt"]
      """  Rpt2MaxValueAmt  """  
      self.Rpt3MaxValueAmt:int = obj["Rpt3MaxValueAmt"]
      """  Rpt3MaxValueAmt  """  
      self.HoldInvoice:bool = obj["HoldInvoice"]
      """  HoldInvoice  """  
      self.CopyLatestInvoice:bool = obj["CopyLatestInvoice"]
      """  CopyLatestInvoice  """  
      self.OverrideEndDate:bool = obj["OverrideEndDate"]
      """  OverrideEndDate  """  
      self.CycleInactive:bool = obj["CycleInactive"]
      """  CycleInactive  """  
      self.RecurSource:bool = obj["RecurSource"]
      """  RecurSource  """  
      self.InstanceNum:int = obj["InstanceNum"]
      """  InstanceNum  """  
      self.RecurBalance:int = obj["RecurBalance"]
      """  RecurBalance  """  
      self.DocRecurBalance:int = obj["DocRecurBalance"]
      """  DocRecurBalance  """  
      self.Rpt1RecurBalance:int = obj["Rpt1RecurBalance"]
      """  Rpt1RecurBalance  """  
      self.Rpt2RecurBalance:int = obj["Rpt2RecurBalance"]
      """  Rpt2RecurBalance  """  
      self.Rpt3RecurBalance:int = obj["Rpt3RecurBalance"]
      """  Rpt3RecurBalance  """  
      self.LastDate:str = obj["LastDate"]
      """  LastDate  """  
      self.RecurringState:str = obj["RecurringState"]
      """  RecurringState  """  
      self.IsRecurring:bool = obj["IsRecurring"]
      """  IsRecurring  """  
      self.InvoiceNumList:str = obj["InvoiceNumList"]
      """  InvoiceNumList  """  
      self.IsAddedToGTI:bool = obj["IsAddedToGTI"]
      """  IsAddedToGTI  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CHISRCodeLine:str = obj["CHISRCodeLine"]
      """  CHISRCodeLine  """  
      self.CMReason:str = obj["CMReason"]
      """  CMReason  """  
      self.THIsImmatAdjustment:bool = obj["THIsImmatAdjustment"]
      """  THIsImmatAdjustment  """  
      self.AGAuthorizationCode:str = obj["AGAuthorizationCode"]
      """  AGAuthorizationCode  """  
      self.AGAuthorizationDate:str = obj["AGAuthorizationDate"]
      """  AGAuthorizationDate  """  
      self.AGUseGoodDefaultMark:bool = obj["AGUseGoodDefaultMark"]
      """  AGUseGoodDefaultMark  """  
      self.AGDocumentLetter:str = obj["AGDocumentLetter"]
      """  AGDocumentLetter  """  
      self.AGInvoicingPoint:str = obj["AGInvoicingPoint"]
      """  AGInvoicingPoint  """  
      self.AGLegalNumber:str = obj["AGLegalNumber"]
      """  AGLegalNumber  """  
      self.AGPrintingControlType:str = obj["AGPrintingControlType"]
      """  AGPrintingControlType  """  
      self.RevisionDate:str = obj["RevisionDate"]
      """  RevisionDate  """  
      self.RevisionNum:int = obj["RevisionNum"]
      """  RevisionNum  """  
      self.TWDeclareYear:int = obj["TWDeclareYear"]
      """  TWDeclareYear  """  
      self.TWDeclarePeriod:int = obj["TWDeclarePeriod"]
      """  TWDeclarePeriod  """  
      self.TWGenerationType:str = obj["TWGenerationType"]
      """  TWGenerationType  """  
      self.TWGUIGroup:str = obj["TWGUIGroup"]
      """  TWGUIGroup  """  
      self.TWPeriodPrefix:str = obj["TWPeriodPrefix"]
      """  TWPeriodPrefix  """  
      self.InvInCollections:bool = obj["InvInCollections"]
      """  Indicates if the Invoice is in Collections status  """  
      self.CollectionsCust:bool = obj["CollectionsCust"]
      """   Indicates if the Customer of the Invoice is in Collections
(Peru Localization)  """  
      self.CounterARForm:int = obj["CounterARForm"]
      """  A counter of the number of times an AR Invoice has been transmitted via EDI.  The counter is automatically incremented each time the EDIReady flag changes from False to True.  """  
      self.PostedRecog:bool = obj["PostedRecog"]
      """  flag indicates if Revenue of the invoice has been already posted  """  
      self.CNConfirmDate:str = obj["CNConfirmDate"]
      """  Confirmation Date  """  
      self.MXSATSeal:str = obj["MXSATSeal"]
      """  MXSATSeal  """  
      self.MXSerie:str = obj["MXSerie"]
      """  MXSerie  """  
      self.MXTaxRcptType:str = obj["MXTaxRcptType"]
      """  MXTaxRcptType  """  
      self.MXFiscalFolio:str = obj["MXFiscalFolio"]
      """  MXFiscalFolio  """  
      self.MXTotalPayments:int = obj["MXTotalPayments"]
      """  MXTotalPayments  """  
      self.MXFolio:str = obj["MXFolio"]
      """  MXFolio  """  
      self.MXCertifiedTimestamp:str = obj["MXCertifiedTimestamp"]
      """  MXCertifiedTimestamp  """  
      self.MXSATCertificateSN:str = obj["MXSATCertificateSN"]
      """  MXSATCertificateSN  """  
      self.MXDigitalSeal:str = obj["MXDigitalSeal"]
      """  MXDigitalSeal  """  
      self.MXPostedTimeStamp:str = obj["MXPostedTimeStamp"]
      """  MXPostedTimeStamp  """  
      self.MXCertificate:str = obj["MXCertificate"]
      """  MXCertificate  """  
      self.MXApprovalYear:int = obj["MXApprovalYear"]
      """  MXApprovalYear  """  
      self.MXCBB:str = obj["MXCBB"]
      """  MXCBB  """  
      self.MXApprovalNum:int = obj["MXApprovalNum"]
      """  MXApprovalNum  """  
      self.MXOriginalStringTFD:str = obj["MXOriginalStringTFD"]
      """  MXOriginalStringTFD  """  
      self.MXPaymentNum:int = obj["MXPaymentNum"]
      """  MXPaymentNum  """  
      self.MXPaidAs:str = obj["MXPaidAs"]
      """  MXPaidAs  """  
      self.MXCertificateSN:str = obj["MXCertificateSN"]
      """  MXCertificateSN  """  
      self.MXOriginalAmount:int = obj["MXOriginalAmount"]
      """  MXOriginalAmount  """  
      self.MXAccountNumber:str = obj["MXAccountNumber"]
      """  MXAccountNumber  """  
      self.MXOriginalDate:str = obj["MXOriginalDate"]
      """  MXOriginalDate  """  
      self.MXOriginalSeries:str = obj["MXOriginalSeries"]
      """  MXOriginalSeries  """  
      self.MXOriginalFolio:str = obj["MXOriginalFolio"]
      """  MXOriginalFolio  """  
      self.MXTaxRegime:str = obj["MXTaxRegime"]
      """  MXTaxRegime  """  
      self.MXOriginalString:str = obj["MXOriginalString"]
      """  MXOriginalString  """  
      self.MXPaymentName:str = obj["MXPaymentName"]
      """  MXPaymentName  """  
      self.EInvoice:bool = obj["EInvoice"]
      """  EInvoice  """  
      self.EInvStatus:int = obj["EInvStatus"]
      """  EInvStatus  """  
      self.EInvTimestamp:str = obj["EInvTimestamp"]
      """  EInvTimestamp  """  
      self.EInvUpdatedBy:str = obj["EInvUpdatedBy"]
      """  EInvUpdatedBy  """  
      self.EInvException:str = obj["EInvException"]
      """  EInvException  """  
      self.WithTaxConfirm:bool = obj["WithTaxConfirm"]
      """  Flagged that this invoice has taxes which were necessary or is necessary now.  """  
      self.UseAltBillToID:bool = obj["UseAltBillToID"]
      """  UseAltBillToID  """  
      self.MXCancelledDate:str = obj["MXCancelledDate"]
      """  MXCancelledDate  """  
      self.Overpaid:bool = obj["Overpaid"]
      """  Overpaid  """  
      self.OrdExchangeRate:int = obj["OrdExchangeRate"]
      """  OrdExchangeRate  """  
      self.PEAPPayNum:int = obj["PEAPPayNum"]
      """  PEAPPayNum  """  
      self.PEBankNumber:str = obj["PEBankNumber"]
      """  PEBankNumber  """  
      self.PECharges:int = obj["PECharges"]
      """  PECharges  """  
      self.PECommissions:int = obj["PECommissions"]
      """  PECommissions  """  
      self.PEDetTaxAmt:int = obj["PEDetTaxAmt"]
      """  PEDetTaxAmt  """  
      self.PEDetTaxCurrencyCode:str = obj["PEDetTaxCurrencyCode"]
      """  PEDetTaxCurrencyCode  """  
      self.PEDischargeAmt:int = obj["PEDischargeAmt"]
      """  PEDischargeAmt  """  
      self.PEDischargeDate:str = obj["PEDischargeDate"]
      """  PEDischargeDate  """  
      self.PEInterest:int = obj["PEInterest"]
      """  PEInterest  """  
      self.PENoPayPenalty:int = obj["PENoPayPenalty"]
      """  PENoPayPenalty  """  
      self.PESUNATDepAmt:int = obj["PESUNATDepAmt"]
      """  CSF Peru - SUNAT Deposit Amount  """  
      self.PESUNATDepDate:str = obj["PESUNATDepDate"]
      """  CSF Peru - SUNAT Deposit Date  """  
      self.PESUNATDepNum:str = obj["PESUNATDepNum"]
      """  CSF Peru -  SUNAT Deposit Number  """  
      self.PEBOEPosted:bool = obj["PEBOEPosted"]
      """  PEBOEPosted  """  
      self.DocPEInterest:int = obj["DocPEInterest"]
      """  DocPEInterest  """  
      self.DocPECommissions:int = obj["DocPECommissions"]
      """  DocPECommissions  """  
      self.DocPECharges:int = obj["DocPECharges"]
      """  DocPECharges  """  
      self.DocPENoPayPenalty:int = obj["DocPENoPayPenalty"]
      """  DocPENoPayPenalty  """  
      self.DocPEDischargeAmt:int = obj["DocPEDischargeAmt"]
      """  DocPEDischargeAmt  """  
      self.DocPEDetTaxAmt:int = obj["DocPEDetTaxAmt"]
      """  DocPEDetTaxAmt  """  
      self.Rpt1PEInterest:int = obj["Rpt1PEInterest"]
      """  Rpt1PEInterest  """  
      self.Rpt1PECommissions:int = obj["Rpt1PECommissions"]
      """  Rpt1PECommissions  """  
      self.Rpt1PECharges:int = obj["Rpt1PECharges"]
      """  Rpt1PECharges  """  
      self.Rpt1PENoPayPenalty:int = obj["Rpt1PENoPayPenalty"]
      """  Rpt1PENoPayPenalty  """  
      self.Rpt1PEDischargeAmt:int = obj["Rpt1PEDischargeAmt"]
      """  Rpt1PEDischargeAmt  """  
      self.Rpt2PEInterest:int = obj["Rpt2PEInterest"]
      """  Rpt2PEInterest  """  
      self.Rpt2PECommissions:int = obj["Rpt2PECommissions"]
      """  Rpt2PECommissions  """  
      self.Rpt2PECharges:int = obj["Rpt2PECharges"]
      """  Rpt2PECharges  """  
      self.Rpt2PENoPayPenalty:int = obj["Rpt2PENoPayPenalty"]
      """  Rpt2PENoPayPenalty  """  
      self.Rpt2PEDischargeAmt:int = obj["Rpt2PEDischargeAmt"]
      """  Rpt2PEDischargeAmt  """  
      self.Rpt3PEInterest:int = obj["Rpt3PEInterest"]
      """  Rpt3PEInterest  """  
      self.Rpt3PECommissions:int = obj["Rpt3PECommissions"]
      """  Rpt3PECommissions  """  
      self.Rpt3PECharges:int = obj["Rpt3PECharges"]
      """  Rpt3PECharges  """  
      self.Rpt3PENoPayPenalty:int = obj["Rpt3PENoPayPenalty"]
      """  Rpt3PENoPayPenalty  """  
      self.Rpt3PEDischargeAmt:int = obj["Rpt3PEDischargeAmt"]
      """  Rpt3PEDischargeAmt  """  
      self.OurSupplierCode:str = obj["OurSupplierCode"]
      """  Our Supplier Code  """  
      self.PEGuaranteeName:str = obj["PEGuaranteeName"]
      """  PEGuaranteeName  """  
      self.PEGuaranteeAddress1:str = obj["PEGuaranteeAddress1"]
      """  PEGuaranteeAddress1  """  
      self.PEGuaranteeAddress2:str = obj["PEGuaranteeAddress2"]
      """  PEGuaranteeAddress2  """  
      self.PEGuaranteeAddress3:str = obj["PEGuaranteeAddress3"]
      """  PEGuaranteeAddress3  """  
      self.PEGuaranteeCity:str = obj["PEGuaranteeCity"]
      """  PEGuaranteeCity  """  
      self.PEGuaranteeState:str = obj["PEGuaranteeState"]
      """  PEGuaranteeState  """  
      self.PEGuaranteeZip:str = obj["PEGuaranteeZip"]
      """  PEGuaranteeZip  """  
      self.PEGuaranteeCountry:str = obj["PEGuaranteeCountry"]
      """  PEGuaranteeCountry  """  
      self.PEGuaranteeTaxID:str = obj["PEGuaranteeTaxID"]
      """  PEGuaranteeTaxID  """  
      self.PEGuaranteePhoneNum:str = obj["PEGuaranteePhoneNum"]
      """  PEGuaranteePhoneNum  """  
      self.PEBOEStatus:str = obj["PEBOEStatus"]
      """  PEBOEStatus  """  
      self.PEBOEIsMultiGen:bool = obj["PEBOEIsMultiGen"]
      """  PEBOEIsMultiGen  """  
      self.PERefDocID:str = obj["PERefDocID"]
      """  PE Reference Document ID  """  
      self.PEReasonCode:str = obj["PEReasonCode"]
      """  PE Reason Code  """  
      self.PEReasonDesc:str = obj["PEReasonDesc"]
      """  PE Reason Description  """  
      self.TWGUIRegNumSeller:str = obj["TWGUIRegNumSeller"]
      """  TW GUI Code Seller  """  
      self.TWGUIRegNumBuyer:str = obj["TWGUIRegNumBuyer"]
      """  TW GUI Code Buyer  """  
      self.TWGUIExportDocumentName:str = obj["TWGUIExportDocumentName"]
      """  Document Name  """  
      self.TWGUIExportRemarks:str = obj["TWGUIExportRemarks"]
      """  Remarks  """  
      self.TWGUIExportVerification:str = obj["TWGUIExportVerification"]
      """  Verification  """  
      self.PEDebitNoteReasonCode:str = obj["PEDebitNoteReasonCode"]
      """  PEDebitNoteReasonCode  """  
      self.PEDebitNote:bool = obj["PEDebitNote"]
      """  PEDebitNote  """  
      self.MXPartPmt:bool = obj["MXPartPmt"]
      """  MXPartPmt  """  
      self.CNTaxInvoiceType:int = obj["CNTaxInvoiceType"]
      """  Tax Invoice Type  """  
      self.MXExportOperationType:str = obj["MXExportOperationType"]
      """  MXExportOperationType  """  
      self.MXExportCustDocCode:str = obj["MXExportCustDocCode"]
      """  MXExportCustDocCode  """  
      self.MXExportCertOriginNum:str = obj["MXExportCertOriginNum"]
      """  MXExportCertOriginNum  """  
      self.MXExportConfNum:str = obj["MXExportConfNum"]
      """  MXExportConfNum  """  
      self.MXExportCertOrigin:bool = obj["MXExportCertOrigin"]
      """  MXExportCertOrigin  """  
      self.MXIncoterm:str = obj["MXIncoterm"]
      """  MXIncoterm  """  
      self.AGDocConcept:int = obj["AGDocConcept"]
      """  AGDocConcept  """  
      self.EInvRefNum:str = obj["EInvRefNum"]
      """  Electronic Invoice reference number  """  
      self.ExportDocRefNum:str = obj["ExportDocRefNum"]
      """  Export document reference number  """  
      self.ExportDocDate:str = obj["ExportDocDate"]
      """  Export document date  """  
      self.INTaxTransactionID:str = obj["INTaxTransactionID"]
      """  Tax Transaction ID  """  
      self.MXMovingReasonFlag:bool = obj["MXMovingReasonFlag"]
      """  MXMovingReasonFlag  """  
      self.MXMovingReason:str = obj["MXMovingReason"]
      """  MXMovingReason  """  
      self.MXNumRegIdTrib:str = obj["MXNumRegIdTrib"]
      """  MXNumRegIdTrib  """  
      self.MXResidenCountryNum:int = obj["MXResidenCountryNum"]
      """  MXResidenCountryNum  """  
      self.MXPurchaseType:str = obj["MXPurchaseType"]
      """  MXPurchaseType  """  
      self.MXConfirmationCode:str = obj["MXConfirmationCode"]
      """  MXConfirmationCode  """  
      self.MXExternalCode:str = obj["MXExternalCode"]
      """  MXExternalCode  """  
      self.ServiceInvoice:bool = obj["ServiceInvoice"]
      """  This invoice was created via an integration with a third-party field service.  """  
      self.MXDomesticTransfer:bool = obj["MXDomesticTransfer"]
      """  MXDomesticTransfer  """  
      self.MXCancellationMode:str = obj["MXCancellationMode"]
      """  MXCancellationMode  """  
      self.INShippingPortCode:str = obj["INShippingPortCode"]
      """  Shipping Port Code  """  
      self.INExportProcedure:str = obj["INExportProcedure"]
      """  Export Procedure  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.DigitalSignature:str = obj["DigitalSignature"]
      """  DigitalSignature  """  
      self.SignedOn:str = obj["SignedOn"]
      """  SignedOn  """  
      self.SignedBy:str = obj["SignedBy"]
      """  SignedBy  """  
      self.FirstPrintDate:str = obj["FirstPrintDate"]
      """  FirstPrintDate  """  
      self.DocCopyNum:int = obj["DocCopyNum"]
      """  DocCopyNum  """  
      self.DepositBalance:int = obj["DepositBalance"]
      """  DepositBalance  """  
      self.DocDepositBalance:int = obj["DocDepositBalance"]
      """  DocDepositBalance  """  
      self.Rpt1DepositBalance:int = obj["Rpt1DepositBalance"]
      """  Rpt1DepositBalance  """  
      self.Rpt2DepositBalance:int = obj["Rpt2DepositBalance"]
      """  Rpt2DepositBalance  """  
      self.Rpt3DepositBalance:int = obj["Rpt3DepositBalance"]
      """  Rpt3DepositBalance  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this invoice record is associated with.  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  The help desk case related to this invoice.  """  
      self.CreditOverride:bool = obj["CreditOverride"]
      """  Indicates that the credit hold was overridden for this invoice.  """  
      self.CreditOverrideDate:str = obj["CreditOverrideDate"]
      """  Description	Indicates that the credit hold was overridden for this invoice.	The date and time the user override the invoice credit hold.  """  
      self.CreditOverrideUserID:str = obj["CreditOverrideUserID"]
      """  The user id that override the invoice credit hold.  """  
      self.CreditHold:bool = obj["CreditHold"]
      """  Indicates the invoice is on credit hold.  Applicable to miscellaneous invoices only.  """  
      self.PEXMLType:int = obj["PEXMLType"]
      """  Peru Electronic Invoice XML Type  """  
      self.COCreditMemoReasonCode:str = obj["COCreditMemoReasonCode"]
      """  COCreditMemoReasonCode  """  
      self.CODebitMemoReasonCode:str = obj["CODebitMemoReasonCode"]
      """  CODebitMemoReasonCode  """  
      self.COReasonDesc:str = obj["COReasonDesc"]
      """  COReasonDesc  """  
      self.CODebitNote:bool = obj["CODebitNote"]
      """  CODebitNote  """  
      self.PEDetractionTranNum:int = obj["PEDetractionTranNum"]
      """  PEDetractionTranNum  """  
      self.PEProductCode:str = obj["PEProductCode"]
      """  PEProductCode  """  
      self.PECollectionGroupID:str = obj["PECollectionGroupID"]
      """  PECollectionGroupID  """  
      self.PECaptionCode:str = obj["PECaptionCode"]
      """  PE Caption Code  """  
      self.PECaption:str = obj["PECaption"]
      """  PE Caption Code Description  """  
      self.PERefDocumentType:str = obj["PERefDocumentType"]
      """  PE Reference DocumentType 1  """  
      self.PERefDocumentNumber:str = obj["PERefDocumentNumber"]
      """  PE Reference Document Number 1  """  
      self.PEDetrGoodServiceCode:str = obj["PEDetrGoodServiceCode"]
      """  PE Detraction good or service code  """  
      self.PERefDocumentType2:str = obj["PERefDocumentType2"]
      """  PE Reference DocumentType 2  """  
      self.PERefDocumentType3:str = obj["PERefDocumentType3"]
      """  PE Reference DocumentType 3  """  
      self.PERefDocumentType4:str = obj["PERefDocumentType4"]
      """  PE Reference DocumentType 4  """  
      self.PERefDocumentType5:str = obj["PERefDocumentType5"]
      """  PE Reference DocumentType 5  """  
      self.PERefDocumentNumber2:str = obj["PERefDocumentNumber2"]
      """  PE Reference Document Number 2  """  
      self.PERefDocumentNumber3:str = obj["PERefDocumentNumber3"]
      """  PE Reference Document Number 3  """  
      self.PERefDocumentNumber4:str = obj["PERefDocumentNumber4"]
      """  PE Reference Document Number 4  """  
      self.PERefDocumentNumber5:str = obj["PERefDocumentNumber5"]
      """  PE Reference Document Number 5  """  
      self.ELIEInvoice:bool = obj["ELIEInvoice"]
      """  E-invoice  """  
      self.ELIEInvStatus:int = obj["ELIEInvStatus"]
      """  Status of E-invoice (1 - Open, 2 - Generated, 3 - Sent, 4 - Error).  """  
      self.ELIEInvUpdatedBy:str = obj["ELIEInvUpdatedBy"]
      """  User Id of the person generated E-invoice.  """  
      self.ELIEInvException:str = obj["ELIEInvException"]
      """  E-invoice error description.  """  
      self.ELIEInvUpdatedOn:str = obj["ELIEInvUpdatedOn"]
      """  Date and Time of E-invoice generation.  """  
      self.COOperType:str = obj["COOperType"]
      """  COOperType  """  
      self.CentralCollection:bool = obj["CentralCollection"]
      """  Flag that indicates if the Invoice is for Central Collection.  """  
      self.CColChildCompany:str = obj["CColChildCompany"]
      """  Company that created this invoice.  """  
      self.CColParentCompany:str = obj["CColParentCompany"]
      """  Central Collection company.  """  
      self.CColOrderNum:int = obj["CColOrderNum"]
      """  Order number on the invoicing company.  """  
      self.CColChildInvoiceNum:int = obj["CColChildInvoiceNum"]
      """  Invoice number on the invoicing company.  """  
      self.CColInvoiceNum:int = obj["CColInvoiceNum"]
      """  Invoice number on central collection company  """  
      self.CColChildLegalNumber:str = obj["CColChildLegalNumber"]
      """  Legal number on the invoicing company invoice.  """  
      self.CColLegalNumber:str = obj["CColLegalNumber"]
      """  Legal number on central collection company.  """  
      self.CColInvoiceRef:int = obj["CColInvoiceRef"]
      """  Invoice reference on the Invoicing Company.  """  
      self.CColInvBal:int = obj["CColInvBal"]
      """  Invoice Balance in the Central Collection company.  """  
      self.DocCColInvBal:int = obj["DocCColInvBal"]
      """  Central Collection Doc Invoice Balance.  """  
      self.CColInvAmt:int = obj["CColInvAmt"]
      """  Invoice Amount on the Invoicing Company.  """  
      self.DocCColInvAmt:int = obj["DocCColInvAmt"]
      """  Invoice Amount on the Invoicing Company.  """  
      self.Rpt1CColInvBal:int = obj["Rpt1CColInvBal"]
      """  Rpt 1 Parent Invoice Balance  """  
      self.Rpt2CColInvBal:int = obj["Rpt2CColInvBal"]
      """  Rpt 2 Parent Invoice Balance  """  
      self.Rpt3CColInvBal:int = obj["Rpt3CColInvBal"]
      """  Rpt 3 Parent Invoice Balance  """  
      self.Rpt1CColInvAmt:int = obj["Rpt1CColInvAmt"]
      """  Rpt 1 Child Invoice Amount  """  
      self.Rpt2CColInvAmt:int = obj["Rpt2CColInvAmt"]
      """  Rpt 2 Child Invoice Amount  """  
      self.Rpt3CColInvAmt:int = obj["Rpt3CColInvAmt"]
      """  Rpt 3 Child Invoice Amount  """  
      self.NettingID:int = obj["NettingID"]
      """  Id of the netting transaction that generated this document.  """  
      self.ELIEInvTerminalName:str = obj["ELIEInvTerminalName"]
      """  User terminal name  """  
      self.ELIEInvTerminalIP:str = obj["ELIEInvTerminalIP"]
      """  User terminal IP  """  
      self.Description:str = obj["Description"]
      """  GL Description  """  
      self.WithholdAcctToInterim:bool = obj["WithholdAcctToInterim"]
      """  WithholdAcctToInterim  """  
      self.CColOpenInvoice:bool = obj["CColOpenInvoice"]
      """  Indicates if the Central Collection parent invoice is open.  """  
      self.AGQRCodeData:str = obj["AGQRCodeData"]
      """  AGQRCodeData  """  
      self.ExemptReasonCode:str = obj["ExemptReasonCode"]
      """  Exempt Reason Code  """  
      self.ELIEInvID:str = obj["ELIEInvID"]
      """  EInvoice ID  """  
      self.CallNum:int = obj["CallNum"]
      """  this is a link to the service call that this invoice is for.  Linetype = "CALL"  """  
      self.CallLine:int = obj["CallLine"]
      """  this is a link to the service call line that this invoice is for.  Linetype = "CALL"  """  
      self.JobNum:str = obj["JobNum"]
      """  Associates the Call Line record back its linked jobnum  """  
      self.MXCancelReasonCode:str = obj["MXCancelReasonCode"]
      """  MXCancelReasonCode  """  
      self.MXSubstInvoiceNum:int = obj["MXSubstInvoiceNum"]
      """  MXSubstInvoiceNum  """  
      self.MXExportType:str = obj["MXExportType"]
      """  MXExportType  """  
      self.MXGlobalInvoicePeriod:str = obj["MXGlobalInvoicePeriod"]
      """  MXGlobalInvoicePeriod  """  
      self.MXGlobalInvoiceMonth:str = obj["MXGlobalInvoiceMonth"]
      """  MXGlobalInvoiceMonth  """  
      self.ELIEInvServiceProviderStatus:int = obj["ELIEInvServiceProviderStatus"]
      """  ELIEInvServiceProviderStatus  """  
      self.IncotermCode:str = obj["IncotermCode"]
      """  Incoterm Code  """  
      self.IncotermLocation:str = obj["IncotermLocation"]
      """  Incoterm Location  """  
      self.CovenantDiscPercent:int = obj["CovenantDiscPercent"]
      """  CovenantDiscPercent  """  
      self.TotalCovenantDiscount:int = obj["TotalCovenantDiscount"]
      """  TotalCovenantDiscount  """  
      self.DocCovenantDiscount:int = obj["DocCovenantDiscount"]
      """  DocCovenantDiscount  """  
      self.Rpt1CovenantDiscount:int = obj["Rpt1CovenantDiscount"]
      """  Rpt1CovenantDiscount  """  
      self.Rpt2CovenantDiscount:int = obj["Rpt2CovenantDiscount"]
      """  Rpt2CovenantDiscount  """  
      self.Rpt3CovenantDiscount:int = obj["Rpt3CovenantDiscount"]
      """  Rpt3CovenantDiscount  """  
      self.TotalInCovenantDiscount:int = obj["TotalInCovenantDiscount"]
      """  TotalInCovenantDiscount  """  
      self.DocInCovenantDiscount:int = obj["DocInCovenantDiscount"]
      """  DocInCovenantDiscount  """  
      self.Rpt1InCovenantDiscount:int = obj["Rpt1InCovenantDiscount"]
      """  Rpt1InCovenantDiscount  """  
      self.Rpt2InCovenantDiscount:int = obj["Rpt2InCovenantDiscount"]
      """  Rpt2InCovenantDiscount  """  
      self.ABAmt:int = obj["ABAmt"]
      """  Total advanced billing amount.  """  
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      """  Indicates if changes can occur after the document has been printed  """  
      self.Rpt3InCovenantDiscount:int = obj["Rpt3InCovenantDiscount"]
      """  Rpt3InCovenantDiscount  """  
      self.ARPNHeadNum:int = obj["ARPNHeadNum"]
      """  ARPNHead's HeadNum  """  
      self.ARPromNoteID:str = obj["ARPromNoteID"]
      """  when InvcHead.PIPayment = O then populate ARPaymentInstrumentID with a value of PI.  """  
      self.AutoGenPN:bool = obj["AutoGenPN"]
      """  Auto generate payment instruments  """  
      self.AvailBTCustList:str = obj["AvailBTCustList"]
      """  Delimited list of available bill to customers.  """  
      self.BankForPI:str = obj["BankForPI"]
      """  Used for Bill of Exchange.  Indicates the bank to use when a payment instrument for the invoice is created.  """  
      self.BankForPIName:str = obj["BankForPIName"]
      self.BTCustID:str = obj["BTCustID"]
      """  Customer ID for the bill to customer (InvcHead.CustNum).  """  
      self.BTCustomerName:str = obj["BTCustomerName"]
      """  Bill to customer name.  """  
      self.ChangeDateTime:str = obj["ChangeDateTime"]
      """  The date and time that the record was last changed  """  
      self.CNGTIAction:str = obj["CNGTIAction"]
      self.CNGTIAddress:str = obj["CNGTIAddress"]
      self.CNGTIBankAccount:str = obj["CNGTIBankAccount"]
      self.CNGTIComment:str = obj["CNGTIComment"]
      self.CNGTICustomerName:str = obj["CNGTICustomerName"]
      self.CNGTIExportAddress:str = obj["CNGTIExportAddress"]
      self.CNGTIGrossInvcAmt:int = obj["CNGTIGrossInvcAmt"]
      """  CSF China, Gross Invoice Amount  """  
      self.CNGTIInvoiceAmt:int = obj["CNGTIInvoiceAmt"]
      """  CSF China, Total invoice amount = InvcHead.InvoiceAmt - InvcHead.WithholdAmt  """  
      self.CNGTINote:str = obj["CNGTINote"]
      self.CNGTIShipToNum:str = obj["CNGTIShipToNum"]
      self.CNGTIStatus1:str = obj["CNGTIStatus1"]
      self.CNGTIStatus2:bool = obj["CNGTIStatus2"]
      self.CNGTITaxCode:str = obj["CNGTITaxCode"]
      self.COIFRSCalculation:bool = obj["COIFRSCalculation"]
      """  IFRS Calculation. If the checkbox is not checked then all the elements below are disabled. If the checkbox is checked, then some elements below become enabled showing default values so that the NPV can be calculated  """  
      self.COIFRSEnabled:bool = obj["COIFRSEnabled"]
      """  If true then Colombia IFRS Net Present Value calculation is enabled  """  
      self.COIFRSFinancialCharge:int = obj["COIFRSFinancialCharge"]
      """  Financial Charge  """  
      self.COIFRSInterestRate:int = obj["COIFRSInterestRate"]
      self.COIFRSNumberOfPeriods:int = obj["COIFRSNumberOfPeriods"]
      """  Number of Periods for payment  """  
      self.COIFRSPresentValue:int = obj["COIFRSPresentValue"]
      """  Present Value  """  
      self.CollectionsInv:bool = obj["CollectionsInv"]
      """  Indicates if Invoice is in Collections (Peru localization)  """  
      self.ContactEmailAddr:str = obj["ContactEmailAddr"]
      """  Contact email address.  """  
      self.ContactFaxNum:str = obj["ContactFaxNum"]
      """  Contact fax number  """  
      self.ContactName:str = obj["ContactName"]
      """  Contact name  """  
      self.ContactPhoneNum:str = obj["ContactPhoneNum"]
      """  Contact phone number  """  
      self.ConvertedFromDep:bool = obj["ConvertedFromDep"]
      """  record converted from deposit  """  
      self.COOperTypeDesc:str = obj["COOperTypeDesc"]
      self.CountryIntrastat:bool = obj["CountryIntrastat"]
      """  True if the Country set for the current company contains an Intrastat code.  """  
      self.CumulativeBalance:int = obj["CumulativeBalance"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      """  Currncy switch used to determine what currency to display amounts in.  """  
      self.CurrentInstanceNum:int = obj["CurrentInstanceNum"]
      self.CustAllowOTS:bool = obj["CustAllowOTS"]
      self.CustOnCreditHold:bool = obj["CustOnCreditHold"]
      self.DepBal:int = obj["DepBal"]
      """  Deposit balance from CashHed  """  
      self.DepositCreditEnabled:bool = obj["DepositCreditEnabled"]
      """  Deposit credit enabled flag.  """  
      self.DirectDebiting:bool = obj["DirectDebiting"]
      self.DisableAplDate:bool = obj["DisableAplDate"]
      """  The flag to indicate if Invoice Header Apply Date is supposed to be Read Only  """  
      self.DispBalDN:int = obj["DispBalDN"]
      """  The net of Invoice Balance and unposted Debit Note value(s) applied to the invoice during one particular Cash Receipt application.  """  
      self.DisplayBillAddr:str = obj["DisplayBillAddr"]
      """  Bill to address in list format.  """  
      self.DisplayCreditCardNum:str = obj["DisplayCreditCardNum"]
      """  Display field for the masked credit card number  """  
      self.DisplayCurrencyID:str = obj["DisplayCurrencyID"]
      self.DisplaySymbol:str = obj["DisplaySymbol"]
      """  Currency display symbol  """  
      self.DNPmtAmt:int = obj["DNPmtAmt"]
      """  The unposted Debit Note value(s) applied to the invoice during the particular invoice payment transaction.  """  
      self.DocABAmt:int = obj["DocABAmt"]
      """  Document Total advanced billing amount.  """  
      self.DocCOIFRSFinancialCharge:int = obj["DocCOIFRSFinancialCharge"]
      """  Financial Charge  """  
      self.DocCOIFRSPresentValue:int = obj["DocCOIFRSPresentValue"]
      """  Present Value  """  
      self.DocCumulativeBalance:int = obj["DocCumulativeBalance"]
      self.DocDepBal:int = obj["DocDepBal"]
      """  Document deposit amount from cashhead.  """  
      self.DocDispBalDN:int = obj["DocDispBalDN"]
      """  The net of Invoice Balance and unposted Debit Note value(s) applied to the invoice during one particular Cash Receipt application.  """  
      self.DocDisplaySymbol:str = obj["DocDisplaySymbol"]
      """  Document display symbol  """  
      self.DocDNPmtAmt:int = obj["DocDNPmtAmt"]
      """  The unposted Debit Note value(s) applied to the invoice during the particular invoice payment transaction.  """  
      self.DocDspPrepDeposit:int = obj["DocDspPrepDeposit"]
      self.DocDspTaxAmt:int = obj["DocDspTaxAmt"]
      self.DocPESUNATDepAmt:int = obj["DocPESUNATDepAmt"]
      """  CSF Peru - SUNAT Deposit Amount  """  
      self.DocRemainTaxAmt:int = obj["DocRemainTaxAmt"]
      self.DocReverseTaxAmt:int = obj["DocReverseTaxAmt"]
      self.DocSATaxAmt:int = obj["DocSATaxAmt"]
      self.DocSourceRecurBalance:int = obj["DocSourceRecurBalance"]
      self.DocSubTotal:int = obj["DocSubTotal"]
      """  Document sub total  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Document Total tax amount from InvcTax for Collection type 'Invoice'  """  
      self.DocVr:int = obj["DocVr"]
      """  Difference between Deposit Amount from invoice header and Total Line Amount in document currency.  """  
      self.DocWHTaxAmt:int = obj["DocWHTaxAmt"]
      self.DspABAmt:int = obj["DspABAmt"]
      """  Display advance billing amount  """  
      self.DspDepBal:int = obj["DspDepBal"]
      """  Display deposit balance.  """  
      self.DspDepCr:int = obj["DspDepCr"]
      """  Display deposit credit.  """  
      self.DspDigitalSignature:str = obj["DspDigitalSignature"]
      self.DspDocABAmt:int = obj["DspDocABAmt"]
      """  Display document advance billing amount  """  
      self.DspDocDepBal:int = obj["DspDocDepBal"]
      """  Display document deposit balance  """  
      self.DspDocDepCr:int = obj["DspDocDepCr"]
      """  Display document deposit credit.  """  
      self.DspDocInvoiceAmt:int = obj["DspDocInvoiceAmt"]
      """  Display document invoice amount  """  
      self.DspDocInvoiceBal:int = obj["DspDocInvoiceBal"]
      """  Display document invoice balance  """  
      self.DspDocRounding:int = obj["DspDocRounding"]
      """  Display Invoice Doc Rounding  """  
      self.DspDocSubTotal:int = obj["DspDocSubTotal"]
      """  display document sub total  """  
      self.DspInvoiceAmt:int = obj["DspInvoiceAmt"]
      """  Display invoice amount  """  
      self.DspInvoiceBal:int = obj["DspInvoiceBal"]
      """  Display Invoice Balance.  """  
      self.DspInvoiceRef:int = obj["DspInvoiceRef"]
      """  Display invoice reference  """  
      self.DspPayDiscDays:str = obj["DspPayDiscDays"]
      self.DspPrepDeposit:int = obj["DspPrepDeposit"]
      self.DspRounding:int = obj["DspRounding"]
      """  Display Rounding in Base  """  
      self.dspSoldToCustID:str = obj["dspSoldToCustID"]
      """  If SoldTo and Alt-Bill to are the same, this displays as null.  """  
      self.DspSubTotal:int = obj["DspSubTotal"]
      """  Display sub total  """  
      self.DspTaxAmt:int = obj["DspTaxAmt"]
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      """  Indicates if assign legal number option is available.  """  
      self.EnableCentralCollection:bool = obj["EnableCentralCollection"]
      self.EnableSOCCDefaults:bool = obj["EnableSOCCDefaults"]
      """  Flag to determine if UseSOCCDefaults should be enabled.  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      """  Indicates if TranDocTypeID is available for input.  """  
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      """  Indicates if the void legal number option is available  """  
      self.ERSInvoice:bool = obj["ERSInvoice"]
      """  It will be displayed to identify invoices automatically generated due ERS shipments.  """  
      self.ExchangeRateDate:str = obj["ExchangeRateDate"]
      """  Indicates which date to be used to calculate the exchange rate, I for Invoice Date, A for Apply Date.  """  
      self.GenedFromRMA:bool = obj["GenedFromRMA"]
      """  Flag for update of InvcHead to allow when group id is "RMACRREQ"  """  
      self.HasBank:bool = obj["HasBank"]
      """  CustBank record exists for customer  """  
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      """  Indicates if a legal number configuration exists for ar invoices/credit memos  """  
      self.InPriceLn:bool = obj["InPriceLn"]
      """  In case if Invoice Header Tax Liability is not assigned this flag indicates if any of Invoice lines has Tax inclusive Tax Liability assinged  """  
      self.IntInvoiceType:str = obj["IntInvoiceType"]
      """  Integration invoice type.  Used for setting of InvoiceType.  """  
      self.InvoiceTypeDesc:str = obj["InvoiceTypeDesc"]
      """  InvoiceType description  """  
      self.IsDK:bool = obj["IsDK"]
      """  Denmark localization external field  """  
      self.IsIntrastatSensitive:bool = obj["IsIntrastatSensitive"]
      """  Set to true if intrastat is enabled.  """  
      self.IsLatestRecurrence:bool = obj["IsLatestRecurrence"]
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.IsPIUnappliedReceipt:bool = obj["IsPIUnappliedReceipt"]
      """  Indicates if the UR Invoice was created from an On Account PI instead of an on account cash receipt.  """  
      self.IsPMForGenPIType:bool = obj["IsPMForGenPIType"]
      self.LatestInvoice:int = obj["LatestInvoice"]
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      """  Stores the message when a legal number is generated.  """  
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.MXCancellationID:str = obj["MXCancellationID"]
      """  MXCancellationID  """  
      self.MXCancellationStatus:str = obj["MXCancellationStatus"]
      """  MXCancellationStatus  """  
      self.NeedConfirmTaxes:bool = obj["NeedConfirmTaxes"]
      """  It indicates that this Invoice has taxes, for which the confirmation is required.  """  
      self.NextDiscDate:str = obj["NextDiscDate"]
      """  This field is to display in Cash Receipt Entry the Discount Date that the payment will take.  """  
      self.NextInvoiceDate:str = obj["NextInvoiceDate"]
      """  NextInvoiceDate = InvcRecurringCycle.LastDate + RecurringCycle.Interval in RecurringCycle.Modifier units  """  
      self.PackSlipNum:int = obj["PackSlipNum"]
      """  Pack slip number from the 1st line item.  """  
      self.PaySchedEnabled:bool = obj["PaySchedEnabled"]
      """  Pay schedule enabled flag  """  
      self.PEBOEChangeStatusTo:str = obj["PEBOEChangeStatusTo"]
      """  Indicates what the user will change the status to  """  
      self.PEBOEStatusDesc:str = obj["PEBOEStatusDesc"]
      self.PECollectionsDate:str = obj["PECollectionsDate"]
      """  Peru CSF: Collections date  """  
      self.PEDetrGoodServiceCodeDesc:str = obj["PEDetrGoodServiceCodeDesc"]
      """  PE Detraction good or service code description  """  
      self.PEDspCurrencySymbol:str = obj["PEDspCurrencySymbol"]
      self.PEInCollections:bool = obj["PEInCollections"]
      """  Peru CSF: No if the invoice is moved out of collections, Yes if the invoice is moved into colletions.  """  
      self.PERefDocumentTypeDesc:str = obj["PERefDocumentTypeDesc"]
      """  PE Document Type Description  """  
      self.PERefDocumentTypeDesc2:str = obj["PERefDocumentTypeDesc2"]
      """  PE Document Type Description 2  """  
      self.PERefDocumentTypeDesc3:str = obj["PERefDocumentTypeDesc3"]
      """  PE Document Type Description 3  """  
      self.PERefDocumentTypeDesc4:str = obj["PERefDocumentTypeDesc4"]
      """  PE Document Type Description 4  """  
      self.PERefDocumentTypeDesc5:str = obj["PERefDocumentTypeDesc5"]
      """  PE Document Type Description 5  """  
      self.PIBankAcctID:str = obj["PIBankAcctID"]
      """  PI - Bank account  """  
      self.PICustBankDtl:bool = obj["PICustBankDtl"]
      """  PI Customer bank required  """  
      self.PIInitiation:str = obj["PIInitiation"]
      """  PI Initiation - generated or received  """  
      self.PrepDepositEnabled:bool = obj["PrepDepositEnabled"]
      """  Prep Deposit enabled flag.  """  
      self.ProposedTaxRgn:str = obj["ProposedTaxRgn"]
      """  The description of the proposed Tax Region  """  
      self.RecalcAmts:str = obj["RecalcAmts"]
      """   This field indicates id all the amounts related to the invoice are supposed to be re-calculated on change of the Applate Date.
"R" - the user's answer is recalculate the amounts
"N" the user's answer is  do not recalculate the amount
Blank - user is not asked  """  
      self.Recurring:bool = obj["Recurring"]
      """  Recurring flag  """  
      self.RemainTaxAmt:int = obj["RemainTaxAmt"]
      self.ReminderSeq:int = obj["ReminderSeq"]
      self.ReversalDocAmt:int = obj["ReversalDocAmt"]
      """  Accumulate all reversal amounts of Credit Memos with the reference to the invoice  """  
      self.ReverseTaxAmt:int = obj["ReverseTaxAmt"]
      self.Rpt1ABAmt:int = obj["Rpt1ABAmt"]
      self.Rpt1COIFRSFinancialCharge:int = obj["Rpt1COIFRSFinancialCharge"]
      """  Financial Charge  """  
      self.Rpt1COIFRSPresentValue:int = obj["Rpt1COIFRSPresentValue"]
      """  Present Value  """  
      self.Rpt1CumulativeBalance:int = obj["Rpt1CumulativeBalance"]
      self.Rpt1DepBal:int = obj["Rpt1DepBal"]
      self.Rpt1DspABAmt:int = obj["Rpt1DspABAmt"]
      self.Rpt1DspDepBal:int = obj["Rpt1DspDepBal"]
      self.Rpt1DspDepCr:int = obj["Rpt1DspDepCr"]
      self.Rpt1DspInvoiceAmt:int = obj["Rpt1DspInvoiceAmt"]
      self.Rpt1DspInvoiceBal:int = obj["Rpt1DspInvoiceBal"]
      self.Rpt1DspPrepDeposit:int = obj["Rpt1DspPrepDeposit"]
      self.Rpt1DspRounding:int = obj["Rpt1DspRounding"]
      self.Rpt1DspSubTotal:int = obj["Rpt1DspSubTotal"]
      self.Rpt1DspTaxAmt:int = obj["Rpt1DspTaxAmt"]
      self.Rpt1RemainTaxAmt:int = obj["Rpt1RemainTaxAmt"]
      self.Rpt1ReverseTaxAmt:int = obj["Rpt1ReverseTaxAmt"]
      self.Rpt1SATaxAmt:int = obj["Rpt1SATaxAmt"]
      self.Rpt1SourceRecurBalance:int = obj["Rpt1SourceRecurBalance"]
      self.Rpt1SubTotal:int = obj["Rpt1SubTotal"]
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      self.Rpt1Vr:int = obj["Rpt1Vr"]
      """  Difference between Deposit Amount from invoice header and Total Line Amount in Rpt1 currency.  """  
      self.Rpt1WHTaxAmt:int = obj["Rpt1WHTaxAmt"]
      self.Rpt2ABAmt:int = obj["Rpt2ABAmt"]
      self.Rpt2COIFRSFinancialCharge:int = obj["Rpt2COIFRSFinancialCharge"]
      """  Financial Charge  """  
      self.Rpt2COIFRSPresentValue:int = obj["Rpt2COIFRSPresentValue"]
      """  Present Value  """  
      self.Rpt2CumulativeBalance:int = obj["Rpt2CumulativeBalance"]
      self.Rpt2DepBal:int = obj["Rpt2DepBal"]
      self.Rpt2DspABAmt:int = obj["Rpt2DspABAmt"]
      self.Rpt2DspDepBal:int = obj["Rpt2DspDepBal"]
      self.Rpt2DspDepCr:int = obj["Rpt2DspDepCr"]
      self.Rpt2DspInvoiceAmt:int = obj["Rpt2DspInvoiceAmt"]
      self.Rpt2DspInvoiceBal:int = obj["Rpt2DspInvoiceBal"]
      self.Rpt2DspPrepDeposit:int = obj["Rpt2DspPrepDeposit"]
      self.Rpt2DspRounding:int = obj["Rpt2DspRounding"]
      self.Rpt2DspSubTotal:int = obj["Rpt2DspSubTotal"]
      self.Rpt2DspTaxAmt:int = obj["Rpt2DspTaxAmt"]
      self.Rpt2RemainTaxAmt:int = obj["Rpt2RemainTaxAmt"]
      self.Rpt2ReverseTaxAmt:int = obj["Rpt2ReverseTaxAmt"]
      self.Rpt2SATaxAmt:int = obj["Rpt2SATaxAmt"]
      self.Rpt2SourceRecurBalance:int = obj["Rpt2SourceRecurBalance"]
      self.Rpt2SubTotal:int = obj["Rpt2SubTotal"]
      self.Rpt2Taxamt:int = obj["Rpt2Taxamt"]
      self.Rpt2Vr:int = obj["Rpt2Vr"]
      """  Difference between Deposit Amount from invoice header and Total Line Amount in Rpt2 currency.  """  
      self.Rpt2WHTaxAmt:int = obj["Rpt2WHTaxAmt"]
      self.Rpt3ABAmt:int = obj["Rpt3ABAmt"]
      self.Rpt3COIFRSFinancialCharge:int = obj["Rpt3COIFRSFinancialCharge"]
      """  Financial Charge  """  
      self.Rpt3COIFRSPresentValue:int = obj["Rpt3COIFRSPresentValue"]
      """  Present Value  """  
      self.Rpt3CumulativeBalance:int = obj["Rpt3CumulativeBalance"]
      self.Rpt3DepBal:int = obj["Rpt3DepBal"]
      self.Rpt3DspABAmt:int = obj["Rpt3DspABAmt"]
      self.Rpt3DspDepBal:int = obj["Rpt3DspDepBal"]
      self.Rpt3DspDepCr:int = obj["Rpt3DspDepCr"]
      self.Rpt3DspInvoiceAmt:int = obj["Rpt3DspInvoiceAmt"]
      self.Rpt3DspInvoiceBal:int = obj["Rpt3DspInvoiceBal"]
      self.Rpt3DspPrepDeposit:int = obj["Rpt3DspPrepDeposit"]
      self.Rpt3DspRounding:int = obj["Rpt3DspRounding"]
      self.Rpt3DspSubTotal:int = obj["Rpt3DspSubTotal"]
      self.Rpt3DspTaxAmt:int = obj["Rpt3DspTaxAmt"]
      self.Rpt3RemainTaxAmt:int = obj["Rpt3RemainTaxAmt"]
      self.Rpt3ReverseTaxAmt:int = obj["Rpt3ReverseTaxAmt"]
      self.Rpt3SATaxAmt:int = obj["Rpt3SATaxAmt"]
      self.Rpt3SourceRecurBalance:int = obj["Rpt3SourceRecurBalance"]
      self.Rpt3SubTotal:int = obj["Rpt3SubTotal"]
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      self.Rpt3Vr:int = obj["Rpt3Vr"]
      """  Difference between Deposit Amount from invoice header and Total Line Amount in Rpt3 currency.  """  
      self.Rpt3WHTaxAmt:int = obj["Rpt3WHTaxAmt"]
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.SalesRepCode1:str = obj["SalesRepCode1"]
      """  1st entry in SalesRepList  """  
      self.SalesRepCode2:str = obj["SalesRepCode2"]
      """  2nd entry in SalesRepList  """  
      self.SalesRepCode3:str = obj["SalesRepCode3"]
      """  3rd entry in SalesRepList.  """  
      self.SalesRepCode4:str = obj["SalesRepCode4"]
      """  4th entry in SalesRepList  """  
      self.SalesRepCode5:str = obj["SalesRepCode5"]
      """  5th entry in SalesRepList  """  
      self.SalesRepName1:str = obj["SalesRepName1"]
      """  1st sales rep name  """  
      self.SalesRepName2:str = obj["SalesRepName2"]
      """  2nd sales rep name  """  
      self.SalesRepName3:str = obj["SalesRepName3"]
      """  3rd sales rep name  """  
      self.SalesRepName4:str = obj["SalesRepName4"]
      """  4th sales rep name  """  
      self.SalesRepName5:str = obj["SalesRepName5"]
      """  5th sales rep name  """  
      self.SATaxAmt:int = obj["SATaxAmt"]
      self.Selected:bool = obj["Selected"]
      """  Boolean for selection of invoices in grid  """  
      self.SkipRecurring:bool = obj["SkipRecurring"]
      self.SoldToAddressList:str = obj["SoldToAddressList"]
      """  Sold to address list.  """  
      self.SoldToCustID:str = obj["SoldToCustID"]
      """  Sold to customer id  """  
      self.SoldToCustomerName:str = obj["SoldToCustomerName"]
      """  Sold to customer name.  """  
      self.SourceInvoiceNum:int = obj["SourceInvoiceNum"]
      self.SourceLastDate:str = obj["SourceLastDate"]
      self.SourceRecurBalance:int = obj["SourceRecurBalance"]
      self.SubTotal:int = obj["SubTotal"]
      """  Sub total for invoice  """  
      self.SystemTranType:str = obj["SystemTranType"]
      """  The system transaction type - ARInvoice or CreditMemo.  Used to filter combo list for TranDocTypeID.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Total tax amount from InvcTax  """  
      self.TaxExchangeRate:int = obj["TaxExchangeRate"]
      self.TaxRgnLineChange:bool = obj["TaxRgnLineChange"]
      """  The flag to indicate if the user is supposed to be asked about Tax Liability change  """  
      self.TotalInstanceNum:int = obj["TotalInstanceNum"]
      self.TransApplyDate:str = obj["TransApplyDate"]
      """  This field is used when invoice is transferred to another Invoice Group and the user has a chance to change the Apply date of the invoice transferred.  """  
      self.UseSOCCDefaults:bool = obj["UseSOCCDefaults"]
      """  If true, the credit card info will come from the sales order.  """  
      self.UseTaxRate:bool = obj["UseTaxRate"]
      self.VNInvDescription:str = obj["VNInvDescription"]
      self.VNInvoiceType:str = obj["VNInvoiceType"]
      self.Vr:int = obj["Vr"]
      """  Difference between Deposit Amount from invoice header and Total Line Amount in base currency.  """  
      self.WHTaxAmt:int = obj["WHTaxAmt"]
      self.XRateLabel:str = obj["XRateLabel"]
      """  Currency label  """  
      self.zEnableCreditHold:bool = obj["zEnableCreditHold"]
      self.AgingDays:int = obj["AgingDays"]
      """  The number of days the invoice is past due.  """  
      self.ELIEInvProhibitedStatuses:str = obj["ELIEInvProhibitedStatuses"]
      """   The list of prohibited statuses.for the Invoice
For examle, if contains 2 (EINVOICE_STATUS_GENERATED) then Generate E-invoice is not allowed.
if contains 2 (EINVOICE_STATUS_SENT) then Sending Invoice via Service provider is not allowed  """  
      self.EnableIncotermLocation:bool = obj["EnableIncotermLocation"]
      """  Flag indicating whether to enable Incoterm Location  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AGInvoicingPointDescription:str = obj["AGInvoicingPointDescription"]
      self.ARSystLNReqForInvc:bool = obj["ARSystLNReqForInvc"]
      self.CardTypeDescription:str = obj["CardTypeDescription"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrRateGrpDescription:str = obj["CurrRateGrpDescription"]
      self.CustomerInactive:bool = obj["CustomerInactive"]
      self.CustomerMXGeneralPublic:bool = obj["CustomerMXGeneralPublic"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerELISendingOption:int = obj["CustomerELISendingOption"]
      self.FOBDescription:str = obj["FOBDescription"]
      self.IncotermsDescription:str = obj["IncotermsDescription"]
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      self.MXPurchaseTypeCodeDesc:str = obj["MXPurchaseTypeCodeDesc"]
      self.MXSubstInvoiceMXFiscalFolio:str = obj["MXSubstInvoiceMXFiscalFolio"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.OurBankPayerRef:str = obj["OurBankPayerRef"]
      self.OurBankBankIdentifier:str = obj["OurBankBankIdentifier"]
      self.OurBankTypeCode:str = obj["OurBankTypeCode"]
      self.OurBankBankAcctID:str = obj["OurBankBankAcctID"]
      self.OurBankCheckingAccount:str = obj["OurBankCheckingAccount"]
      self.OurBankBankName:str = obj["OurBankBankName"]
      self.OurBankIBANCode:str = obj["OurBankIBANCode"]
      self.OurBankLocalBIC:str = obj["OurBankLocalBIC"]
      self.OurBankDescription:str = obj["OurBankDescription"]
      self.PayMethodName:str = obj["PayMethodName"]
      self.PayMethodSummarizePerCustomer:bool = obj["PayMethodSummarizePerCustomer"]
      self.PayMethodType:int = obj["PayMethodType"]
      self.PlantName:str = obj["PlantName"]
      self.ProjectDescription:str = obj["ProjectDescription"]
      self.RecurringCycleMaximumValue:bool = obj["RecurringCycleMaximumValue"]
      self.SoldToCustNumInactive:bool = obj["SoldToCustNumInactive"]
      self.SoldToCustNumCustID:str = obj["SoldToCustNumCustID"]
      self.SoldToCustNumName:str = obj["SoldToCustNumName"]
      self.TaxRateGrpDescription:str = obj["TaxRateGrpDescription"]
      self.TaxRegionDescription:str = obj["TaxRegionDescription"]
      self.TermsCodeDescription:str = obj["TermsCodeDescription"]
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      self.XbSystOCRCalcType:bool = obj["XbSystOCRCalcType"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_InvcsForCustTableset:
   def __init__(self, obj):
      self.InvcHead:list[Erp_Tablesets_InvcHeadRow] = obj["InvcHead"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
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

class Erp_Tablesets_PITotalsRow:
   def __init__(self, obj):
      self.CashRcv:int = obj["CashRcv"]
      self.DocCashRcv:int = obj["DocCashRcv"]
      self.DocDscTaken:int = obj["DocDscTaken"]
      self.DocGainReal:int = obj["DocGainReal"]
      self.DocGainUnreal:int = obj["DocGainUnreal"]
      self.DscTaken:int = obj["DscTaken"]
      self.GainReal:int = obj["GainReal"]
      self.GainUnreal:int = obj["GainUnreal"]
      self.RevalDate:str = obj["RevalDate"]
      self.Rpt1CashRcv:int = obj["Rpt1CashRcv"]
      self.Rpt1DscTaken:int = obj["Rpt1DscTaken"]
      self.Rpt1GainReal:int = obj["Rpt1GainReal"]
      self.Rpt1GainUnreal:int = obj["Rpt1GainUnreal"]
      self.Rpt2CashRcv:int = obj["Rpt2CashRcv"]
      self.Rpt2DscTaken:int = obj["Rpt2DscTaken"]
      self.Rpt2GainReal:int = obj["Rpt2GainReal"]
      self.Rpt2GainUnreal:int = obj["Rpt2GainUnreal"]
      self.Rpt3CashRcv:int = obj["Rpt3CashRcv"]
      self.Rpt3DscTaken:int = obj["Rpt3DscTaken"]
      self.Rpt3GainReal:int = obj["Rpt3GainReal"]
      self.Rpt3GainUnreal:int = obj["Rpt3GainUnreal"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PNSummaryRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PromNoteID:str = obj["PromNoteID"]
      """  Payment Instrument ID  """  
      self.Type:str = obj["Type"]
      """  Type  """  
      self.PIStatus:str = obj["PIStatus"]
      """  Status  """  
      self.PIStage:str = obj["PIStage"]
      """  Stage  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.LegalNumber:str = obj["LegalNumber"]
      self.IssueDate:str = obj["IssueDate"]
      self.DueDate:str = obj["DueDate"]
      self.DiscountAmt:int = obj["DiscountAmt"]
      self.DocDiscountAmount:int = obj["DocDiscountAmount"]
      self.Rpt1DiscountAmt:int = obj["Rpt1DiscountAmt"]
      self.Rpt2DiscountAmt:int = obj["Rpt2DiscountAmt"]
      self.Rpt3DiscountAmt:int = obj["Rpt3DiscountAmt"]
      self.TranAmt:int = obj["TranAmt"]
      self.DocTranAmt:int = obj["DocTranAmt"]
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      self.Posted:bool = obj["Posted"]
      self.DNAmount:int = obj["DNAmount"]
      self.DocDNAmount:int = obj["DocDNAmount"]
      self.Rpt1DNAmount:int = obj["Rpt1DNAmount"]
      self.Rpt2DNAmount:int = obj["Rpt2DNAmount"]
      self.Rpt3DNAmount:int = obj["Rpt3DNAmount"]
      self.TranDate:str = obj["TranDate"]
      self.CustNum:int = obj["CustNum"]
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  InvoiceNum  """  
      self.GainLossType:str = obj["GainLossType"]
      self.RevalueDate:str = obj["RevalueDate"]
      self.RevalueBal:int = obj["RevalueBal"]
      self.DocRevalueBal:int = obj["DocRevalueBal"]
      self.Rpt1RevalueBal:int = obj["Rpt1RevalueBal"]
      self.Rpt2RevalueBal:int = obj["Rpt2RevalueBal"]
      self.Rpt3RevalueBal:int = obj["Rpt3RevalueBal"]
      self.TranType:str = obj["TranType"]
      self.Reference:str = obj["Reference"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PNSummaryTableset:
   def __init__(self, obj):
      self.PNSummary:list[Erp_Tablesets_PNSummaryRow] = obj["PNSummary"]
      self.PITotals:list[Erp_Tablesets_PITotalsRow] = obj["PITotals"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_TaxDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SourceModule:str = obj["SourceModule"]
      """   Indicates the module that created this tax detail.  This is assigned by the system.
Values can be; AR, AP.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  HeadNum  """  
      self.APTranNo:int = obj["APTranNo"]
      """  Integer assigned by the system copied from APTran.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  Taxable amount for this invoice. Manually entered if the currency is the base currency.  """  
      self.DocTaxableAmt:int = obj["DocTaxableAmt"]
      """  Taxable amount for this invoice in foreign currency. Manually entered.  """  
      self.Percent:int = obj["Percent"]
      """  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount. Manually entered if the currency is the base currency.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount in foreign currency. Manually entered.  """  
      self.ReverseCharge:bool = obj["ReverseCharge"]
      """  Reverse Charge.  """  
      self.Rpt1TaxableAmt:int = obj["Rpt1TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxableAmt:int = obj["Rpt2TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxableAmt:int = obj["Rpt3TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.RateCode:str = obj["RateCode"]
      """  Rate Code  """  
      self.CollectionType:int = obj["CollectionType"]
      """  Collection Type  """  
      self.Timing:int = obj["Timing"]
      """  Timing of when to report taxes  """  
      self.ExemptType:int = obj["ExemptType"]
      """  Exemption Type  """  
      self.ExemptPercent:int = obj["ExemptPercent"]
      """  Exemption Percent  """  
      self.ResolutionNum:str = obj["ResolutionNum"]
      """  Resolution Number  """  
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
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  The open A/R invoice # that the transaction applies against. Not used by the MisPay trantype. In the case of PayInv, or CMemo transaction this must be a valid InvcHead record where InvcHead.CreditMemo = No. In case of "Adjust" transactions this can be either a invoice or a credit memo reference. Note: The "Apply Credit Memo" program automatically creates an additional CashDtl records for each invoice to which the credit memo is applied.  In this additional record this field contains the credit memo's number.  """  
      self.InvoiceRef:int = obj["InvoiceRef"]
      """  Applicable to CMemo transaction types only. The "Apply Credit Memo" program creates two CashDtl records for each invoice that a credit memo is applied to. One record for the <credit> to the invoice and a second record for the debit to the credit memo. In the first record this field is the InvoiceNum of the Credit memo. In the second record it is the InvoiceNum of the invoice that the credit memo was applied to.  """  
      self.ECAcquisitionSeq:int = obj["ECAcquisitionSeq"]
      """   Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.
NOTE:  This field is now used in VAT Reverse Charge logic.  If an invoice line is marked for Reverse Charge, a second line is created just like in the ECAcquisition logic. To distinguish the two scenarios, the ReverseCharge flag will be set to true if the second line is for Reverse Charge.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Relates record to a BankAcct.  """  
      self.TranNum:int = obj["TranNum"]
      """  Unique ID of the Transaction.  """  
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
      self.Manual:bool = obj["Manual"]
      """  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  """  
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
      self.DiscTaxAdj:int = obj["DiscTaxAdj"]
      """  Discount Tax Adjustment  """  
      self.DocDiscTaxAdj:int = obj["DocDiscTaxAdj"]
      """  Discount Tax Adjustment in foreign currency.  """  
      self.Rpt1DiscTaxAdj:int = obj["Rpt1DiscTaxAdj"]
      """  Reporting currency value of this field  """  
      self.Rpt2DiscTaxAdj:int = obj["Rpt2DiscTaxAdj"]
      """  Reporting currency value of this field  """  
      self.Rpt3DiscTaxAdj:int = obj["Rpt3DiscTaxAdj"]
      """  Reporting currency value of this field  """  
      self.DiscTaxableAdj:int = obj["DiscTaxableAdj"]
      """  Discount Taxable Adjustment  """  
      self.DocDiscTaxableAdj:int = obj["DocDiscTaxableAdj"]
      """  Discount Taxable Adjustment in foreign currency.  """  
      self.Rpt1DiscTaxableAdj:int = obj["Rpt1DiscTaxableAdj"]
      """  Reporting currency value of this field  """  
      self.Rpt2DiscTaxableAdj:int = obj["Rpt2DiscTaxableAdj"]
      """  Reporting currency value of this field  """  
      self.Rpt3DiscTaxableAdj:int = obj["Rpt3DiscTaxableAdj"]
      """  Reporting currency value of this field  """  
      self.TextCode:str = obj["TextCode"]
      """  Unique Identifier for Legal Text  """  
      self.Voided:bool = obj["Voided"]
      """  Indicates if transaction was voided.  The rest of the unique key will contain the original transaction values (like APTran)  """  
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
      self.DiscTaxAdjVar:int = obj["DiscTaxAdjVar"]
      """  Discount Tax Adjustment Variance  """  
      self.DocDiscTaxAdjVar:int = obj["DocDiscTaxAdjVar"]
      """  Discount Tax Adjustment Variance  """  
      self.Rpt1DiscTaxAdjVar:int = obj["Rpt1DiscTaxAdjVar"]
      """  Reporting currency value of this field  """  
      self.Rpt2DiscTaxAdjVar:int = obj["Rpt2DiscTaxAdjVar"]
      """  Reporting currency value of this field  """  
      self.Rpt3DiscTaxAdjVar:int = obj["Rpt3DiscTaxAdjVar"]
      """  Reporting currency value of this field  """  
      self.PCashDeskID:str = obj["PCashDeskID"]
      """  Unique identifier of Petty Cash Desk  """  
      self.PCashRefNum:int = obj["PCashRefNum"]
      """  Reference Number, unique identifier of Petty Cash Document  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AGOrigTaxableAmt:int = obj["AGOrigTaxableAmt"]
      """  AGOrigTaxableAmt  """  
      self.GainLoss:int = obj["GainLoss"]
      """  GainLoss  """  
      self.DocGainLoss:int = obj["DocGainLoss"]
      """  DocGainLoss  """  
      self.Rpt1GainLoss:int = obj["Rpt1GainLoss"]
      """  Rpt1GainLoss  """  
      self.Rpt2GainLoss:int = obj["Rpt2GainLoss"]
      """  Rpt2GainLoss  """  
      self.Rpt3GainLoss:int = obj["Rpt3GainLoss"]
      """  Rpt3GainLoss  """  
      self.CNCFICode:str = obj["CNCFICode"]
      """  CNCFICode  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  APInvoiceNum  """  
      self.TranType:str = obj["TranType"]
      """  TranType  """  
      self.MovementNum:int = obj["MovementNum"]
      """  MovementNum  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.CNCFICodeDescription:str = obj["CNCFICodeDescription"]
      self.CTDescription:str = obj["CTDescription"]
      self.DisableManual:bool = obj["DisableManual"]
      """  Flag to indicate if Manual checkbos should be Read Only  """  
      self.GroupID:str = obj["GroupID"]
      """  Group ID - used to link to Cash Head  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.DedTaxChanged:bool = obj["DedTaxChanged"]
      """  The flag to indicate if the user changed Deductible Tax amount on manually updated tax record  """  
      self.EnableTax:bool = obj["EnableTax"]
      self.BitFlag:int = obj["BitFlag"]
      self.RateCodeDescription:str = obj["RateCodeDescription"]
      self.TaxCodeDescription:str = obj["TaxCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtARPromissoryNotesTableset:
   def __init__(self, obj):
      self.ARPNHead:list[Erp_Tablesets_ARPNHeadRow] = obj["ARPNHead"]
      self.ARPNHeadAttch:list[Erp_Tablesets_ARPNHeadAttchRow] = obj["ARPNHeadAttch"]
      self.BankTran:list[Erp_Tablesets_BankTranRow] = obj["BankTran"]
      self.BankTranTaxDtl:list[Erp_Tablesets_BankTranTaxDtlRow] = obj["BankTranTaxDtl"]
      self.BankTranTGLC:list[Erp_Tablesets_BankTranTGLCRow] = obj["BankTranTGLC"]
      self.ARPNDtl:list[Erp_Tablesets_ARPNDtlRow] = obj["ARPNDtl"]
      self.TaxDtl:list[Erp_Tablesets_TaxDtlRow] = obj["TaxDtl"]
      self.ARPNHeadTGLC:list[Erp_Tablesets_ARPNHeadTGLCRow] = obj["ARPNHeadTGLC"]
      self.ARPNList:list[Erp_Tablesets_ARPNListRow] = obj["ARPNList"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class FillPNSummary_input:
   """ Required : 
   ipcustNum
   ipStageFilter
   fromDays
   inRange
   """  
   def __init__(self, obj):
      self.ipcustNum:int = obj["ipcustNum"]
      """  The customer number  """  
      self.ipStageFilter:str = obj["ipStageFilter"]
      """  All, Open, Closed, or New  """  
      self.fromDays:int = obj["fromDays"]
      """  the amount of days to get a date from which the invoices will be selected.  """  
      self.inRange:bool = obj["inRange"]
      """  if the invoices will be selected from an specific date.  """  
      pass

class FillPNSummary_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PNSummaryTableset] = obj["returnObj"]
      pass

class GenerateARPNDtl_input:
   """ Required : 
   groupID
   headNum
   invoiceNum
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      """  Cash Group ID  """  
      self.headNum:int = obj["headNum"]
      """  Promissory Note HeadNum  """  
      self.invoiceNum:int = obj["invoiceNum"]
      """  Promissory Note Invoice Num  """  
      pass

class GenerateARPNDtl_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["returnObj"]
      pass

class GenerateARPNDtls_input:
   """ Required : 
   groupID
   custNum
   currencyCode
   invoiceNum
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      """  Cash Group ID  """  
      self.custNum:int = obj["custNum"]
      """  Customer Number  """  
      self.currencyCode:str = obj["currencyCode"]
      """  Currency Code Number  """  
      self.invoiceNum:int = obj["invoiceNum"]
      """  Promissory Note Invoice Num  """  
      pass

class GenerateARPNDtls_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["returnObj"]
      pass

class GetARPNListTracker_input:
   """ Required : 
   ipPNID
   fromTracker
   """  
   def __init__(self, obj):
      self.ipPNID:str = obj["ipPNID"]
      """  ipPNID  """  
      self.fromTracker:bool = obj["fromTracker"]
      """  Indicates if the method was called from the Tracker or the Update program  """  
      pass

class GetARPNListTracker_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["returnObj"]
      pass

class GetARPNList_input:
   """ Required : 
   ipType
   ipPNID
   ipCustID
   """  
   def __init__(self, obj):
      self.ipType:str = obj["ipType"]
      """  ipType  """  
      self.ipPNID:str = obj["ipPNID"]
      """  ipPNID  """  
      self.ipCustID:str = obj["ipCustID"]
      """  ipCustID  """  
      pass

class GetARPNList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["returnObj"]
      pass

class GetARPNMove_input:
   """ Required : 
   iGroupID
   iHeadNum
   """  
   def __init__(self, obj):
      self.iGroupID:str = obj["iGroupID"]
      """  The Group Number  """  
      self.iHeadNum:int = obj["iHeadNum"]
      """  The Header Number  """  
      pass

class GetARPNMove_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ARPNMoveTableset] = obj["returnObj"]
      pass

class GetAvailTranDocTypes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.AvailTypes:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetBankAcctInfo_input:
   """ Required : 
   bankAcctID
   ds
   """  
   def __init__(self, obj):
      self.bankAcctID:str = obj["bankAcctID"]
      """  Proposed BankAcctID  """  
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

class GetBankAcctInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetBankFeeDefaultAccount_input:
   """ Required : 
   bankAcctID
   tranNum
   voided
   ds
   """  
   def __init__(self, obj):
      self.bankAcctID:str = obj["bankAcctID"]
      """  The Bank Account ID  """  
      self.tranNum:int = obj["tranNum"]
      """  The Bank Fee Tran Num  """  
      self.voided:bool = obj["voided"]
      """  voided  """  
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

class GetBankFeeDefaultAccount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   groupID
   headNum
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      self.headNum:int = obj["headNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["returnObj"]
      pass

class GetById4PITracker_input:
   """ Required : 
   ipGroupID
   ipHeadNum
   ds
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  Group ID  """  
      self.ipHeadNum:int = obj["ipHeadNum"]
      """  Head Num  """  
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

class GetById4PITracker_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetBySysRowID_input:
   """ Required : 
   id
   """  
   def __init__(self, obj):
      self.id:str = obj["id"]
      pass

class GetBySysRowID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      self.fieldName:str = obj["fieldName"]
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetCurrencyCodeForBatch_input:
   """ Required : 
   ipGroupID
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  ipGroupID  """  
      pass

class GetCurrencyCodeForBatch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opCurrencyCode:str = obj["parameters"]
      self.opDefaultFound:bool = obj["opDefaultFound"]
      pass

      """  output parameters  """  

class GetCurrencyInfoMaster_input:
   """ Required : 
   currencyCode
   ds
   """  
   def __init__(self, obj):
      self.currencyCode:str = obj["currencyCode"]
      """  Proposed Currency Code  """  
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

class GetCurrencyInfoMaster_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetCurrencyInfo_input:
   """ Required : 
   currencyCode
   ds
   """  
   def __init__(self, obj):
      self.currencyCode:str = obj["currencyCode"]
      """  Proposed Currency Code  """  
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

class GetCurrencyInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetCustPIFlags_input:
   """ Required : 
   custID
   """  
   def __init__(self, obj):
      self.custID:str = obj["custID"]
      """  CustID for Customer  """  
      pass

class GetCustPIFlags_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.autoGenPromNotes:bool = obj["autoGenPromNotes"]
      self.directDebiting:bool = obj["directDebiting"]
      self.hasBank:bool = obj["hasBank"]
      pass

      """  output parameters  """  

class GetCustomerInfo_input:
   """ Required : 
   custID
   ds
   """  
   def __init__(self, obj):
      self.custID:str = obj["custID"]
      """  Proposed Customer ID  """  
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

class GetCustomerInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetDtlInvoiceInfo_input:
   """ Required : 
   invoiceNum
   ds
   """  
   def __init__(self, obj):
      self.invoiceNum:int = obj["invoiceNum"]
      """  Proposed Invoice Number  """  
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

class GetDtlInvoiceInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetDtlLegalNumberInfo_input:
   """ Required : 
   legalNumber
   ds
   """  
   def __init__(self, obj):
      self.legalNumber:str = obj["legalNumber"]
      """  Proposed Legal Number  """  
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

class GetDtlLegalNumberInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetDtlTranAmtInfo_input:
   """ Required : 
   docTranAmt
   ds
   """  
   def __init__(self, obj):
      self.docTranAmt:int = obj["docTranAmt"]
      """  Proposed transaction amount  """  
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

class GetDtlTranAmtInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetEligibleInvcsForSinglGenPI_input:
   """ Required : 
   ipCustID
   ipCurrencyCode
   """  
   def __init__(self, obj):
      self.ipCustID:str = obj["ipCustID"]
      """  customer ID  """  
      self.ipCurrencyCode:str = obj["ipCurrencyCode"]
      """  currency code  """  
      pass

class GetEligibleInvcsForSinglGenPI_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InvcsForCustTableset] = obj["returnObj"]
      pass

class GetExistingGenPI_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

class GetExistingGenPI_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetGLJrnDtl_input:
   """ Required : 
   iGroupID
   iHeadNum
   """  
   def __init__(self, obj):
      self.iGroupID:str = obj["iGroupID"]
      """  The Group Number  """  
      self.iHeadNum:int = obj["iHeadNum"]
      """  The Header Number  """  
      pass

class GetGLJrnDtl_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLJrnDtlMovTableset] = obj["returnObj"]
      pass

class GetGroupIDForPIWithHeadNum_input:
   """ Required : 
   arPromNoteID
   aHeadNum
   """  
   def __init__(self, obj):
      self.arPromNoteID:str = obj["arPromNoteID"]
      """  AR Promissory Note ID  """  
      self.aHeadNum:int = obj["aHeadNum"]
      """  HeadNum ID  """  
      pass

class GetGroupIDForPIWithHeadNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.groupID:str = obj["parameters"]
      self.headNum:int = obj["parameters"]
      pass

      """  output parameters  """  

class GetGroupIDForPI_input:
   """ Required : 
   arPromNoteID
   """  
   def __init__(self, obj):
      self.arPromNoteID:str = obj["arPromNoteID"]
      """  AR Promissory Note ID  """  
      pass

class GetGroupIDForPI_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.groupID:str = obj["parameters"]
      self.headNum:int = obj["parameters"]
      pass

      """  output parameters  """  

class GetHdrInvoiceInfo_input:
   """ Required : 
   invoiceNum
   ds
   """  
   def __init__(self, obj):
      self.invoiceNum:int = obj["invoiceNum"]
      """  Invoice Number to get Customer information from  """  
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

class GetHdrInvoiceInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetHdrLegalNumberInfo_input:
   """ Required : 
   legalNumber
   ds
   """  
   def __init__(self, obj):
      self.legalNumber:str = obj["legalNumber"]
      """  Legal Number to get Customer information from  """  
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

class GetHdrLegalNumberInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetHeadNumForPI_input:
   """ Required : 
   invoiceNum
   """  
   def __init__(self, obj):
      self.invoiceNum:int = obj["invoiceNum"]
      """  Invoice Number  """  
      pass

class GetHeadNumForPI_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.headNum:int = obj["parameters"]
      pass

      """  output parameters  """  

class GetInvcsSinglGenPI_input:
   """ Required : 
   ipCustID
   ipCurrencyCode
   """  
   def __init__(self, obj):
      self.ipCustID:str = obj["ipCustID"]
      """  customer ID  """  
      self.ipCurrencyCode:str = obj["ipCurrencyCode"]
      """  currency code  """  
      pass

class GetInvcsSinglGenPI_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InvcsForCustTableset] = obj["returnObj"]
      pass

class GetLegalNumGenOpts_input:
   """ Required : 
   ipGroupID
   ipHeadNum
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  ARPN group identifier.  """  
      self.ipHeadNum:int = obj["ipHeadNum"]
      """  ARPN header number.  """  
      pass

class GetLegalNumGenOpts_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.opPromptForNum:bool = obj["opPromptForNum"]
      pass

      """  output parameters  """  

class GetLegalNumberInfo_input:
   """ Required : 
   legalNumber
   ds
   """  
   def __init__(self, obj):
      self.legalNumber:str = obj["legalNumber"]
      """  Proposed Legal Number  """  
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

class GetLegalNumberInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetListCustom_input:
   """ Required : 
   type
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.type:str = obj["type"]
      """  PI type  """  
      self.whereClause:str = obj["whereClause"]
      """  Where clause from search  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      pass

class GetListCustom_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ARPNHeadListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

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
      self.returnObj:list[Erp_Tablesets_ARPNHeadListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewARPNDtl_input:
   """ Required : 
   ds
   headNum
   invoiceNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      self.headNum:int = obj["headNum"]
      self.invoiceNum:int = obj["invoiceNum"]
      pass

class GetNewARPNDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewARPNHeadAttch_input:
   """ Required : 
   ds
   groupID
   headNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      self.headNum:int = obj["headNum"]
      pass

class GetNewARPNHeadAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewARPNHeadByGroupID_input:
   """ Required : 
   piGroupID
   ds
   """  
   def __init__(self, obj):
      self.piGroupID:str = obj["piGroupID"]
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

class GetNewARPNHeadByGroupID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewARPNHeadByInvoiceAndAccount_input:
   """ Required : 
   ipBankAcctID
   invoiceNum
   ds
   """  
   def __init__(self, obj):
      self.ipBankAcctID:str = obj["ipBankAcctID"]
      self.invoiceNum:int = obj["invoiceNum"]
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

class GetNewARPNHeadByInvoiceAndAccount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewARPNHeadByInvoiceNum_input:
   """ Required : 
   invoiceNum
   ds
   """  
   def __init__(self, obj):
      self.invoiceNum:int = obj["invoiceNum"]
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

class GetNewARPNHeadByInvoiceNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewARPNHeadTGLC_input:
   """ Required : 
   ds
   groupID
   headNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      self.headNum:int = obj["headNum"]
      pass

class GetNewARPNHeadTGLC_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewARPNHead_input:
   """ Required : 
   ds
   groupID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      pass

class GetNewARPNHead_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewBankTranByHeadNum_input:
   """ Required : 
   lvHeadNum
   lvBankAcctID
   ds
   """  
   def __init__(self, obj):
      self.lvHeadNum:int = obj["lvHeadNum"]
      self.lvBankAcctID:str = obj["lvBankAcctID"]
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

class GetNewBankTranByHeadNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewBankTranTGLC_input:
   """ Required : 
   ds
   bankAcctID
   tranNum
   voided
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      self.bankAcctID:str = obj["bankAcctID"]
      self.tranNum:int = obj["tranNum"]
      self.voided:bool = obj["voided"]
      pass

class GetNewBankTranTGLC_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewBankTranTaxDtl_input:
   """ Required : 
   ds
   sourceModule
   headNum
   apTranNo
   invoiceNum
   invoiceRef
   bankAcctID
   tranNum
   voided
   taxCode
   rateCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      self.sourceModule:str = obj["sourceModule"]
      self.headNum:int = obj["headNum"]
      self.apTranNo:int = obj["apTranNo"]
      self.invoiceNum:int = obj["invoiceNum"]
      self.invoiceRef:int = obj["invoiceRef"]
      self.bankAcctID:str = obj["bankAcctID"]
      self.tranNum:int = obj["tranNum"]
      self.voided:bool = obj["voided"]
      self.taxCode:str = obj["taxCode"]
      self.rateCode:str = obj["rateCode"]
      pass

class GetNewBankTranTaxDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewBankTran_input:
   """ Required : 
   ds
   bankAcctID
   tranNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      self.bankAcctID:str = obj["bankAcctID"]
      self.tranNum:int = obj["tranNum"]
      pass

class GetNewBankTran_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewTaxDtl_input:
   """ Required : 
   ds
   sourceModule
   headNum
   apTranNo
   invoiceNum
   invoiceRef
   bankAcctID
   tranNum
   voided
   taxCode
   rateCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      self.sourceModule:str = obj["sourceModule"]
      self.headNum:int = obj["headNum"]
      self.apTranNo:int = obj["apTranNo"]
      self.invoiceNum:int = obj["invoiceNum"]
      self.invoiceRef:int = obj["invoiceRef"]
      self.bankAcctID:str = obj["bankAcctID"]
      self.tranNum:int = obj["tranNum"]
      self.voided:bool = obj["voided"]
      self.taxCode:str = obj["taxCode"]
      self.rateCode:str = obj["rateCode"]
      pass

class GetNewTaxDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPITypePropByPMUID_input:
   """ Required : 
   ipPMUID
   """  
   def __init__(self, obj):
      self.ipPMUID:int = obj["ipPMUID"]
      """  PMUID  """  
      pass

class GetPITypePropByPMUID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opCustBankDtl:bool = obj["opCustBankDtl"]
      self.opInitiation:str = obj["parameters"]
      self.opBankAcctID:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetPNotesByGroupID_input:
   """ Required : 
   ipGroupID
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  ipGroupID  """  
      pass

class GetPNotesByGroupID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ARPNHeadListTableset] = obj["returnObj"]
      pass

class GetPNotesGenerated_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetPNotesGenerated_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ARPNHeadListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetPNotes_input:
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

class GetPNotes_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ARPNHeadListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRateCodeInfo_input:
   """ Required : 
   rateCode
   taxtbl
   ds
   """  
   def __init__(self, obj):
      self.rateCode:str = obj["rateCode"]
      """  Proposed RateCode value  """  
      self.taxtbl:str = obj["taxtbl"]
      """  Tax temp-table name  """  
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

class GetRateCodeInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows4Tracker_input:
   """ Required : 
   whereClauseARPNHead
   whereClauseARPNHeadAttch
   whereClauseBankTran
   whereClauseBankTranTaxDtl
   whereClauseBankTranTGLC
   whereClauseARPNDtl
   whereClauseTaxDtl
   whereClauseARPNHeadTGLC
   whereClauseARPNList
   whereClauseLegalNumGenOpts
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseARPNHead:str = obj["whereClauseARPNHead"]
      """  where condition for ARPNHead table  """  
      self.whereClauseARPNHeadAttch:str = obj["whereClauseARPNHeadAttch"]
      """  where condition for ARPNHeadAttch table  """  
      self.whereClauseBankTran:str = obj["whereClauseBankTran"]
      """  where condition for BankTran table  """  
      self.whereClauseBankTranTaxDtl:str = obj["whereClauseBankTranTaxDtl"]
      """  where condition for ClauseBankTranTaxDtl  """  
      self.whereClauseBankTranTGLC:str = obj["whereClauseBankTranTGLC"]
      """  where condition for ClauseBankTranTGLC  """  
      self.whereClauseARPNDtl:str = obj["whereClauseARPNDtl"]
      """  where condition for ClauseARPNDtl  """  
      self.whereClauseTaxDtl:str = obj["whereClauseTaxDtl"]
      """  where condition for ClauseTaxDtl  """  
      self.whereClauseARPNHeadTGLC:str = obj["whereClauseARPNHeadTGLC"]
      """  where condition for ClauseARPNHeadTGLC  """  
      self.whereClauseARPNList:str = obj["whereClauseARPNList"]
      """  where condition for ClauseARPNList  """  
      self.whereClauseLegalNumGenOpts:str = obj["whereClauseLegalNumGenOpts"]
      """  where condition for ClauseLegalNumGenOpts  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      pass

class GetRows4Tracker_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsByGrpIDExt_input:
   """ Required : 
   ipGroupiD
   dummy
   """  
   def __init__(self, obj):
      self.ipGroupiD:str = obj["ipGroupiD"]
      """  GroupID  """  
      self.dummy:str = obj["dummy"]
      """  dummy param which helps to refresh landing page on Kinetic  """  
      pass

class GetRowsByGrpIDExt_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ARPNHeadListTableset] = obj["returnObj"]
      pass

class GetRowsByGrpID_input:
   """ Required : 
   ipGroupiD
   """  
   def __init__(self, obj):
      self.ipGroupiD:str = obj["ipGroupiD"]
      """  Group ID  """  
      pass

class GetRowsByGrpID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ARPNHeadListTableset] = obj["returnObj"]
      pass

class GetRows_input:
   """ Required : 
   whereClauseARPNHead
   whereClauseARPNHeadAttch
   whereClauseBankTran
   whereClauseBankTranTaxDtl
   whereClauseBankTranTGLC
   whereClauseARPNDtl
   whereClauseTaxDtl
   whereClauseARPNHeadTGLC
   whereClauseARPNList
   whereClauseLegalNumGenOpts
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseARPNHead:str = obj["whereClauseARPNHead"]
      self.whereClauseARPNHeadAttch:str = obj["whereClauseARPNHeadAttch"]
      self.whereClauseBankTran:str = obj["whereClauseBankTran"]
      self.whereClauseBankTranTaxDtl:str = obj["whereClauseBankTranTaxDtl"]
      self.whereClauseBankTranTGLC:str = obj["whereClauseBankTranTGLC"]
      self.whereClauseARPNDtl:str = obj["whereClauseARPNDtl"]
      self.whereClauseTaxDtl:str = obj["whereClauseTaxDtl"]
      self.whereClauseARPNHeadTGLC:str = obj["whereClauseARPNHeadTGLC"]
      self.whereClauseARPNList:str = obj["whereClauseARPNList"]
      self.whereClauseLegalNumGenOpts:str = obj["whereClauseLegalNumGenOpts"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSalesTaxInfo_input:
   """ Required : 
   taxCode
   taxtbl
   ds
   """  
   def __init__(self, obj):
      self.taxCode:str = obj["taxCode"]
      """  Proposed TaxCode value  """  
      self.taxtbl:str = obj["taxtbl"]
      """  Tax temp-table name  """  
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

class GetSalesTaxInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetTaxableInfo_input:
   """ Required : 
   taxableAmt
   taxPercent
   fixedAmount
   taxtbl
   ds
   """  
   def __init__(self, obj):
      self.taxableAmt:int = obj["taxableAmt"]
      """  Proposed new taxable Amount  """  
      self.taxPercent:int = obj["taxPercent"]
      """  Proposed Tax Percent  """  
      self.fixedAmount:int = obj["fixedAmount"]
      """  Propoed Fixed Amount  """  
      self.taxtbl:str = obj["taxtbl"]
      """  tax temp-table name  """  
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

class GetTaxableInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetTranAmt_input:
   """ Required : 
   baseEntered
   ds
   """  
   def __init__(self, obj):
      self.baseEntered:bool = obj["baseEntered"]
      """  If the TranAmt field was updated then value should be yes, otherwise no  """  
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

class GetTranAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetUnapprovedPI_input:
   """ Required : 
   piGroup
   piPayMethodFilter
   """  
   def __init__(self, obj):
      self.piGroup:str = obj["piGroup"]
      """  Group ID  """  
      self.piPayMethodFilter:str = obj["piPayMethodFilter"]
      """  PayMethodFilter Filter  """  
      pass

class GetUnapprovedPI_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ARPNHeadListTableset] = obj["returnObj"]
      pass

class GetUnapprovedPIwithCount_input:
   """ Required : 
   piGroup
   piPayMethodFilter
   """  
   def __init__(self, obj):
      self.piGroup:str = obj["piGroup"]
      """  Group ID  """  
      self.piPayMethodFilter:str = obj["piPayMethodFilter"]
      """  PayMethodFilter Filter  """  
      pass

class GetUnapprovedPIwithCount_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ARPNHeadListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.opCreatedRecCounter:int = obj["parameters"]
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

class KineticFillPNSummary_input:
   """ Required : 
   ipcustNum
   ipStageFilter
   fromDays
   inRange
   """  
   def __init__(self, obj):
      self.ipcustNum:int = obj["ipcustNum"]
      """  The customer number  """  
      self.ipStageFilter:str = obj["ipStageFilter"]
      """  All, Open, Closed, or New  """  
      self.fromDays:int = obj["fromDays"]
      """  the amount of days to get a date from which the invoices will be selected.  """  
      self.inRange:bool = obj["inRange"]
      """  if the invoices will be selected from an specific date.  """  
      pass

class KineticFillPNSummary_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PNSummaryTableset] = obj["returnObj"]
      pass

class LeaveARPNHead_input:
   """ Required : 
   groupID
   headNum
   onAccount
   ds
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      """  Cash Receipt Group ID  """  
      self.headNum:int = obj["headNum"]
      """  Cash Receipt number  """  
      self.onAccount:bool = obj["onAccount"]
      """  Indicates if excess cash should go on account  """  
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

class LeaveARPNHead_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class MarkSent_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

class MarkSent_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class MarkSigned_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

class MarkSigned_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeBankAcctID_input:
   """ Required : 
   ipBankAcctID
   ds
   """  
   def __init__(self, obj):
      self.ipBankAcctID:str = obj["ipBankAcctID"]
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

class OnChangeBankAcctID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeBankFeeID_input:
   """ Required : 
   pcBankFeeID
   ds
   """  
   def __init__(self, obj):
      self.pcBankFeeID:str = obj["pcBankFeeID"]
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

class OnChangeBankFeeID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeType_input:
   """ Required : 
   pcType
   ds
   """  
   def __init__(self, obj):
      self.pcType:str = obj["pcType"]
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

class OnChangeType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PostPIGroupWithoutGL_input:
   """ Required : 
   ipGroupID
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  Group ID of PI  """  
      pass

class PostPIGroupWithoutGL_output:
   def __init__(self, obj):
      pass

class PostPNWithoutGL_input:
   """ Required : 
   ipGroupID
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  ipGroupID  """  
      pass

class PostPNWithoutGL_output:
   def __init__(self, obj):
      pass

class PrePostCheck_input:
   """ Required : 
   ipGroupID
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  Group ID of PI  """  
      pass

class PrePostCheck_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.vTaxQuestion:str = obj["parameters"]
      self.legalNumberMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class PreUpdate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

class PreUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      self.requiresUserInput:bool = obj["requiresUserInput"]
      pass

      """  output parameters  """  

class RecalcBankTax_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

class RecalcBankTax_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SetReadyToCalc_input:
   """ Required : 
   ipGroupID
   ipHeadNum
   ipInvoiceNum
   ipInvoiceRef
   ipBankAcctID
   ipTranNum
   ipVoided
   ipCalcAll
   ds
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  ipGroupID  """  
      self.ipHeadNum:int = obj["ipHeadNum"]
      """  ipHeadNum  """  
      self.ipInvoiceNum:int = obj["ipInvoiceNum"]
      """  ipInvoiceNum  """  
      self.ipInvoiceRef:int = obj["ipInvoiceRef"]
      """  ipInvoiceRef  """  
      self.ipBankAcctID:str = obj["ipBankAcctID"]
      """  ipBankAcctID  """  
      self.ipTranNum:int = obj["ipTranNum"]
      """  ipTranNum  """  
      self.ipVoided:bool = obj["ipVoided"]
      """  ipVoided  """  
      self.ipCalcAll:bool = obj["ipCalcAll"]
      """  ipCalcAll  """  
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

class SetReadyToCalc_output:
   def __init__(self, obj):
      pass

class SingleGenPIExt_input:
   """ Required : 
   ipCustNum
   ipCustId
   ipPIStatus
   ipPIType
   ipGroupID
   ipCurrencyCode
   ds
   """  
   def __init__(self, obj):
      self.ipCustNum:int = obj["ipCustNum"]
      self.ipCustId:str = obj["ipCustId"]
      self.ipPIStatus:str = obj["ipPIStatus"]
      self.ipPIType:str = obj["ipPIType"]
      self.ipGroupID:str = obj["ipGroupID"]
      self.ipCurrencyCode:str = obj["ipCurrencyCode"]
      self.ds:list[Erp_Tablesets_InvcsForCustTableset] = obj["ds"]
      pass

class SingleGenPIExt_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["returnObj"]
      pass

class SingleGenPI_input:
   """ Required : 
   ipCustNum
   ipCustId
   ipPIStatus
   ipPIType
   ipInvcList
   ipGroupID
   ipCurrencyCode
   """  
   def __init__(self, obj):
      self.ipCustNum:int = obj["ipCustNum"]
      """  ipCustNum  """  
      self.ipCustId:str = obj["ipCustId"]
      """  ipCustId  """  
      self.ipPIStatus:str = obj["ipPIStatus"]
      """  ipPIStatus  """  
      self.ipPIType:str = obj["ipPIType"]
      """  ipPIType  """  
      self.ipInvcList:str = obj["ipInvcList"]
      """  ipInvcList  """  
      self.ipGroupID:str = obj["ipGroupID"]
      """  ipGroupID  """  
      self.ipCurrencyCode:str = obj["ipCurrencyCode"]
      """  ipCurrencyCode  """  
      pass

class SingleGenPI_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["returnObj"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtARPromissoryNotesTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtARPromissoryNotesTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateARPIType_input:
   """ Required : 
   PIType
   """  
   def __init__(self, obj):
      self.PIType:str = obj["PIType"]
      pass

class ValidateARPIType_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  Bool  """  
      pass

class ValidateDuplicatedARPromNoteID_input:
   """ Required : 
   iARPromNoteID
   iPIType
   iCustID
   ds
   """  
   def __init__(self, obj):
      self.iARPromNoteID:str = obj["iARPromNoteID"]
      self.iPIType:str = obj["iPIType"]
      self.iCustID:str = obj["iCustID"]
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

class ValidateDuplicatedARPromNoteID_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class VoidLegalNumber_input:
   """ Required : 
   ipGroupID
   ipHeadNum
   ipVoidedReason
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  ARPN group identifier.  """  
      self.ipHeadNum:int = obj["ipHeadNum"]
      """  ARPN header number.  """  
      self.ipVoidedReason:str = obj["ipVoidedReason"]
      """  Indicates reason why legal number should be voided.  """  
      pass

class VoidLegalNumber_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ARPromissoryNotesTableset] = obj["returnObj"]
      pass

class WriteXMLFile_input:
   """ Required : 
   ipGroupID
   ipHeadNum
   ipFileName
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      self.ipHeadNum:int = obj["ipHeadNum"]
      self.ipFileName:str = obj["ipFileName"]
      pass

class WriteXMLFile_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  File Path on server  """  
      pass

