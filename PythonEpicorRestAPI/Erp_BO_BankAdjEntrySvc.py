import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.BankAdjEntrySvc
# Description: Bank Adjustment Entry Business Object
           bo/BankAdjEntry/BankAdjEntry.p
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_BankAdjEntries(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BankAdjEntries items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BankAdjEntries
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BankGrpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/BankAdjEntries",headers=creds) as resp:
           return await resp.json()

async def post_BankAdjEntries(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BankAdjEntries
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BankGrpRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.BankGrpRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/BankAdjEntries", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BankAdjEntries_Company_GroupID(Company, GroupID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BankAdjEntry item
   Description: Calls GetByID to retrieve the BankAdjEntry item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BankAdjEntry
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BankGrpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/BankAdjEntries(" + Company + "," + GroupID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BankAdjEntries_Company_GroupID(Company, GroupID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BankAdjEntry for the service
   Description: Calls UpdateExt to update BankAdjEntry. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BankAdjEntry
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.BankGrpRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/BankAdjEntries(" + Company + "," + GroupID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BankAdjEntries_Company_GroupID(Company, GroupID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BankAdjEntry item
   Description: Call UpdateExt to delete BankAdjEntry item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BankAdjEntry
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/BankAdjEntries(" + Company + "," + GroupID + ")",headers=creds) as resp:
           return await resp.json()

async def get_BankAdjEntries_Company_GroupID_BankTrans(Company, GroupID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get BankTrans items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BankTrans1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/BankAdjEntries(" + Company + "," + GroupID + ")/BankTrans",headers=creds) as resp:
           return await resp.json()

async def get_BankAdjEntries_Company_GroupID_BankTrans_Company_BankAcctID_TranNum_Voided(Company, GroupID, BankAcctID, TranNum, Voided, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BankTran item
   Description: Calls GetByID to retrieve the BankTran item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BankTran1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/BankAdjEntries(" + Company + "," + GroupID + ")/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/BankTrans",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/BankTrans", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")",headers=creds) as resp:
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
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")", json=requestBody,headers=creds) as resp:
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")/BankTranTaxDtls",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")/BankTranTaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")/BankTranTGLCs",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")/BankTranTGLCs(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + "," + SysRowID + ")",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/BankTranTaxDtls",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/BankTranTaxDtls", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/BankTranTaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
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
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/BankTranTaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", json=requestBody,headers=creds) as resp:
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/BankTranTaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/BankTranTGLCs",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/BankTranTGLCs", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/BankTranTGLCs(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + "," + SysRowID + ")",headers=creds) as resp:
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
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/BankTranTGLCs(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + "," + SysRowID + ")", json=requestBody,headers=creds) as resp:
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/BankTranTGLCs(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + "," + SysRowID + ")",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/LegalNumGenOpts",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/LegalNumGenOpts", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
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
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", json=requestBody,headers=creds) as resp:
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BankGrpListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseBankGrp, whereClauseBankTran, whereClauseBankTranTaxDtl, whereClauseBankTranTGLC, whereClauseLegalNumGenOpts, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseBankGrp=" + whereClauseBankGrp
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(groupID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "groupID=" + groupID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_BeforeGetBankGrp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BeforeGetBankGrp
   Description: This method checks to see if the selected Bank Group is valid (i.e. not in use by
other user and not a CashBook entry) before fetching the dataset.
   OperationID: BeforeGetBankGrp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BeforeGetBankGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BeforeGetBankGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeGrpBankAcct(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeGrpBankAcct
   Description: Call this method to update the BankGrp Bank Account information when the
Bank Account ID changes.
   OperationID: ChangeGrpBankAcct
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeGrpBankAcct_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeGrpBankAcct_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeGrpTranDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeGrpTranDate
   Description: Call this method to update the BankGrp fiscal period and year when the
transaction date changes.
   OperationID: ChangeGrpTranDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeGrpTranDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeGrpTranDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTranDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTranDate
   Description: Call this method to update the Rate field when the
Adjustment Transaction date changes.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteZeroAmtTaxRec(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteZeroAmtTaxRec
   Description: This method deletes TaxDtl records which have zero amounts
Since Payments TAx logic calculates tax conditionally only for the first tax line the invoice could have multiple zero tax records.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetByTranNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByTranNum
   Description: Same functionality as GetByID.  Except you can use BankAcctID and TranNum
to fetch the BankAdjEntryDataSet.
   OperationID: GetByTranNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByTranNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByTranNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetByTranNumAutoGen(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByTranNumAutoGen
   Description: Same functionality as GetByTranNum. Use only for Auto Bank Reconciliation.
   OperationID: GetByTranNumAutoGen
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByTranNumAutoGen_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByTranNumAutoGen_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetByTranNumTracker(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByTranNumTracker
   Description: Create new tableset and fills it with data, to use in tracker. Can load posted data (without group). Can create fake BankGrp! Use with extreme caution!
   OperationID: GetByTranNumTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByTranNumTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByTranNumTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBankGrpNoLock(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBankGrpNoLock
   Description: Inserts a new row in the DataSet with defaults populated. Active user locking disabled.
   OperationID: GetNewBankGrpNoLock
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBankGrpNoLock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBankGrpNoLock_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBankTran1(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBankTran1
   Description: This method is to be used in place of GetNewBankTran.  This method asks for
Group ID to link the Bank Adjustment Group (BankGrp) to BankTran.
   OperationID: GetNewBankTran1
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBankTran1_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBankTran1_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LeaveBankGrp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LeaveBankGrp
   Description: This method must be run whenever the use is leaving the current BankGrp record
(either by selecting a new Bank Group or by leaving the screen)
   OperationID: LeaveBankGrp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveBankGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveBankGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeBankFeeID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeBankFeeID
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetBankTranDefaultAccount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetBankTranDefaultAccount
   Description: This method is used to get the default account(s) for a Bank Fee
   OperationID: GetBankTranDefaultAccount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBankTranDefaultAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBankTranDefaultAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetReadyToCalc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetReadyToCalc
   Description: Purpose: CALCULATE VANTAGE\TAX CONNECT TAX CALCULATIONS
UI NEEDS TO CALL A SAVE BEFORE CALLING THIS PROCEDURE
Parameters:  none
Notes:
<param name="ipGroupID">ipGroupID </param><param name="ipTranNum">ipTranNum </param><param name="ipBankAcctID">ipBankAcctID </param><param name="ipVoided">ipVoided</param><param name="ipCalcAll">ipCalcAll</param><param name="ds">BankAdjEntry dataset</param>
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteMasterBankRec(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteMasterBankRec
   OperationID: DeleteMasterBankRec
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteMasterBankRec_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteMasterBankRec_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetByIDFiltered(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByIDFiltered
   Description: This method is created to get only BankTran records associated to the Bank adj group, filtering those records created by AP payment entry and cash receipt entry.
   OperationID: GetByIDFiltered
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByIDFiltered_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDFiltered_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetByIDFilteredNoLock(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByIDFilteredNoLock
   Description: This method is created to get only BankTran records associated to the Bank adj group, filtering those records created by AP payment entry and cash receipt entry.
Active user locking disabled.
   OperationID: GetByIDFilteredNoLock
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByIDFilteredNoLock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDFilteredNoLock_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AdjGroupExists(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AdjGroupExists
   Description: This method is called to check if group with entered ID exists
   OperationID: AdjGroupExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AdjGroupExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AdjGroupExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AssignLegalNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AssignLegalNumber
   Description: Assigns a legal number to the bank adjustment.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLegalNumGenOpts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetLegalNumGenOpts
   Description: This method will return a record in the LegalNumGenOpts datatable if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PrePostGrp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PrePostGrp
   Description: Method to call before posting bank adjustment group..  This method will check if there are
tax records with zero amounts and return
message text asking the user if they would like to continue with posting or delete these tax records before posting.
   OperationID: PrePostGrp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PrePostGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrePostGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateGLAccountOfAllLines(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateGLAccountOfAllLines
   Description: Validates GLAccounts for all Lines
   OperationID: ValidateGLAccountOfAllLines
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateGLAccountOfAllLines_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateGLAccountOfAllLines_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBankGrp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBankGrp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBankGrp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBankGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBankGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAdjEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankGrpListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_BankGrpListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankGrpRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_BankGrpRow] = obj["value"]
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

class Erp_Tablesets_BankGrpListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing transaction entry the user establishes a "Group ID". All transactions belong to a group. This current GroupID is assigned by the user.  Once created It can not be changed.  The Group ID is used to Selectively print and post the transactions.  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction Date.  The user enters the single date that will be used for posting of all the transaction within this batch. This date must be found in the Fiscal file. The Fiscal file provides the Fiscal Year and Period, which should be displayed for reference.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID that created this batch.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year. This is defaulted based on the finding the Fiscal master for the corresponding TranDate.  User can override this.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period for all  the transactions in this batch. Defaulted based on the Fiscal master which contains the TranDate period.  """  
      self.ActiveUserID:str = obj["ActiveUserID"]
      """  The user ID that is currently logged into this Group. This is displayed on the Group browser so that users may know which Groups are available.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Related record to a  BankAcct.  """  
      self.Cashbook:bool = obj["Cashbook"]
      """  if this group is created by the Cashbook then other programs can not select this group.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal Year Suffix. This is defaulted based on the finding the Fiscal period using the company calendar for the corresponding TranDate.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.RedStorno:bool = obj["RedStorno"]
      """  Red Storno Flag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BankCheckingAcct:str = obj["BankCheckingAcct"]
      """  Bank Checking Account number  """  
      self.BankCurrencyDesc:str = obj["BankCurrencyDesc"]
      """  Bank Currency Description  """  
      self.IsLcked:bool = obj["IsLcked"]
      """  Shows is this invoice is blocked in RvLock  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.LockStatus:str = obj["LockStatus"]
      """  Locked means can not be posted: an invoice is already in review journal or in posting process  """  
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      """  The Bank's full name.  """  
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      """  Full description of the bank account.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BankGrpRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing transaction entry the user establishes a "Group ID". All transactions belong to a group. This current GroupID is assigned by the user.  Once created It can not be changed.  The Group ID is used to Selectively print and post the transactions.  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction Date.  The user enters the single date that will be used for posting of all the transaction within this batch. This date must be found in the Fiscal file. The Fiscal file provides the Fiscal Year and Period, which should be displayed for reference.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID that created this batch.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year. This is defaulted based on the finding the Fiscal master for the corresponding TranDate.  User can override this.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period for all  the transactions in this batch. Defaulted based on the Fiscal master which contains the TranDate period.  """  
      self.ActiveUserID:str = obj["ActiveUserID"]
      """  The user ID that is currently logged into this Group. This is displayed on the Group browser so that users may know which Groups are available.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Related record to a  BankAcct.  """  
      self.Cashbook:bool = obj["Cashbook"]
      """  if this group is created by the Cashbook then other programs can not select this group.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal Year Suffix. This is defaulted based on the finding the Fiscal period using the company calendar for the corresponding TranDate.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.RedStorno:bool = obj["RedStorno"]
      """  Red Storno Flag  """  
      self.AutoGenerated:bool = obj["AutoGenerated"]
      """  AutoGenerated  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.BankCheckingAcct:str = obj["BankCheckingAcct"]
      """  Bank Checking Account number  """  
      self.BankCurrencyDesc:str = obj["BankCurrencyDesc"]
      """  Bank Currency Description  """  
      self.IsLcked:bool = obj["IsLcked"]
      """  Shows is this invoice is blocked in RvLock  """  
      self.LockStatus:str = obj["LockStatus"]
      """  Locked means can not be posted: an invoice is already in review journal or in posting process  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      self.XbSystSiteIsLegalEntity:bool = obj["XbSystSiteIsLegalEntity"]
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




#########################################################################
# Custom Schemas:
#########################################################################
class AdjGroupExists_input:
   """ Required : 
   ipGroupID
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      pass

class AdjGroupExists_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class AssignLegalNumber_input:
   """ Required : 
   BankAcctID
   TranNum
   Voided
   ds
   """  
   def __init__(self, obj):
      self.BankAcctID:str = obj["BankAcctID"]
      """  The bank account id.  """  
      self.TranNum:int = obj["TranNum"]
      """  The bank transaction number.  """  
      self.Voided:bool = obj["Voided"]
      """  The bank transaction voided value.  """  
      self.ds:list[Erp_Tablesets_BankAdjEntryTableset] = obj["ds"]
      pass

class AssignLegalNumber_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.LegalNumberMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_BankAdjEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class BeforeGetBankGrp_input:
   """ Required : 
   groupID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      """  Selected Bank Group ID  """  
      pass

class BeforeGetBankGrp_output:
   def __init__(self, obj):
      pass

class ChangeGrpBankAcct_input:
   """ Required : 
   ProposedBankAcctID
   ds
   """  
   def __init__(self, obj):
      self.ProposedBankAcctID:str = obj["ProposedBankAcctID"]
      """  The proposed Bank Account ID  """  
      self.ds:list[Erp_Tablesets_BankAdjEntryTableset] = obj["ds"]
      pass

class ChangeGrpBankAcct_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankAdjEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeGrpTranDate_input:
   """ Required : 
   ProposedTranDate
   ds
   """  
   def __init__(self, obj):
      self.ProposedTranDate:str = obj["ProposedTranDate"]
      """  The proposed Transaction Date  """  
      self.ds:list[Erp_Tablesets_BankAdjEntryTableset] = obj["ds"]
      pass

class ChangeGrpTranDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankAdjEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeTranAmt_input:
   """ Required : 
   ipTranAmtType
   ProposedTranAmt
   ds
   """  
   def __init__(self, obj):
      self.ipTranAmtType:str = obj["ipTranAmtType"]
      """  Indicate which of the transaction amount is changed.
            Valid values are: [R]B|D
            R - Recalculation or exchange rates required
            B - for Base Tran Amount
            D - for Doc Tran Amount  """  
      self.ProposedTranAmt:int = obj["ProposedTranAmt"]
      """  The proposed Transaction Amount  """  
      self.ds:list[Erp_Tablesets_BankAdjEntryTableset] = obj["ds"]
      pass

class ChangeTranAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankAdjEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeTranDate_input:
   """ Required : 
   ProposedTranDate
   ds
   """  
   def __init__(self, obj):
      self.ProposedTranDate:str = obj["ProposedTranDate"]
      """  The proposed Adjustment Transaction Date  """  
      self.ds:list[Erp_Tablesets_BankAdjEntryTableset] = obj["ds"]
      pass

class ChangeTranDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankAdjEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckDocumentIsLocked_input:
   """ Required : 
   vGroupID
   """  
   def __init__(self, obj):
      self.vGroupID:str = obj["vGroupID"]
      """  GroupID  """  
      pass

class CheckDocumentIsLocked_output:
   def __init__(self, obj):
      pass

class DeleteByID_input:
   """ Required : 
   groupID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteMasterBankRec_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BankAdjEntryTableset] = obj["ds"]
      pass

class DeleteMasterBankRec_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankAdjEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

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

class Erp_Tablesets_BankAdjEntryTableset:
   def __init__(self, obj):
      self.BankGrp:list[Erp_Tablesets_BankGrpRow] = obj["BankGrp"]
      self.BankTran:list[Erp_Tablesets_BankTranRow] = obj["BankTran"]
      self.BankTranTaxDtl:list[Erp_Tablesets_BankTranTaxDtlRow] = obj["BankTranTaxDtl"]
      self.BankTranTGLC:list[Erp_Tablesets_BankTranTGLCRow] = obj["BankTranTGLC"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_BankGrpListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing transaction entry the user establishes a "Group ID". All transactions belong to a group. This current GroupID is assigned by the user.  Once created It can not be changed.  The Group ID is used to Selectively print and post the transactions.  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction Date.  The user enters the single date that will be used for posting of all the transaction within this batch. This date must be found in the Fiscal file. The Fiscal file provides the Fiscal Year and Period, which should be displayed for reference.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID that created this batch.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year. This is defaulted based on the finding the Fiscal master for the corresponding TranDate.  User can override this.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period for all  the transactions in this batch. Defaulted based on the Fiscal master which contains the TranDate period.  """  
      self.ActiveUserID:str = obj["ActiveUserID"]
      """  The user ID that is currently logged into this Group. This is displayed on the Group browser so that users may know which Groups are available.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Related record to a  BankAcct.  """  
      self.Cashbook:bool = obj["Cashbook"]
      """  if this group is created by the Cashbook then other programs can not select this group.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal Year Suffix. This is defaulted based on the finding the Fiscal period using the company calendar for the corresponding TranDate.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.RedStorno:bool = obj["RedStorno"]
      """  Red Storno Flag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BankCheckingAcct:str = obj["BankCheckingAcct"]
      """  Bank Checking Account number  """  
      self.BankCurrencyDesc:str = obj["BankCurrencyDesc"]
      """  Bank Currency Description  """  
      self.IsLcked:bool = obj["IsLcked"]
      """  Shows is this invoice is blocked in RvLock  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.LockStatus:str = obj["LockStatus"]
      """  Locked means can not be posted: an invoice is already in review journal or in posting process  """  
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      """  The Bank's full name.  """  
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      """  Full description of the bank account.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BankGrpListTableset:
   def __init__(self, obj):
      self.BankGrpList:list[Erp_Tablesets_BankGrpListRow] = obj["BankGrpList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_BankGrpRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing transaction entry the user establishes a "Group ID". All transactions belong to a group. This current GroupID is assigned by the user.  Once created It can not be changed.  The Group ID is used to Selectively print and post the transactions.  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction Date.  The user enters the single date that will be used for posting of all the transaction within this batch. This date must be found in the Fiscal file. The Fiscal file provides the Fiscal Year and Period, which should be displayed for reference.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID that created this batch.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year. This is defaulted based on the finding the Fiscal master for the corresponding TranDate.  User can override this.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period for all  the transactions in this batch. Defaulted based on the Fiscal master which contains the TranDate period.  """  
      self.ActiveUserID:str = obj["ActiveUserID"]
      """  The user ID that is currently logged into this Group. This is displayed on the Group browser so that users may know which Groups are available.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Related record to a  BankAcct.  """  
      self.Cashbook:bool = obj["Cashbook"]
      """  if this group is created by the Cashbook then other programs can not select this group.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal Year Suffix. This is defaulted based on the finding the Fiscal period using the company calendar for the corresponding TranDate.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.RedStorno:bool = obj["RedStorno"]
      """  Red Storno Flag  """  
      self.AutoGenerated:bool = obj["AutoGenerated"]
      """  AutoGenerated  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.BankCheckingAcct:str = obj["BankCheckingAcct"]
      """  Bank Checking Account number  """  
      self.BankCurrencyDesc:str = obj["BankCurrencyDesc"]
      """  Bank Currency Description  """  
      self.IsLcked:bool = obj["IsLcked"]
      """  Shows is this invoice is blocked in RvLock  """  
      self.LockStatus:str = obj["LockStatus"]
      """  Locked means can not be posted: an invoice is already in review journal or in posting process  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      self.XbSystSiteIsLegalEntity:bool = obj["XbSystSiteIsLegalEntity"]
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

class Erp_Tablesets_UpdExtBankAdjEntryTableset:
   def __init__(self, obj):
      self.BankGrp:list[Erp_Tablesets_BankGrpRow] = obj["BankGrp"]
      self.BankTran:list[Erp_Tablesets_BankTranRow] = obj["BankTran"]
      self.BankTranTaxDtl:list[Erp_Tablesets_BankTranTaxDtlRow] = obj["BankTranTaxDtl"]
      self.BankTranTGLC:list[Erp_Tablesets_BankTranTGLCRow] = obj["BankTranTGLC"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetBankTranDefaultAccount_input:
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
      self.ds:list[Erp_Tablesets_BankAdjEntryTableset] = obj["ds"]
      pass

class GetBankTranDefaultAccount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankAdjEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetByIDFilteredNoLock_input:
   """ Required : 
   groupID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      """  Bankd Adj Entry group ID  """  
      pass

class GetByIDFilteredNoLock_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_BankAdjEntryTableset] = obj["returnObj"]
      pass

class GetByIDFiltered_input:
   """ Required : 
   groupID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      """  Bankd Adj Entry group ID  """  
      pass

class GetByIDFiltered_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_BankAdjEntryTableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   groupID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_BankAdjEntryTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_BankAdjEntryTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_BankAdjEntryTableset] = obj["returnObj"]
      pass

class GetByTranNumAutoGen_input:
   """ Required : 
   pcBankAcctID
   piTranNum
   """  
   def __init__(self, obj):
      self.pcBankAcctID:str = obj["pcBankAcctID"]
      """  Bank Acct ID  """  
      self.piTranNum:int = obj["piTranNum"]
      """  BankTran.TranNum  """  
      pass

class GetByTranNumAutoGen_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_BankAdjEntryTableset] = obj["returnObj"]
      pass

class GetByTranNumTracker_input:
   """ Required : 
   pBankAcctId
   pTranNum
   pVoided
   """  
   def __init__(self, obj):
      self.pBankAcctId:str = obj["pBankAcctId"]
      """  Bank Acct ID  """  
      self.pTranNum:int = obj["pTranNum"]
      """  BankTran TranNum  """  
      self.pVoided:bool = obj["pVoided"]
      """  BankTran Voided  """  
      pass

class GetByTranNumTracker_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_BankAdjEntryTableset] = obj["returnObj"]
      pass

class GetByTranNum_input:
   """ Required : 
   pcBankAcctID
   piTranNum
   plVoided
   """  
   def __init__(self, obj):
      self.pcBankAcctID:str = obj["pcBankAcctID"]
      """  Bank Acct ID  """  
      self.piTranNum:int = obj["piTranNum"]
      """  BankTran.TranNum  """  
      self.plVoided:bool = obj["plVoided"]
      """  BankTran.Voided  """  
      pass

class GetByTranNum_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_BankAdjEntryTableset] = obj["returnObj"]
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

class GetLegalNumGenOpts_input:
   """ Required : 
   ds
   BankAcctID
   TranNum
   Voided
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BankAdjEntryTableset] = obj["ds"]
      self.BankAcctID:str = obj["BankAcctID"]
      """  Bank Account ID  """  
      self.TranNum:int = obj["TranNum"]
      """  Bank Tran Number  """  
      self.Voided:bool = obj["Voided"]
      """  Bank Tran Voided  """  
      pass

class GetLegalNumGenOpts_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankAdjEntryTableset] = obj["ds"]
      self.RequiresUserInput:bool = obj["RequiresUserInput"]
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
      self.returnObj:list[Erp_Tablesets_BankGrpListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewBankGrpNoLock_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BankAdjEntryTableset] = obj["ds"]
      pass

class GetNewBankGrpNoLock_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankAdjEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewBankGrp_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BankAdjEntryTableset] = obj["ds"]
      pass

class GetNewBankGrp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankAdjEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewBankTran1_input:
   """ Required : 
   ds
   vGroupID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BankAdjEntryTableset] = obj["ds"]
      self.vGroupID:str = obj["vGroupID"]
      """  The Bank Adjustment Group ID  """  
      pass

class GetNewBankTran1_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankAdjEntryTableset] = obj["ds"]
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
      self.ds:list[Erp_Tablesets_BankAdjEntryTableset] = obj["ds"]
      self.bankAcctID:str = obj["bankAcctID"]
      self.tranNum:int = obj["tranNum"]
      self.voided:bool = obj["voided"]
      pass

class GetNewBankTranTGLC_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankAdjEntryTableset] = obj["ds"]
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
      self.ds:list[Erp_Tablesets_BankAdjEntryTableset] = obj["ds"]
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
      self.ds:list[Erp_Tablesets_BankAdjEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewBankTran_input:
   """ Required : 
   ds
   bankAcctID
   tranNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BankAdjEntryTableset] = obj["ds"]
      self.bankAcctID:str = obj["bankAcctID"]
      self.tranNum:int = obj["tranNum"]
      pass

class GetNewBankTran_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankAdjEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRateCodeInfo_input:
   """ Required : 
   rateCode
   ds
   """  
   def __init__(self, obj):
      self.rateCode:str = obj["rateCode"]
      """  Proposed RateCode value  """  
      self.ds:list[Erp_Tablesets_BankAdjEntryTableset] = obj["ds"]
      pass

class GetRateCodeInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankAdjEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseBankGrp
   whereClauseBankTran
   whereClauseBankTranTaxDtl
   whereClauseBankTranTGLC
   whereClauseLegalNumGenOpts
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseBankGrp:str = obj["whereClauseBankGrp"]
      self.whereClauseBankTran:str = obj["whereClauseBankTran"]
      self.whereClauseBankTranTaxDtl:str = obj["whereClauseBankTranTaxDtl"]
      self.whereClauseBankTranTGLC:str = obj["whereClauseBankTranTGLC"]
      self.whereClauseLegalNumGenOpts:str = obj["whereClauseLegalNumGenOpts"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_BankAdjEntryTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSalesTaxInfo_input:
   """ Required : 
   taxCode
   ds
   """  
   def __init__(self, obj):
      self.taxCode:str = obj["taxCode"]
      """  Proposed TaxCode value  """  
      self.ds:list[Erp_Tablesets_BankAdjEntryTableset] = obj["ds"]
      pass

class GetSalesTaxInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankAdjEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetTaxableInfo_input:
   """ Required : 
   taxableAmt
   taxPercent
   fixedAmount
   ds
   """  
   def __init__(self, obj):
      self.taxableAmt:int = obj["taxableAmt"]
      """  Proposed new taxable Amount  """  
      self.taxPercent:int = obj["taxPercent"]
      """  Proposed Tax Percent  """  
      self.fixedAmount:int = obj["fixedAmount"]
      """  Propoed Fixed Amount  """  
      self.ds:list[Erp_Tablesets_BankAdjEntryTableset] = obj["ds"]
      pass

class GetTaxableInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankAdjEntryTableset] = obj["ds"]
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

class LeaveBankGrp_input:
   """ Required : 
   groupID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      """  Bank Group ID to clear  """  
      pass

class LeaveBankGrp_output:
   def __init__(self, obj):
      pass

class OnChangeBankFeeID_input:
   """ Required : 
   pcBankFeeID
   ds
   """  
   def __init__(self, obj):
      self.pcBankFeeID:str = obj["pcBankFeeID"]
      self.ds:list[Erp_Tablesets_BankAdjEntryTableset] = obj["ds"]
      pass

class OnChangeBankFeeID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankAdjEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PrePostGrp_input:
   """ Required : 
   postGroupID
   """  
   def __init__(self, obj):
      self.postGroupID:str = obj["postGroupID"]
      """  The Group ID of the Group to post  """  
      pass

class PrePostGrp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.taxRecMessage:str = obj["parameters"]
      self.legalNumberMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class PreUpdate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BankAdjEntryTableset] = obj["ds"]
      pass

class PreUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankAdjEntryTableset] = obj["ds"]
      self.requiresUserInput:bool = obj["requiresUserInput"]
      pass

      """  output parameters  """  

class RecalcBankTax_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BankAdjEntryTableset] = obj["ds"]
      pass

class RecalcBankTax_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankAdjEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SetReadyToCalc_input:
   """ Required : 
   ipGroupID
   ipTranNum
   ipBankAcctID
   ipVoided
   ipCalcAll
   ds
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      self.ipTranNum:int = obj["ipTranNum"]
      self.ipBankAcctID:str = obj["ipBankAcctID"]
      self.ipVoided:bool = obj["ipVoided"]
      self.ipCalcAll:bool = obj["ipCalcAll"]
      self.ds:list[Erp_Tablesets_BankAdjEntryTableset] = obj["ds"]
      pass

class SetReadyToCalc_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankAdjEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtBankAdjEntryTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtBankAdjEntryTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BankAdjEntryTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankAdjEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateGLAccountOfAllLines_input:
   """ Required : 
   groupID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      pass

class ValidateGLAccountOfAllLines_output:
   def __init__(self, obj):
      pass

class VoidLegalNumber_input:
   """ Required : 
   BankAcctID
   TranNum
   Voided
   VoidedReason
   ds
   """  
   def __init__(self, obj):
      self.BankAcctID:str = obj["BankAcctID"]
      """  Bank Account ID  """  
      self.TranNum:int = obj["TranNum"]
      """  Bank Transaction number  """  
      self.Voided:bool = obj["Voided"]
      """  Bank Transaction Voided value  """  
      self.VoidedReason:str = obj["VoidedReason"]
      """  Reason for the void  """  
      self.ds:list[Erp_Tablesets_BankAdjEntryTableset] = obj["ds"]
      pass

class VoidLegalNumber_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankAdjEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

